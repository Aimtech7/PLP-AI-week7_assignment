"""
Fairness Audit Tool for COMPAS Dataset
=======================================

This module provides functions to audit machine learning models for fairness
using the COMPAS recidivism dataset. It calculates various fairness metrics
and generates visualizations to identify potential bias.

Usage:
    python fairness_audit.py --input ../data/compas_dataset.csv

Author: AI Ethics Assignment
License: MIT
"""

import argparse
import os
import sys
from typing import Dict, Tuple, Optional
import warnings

warnings.filterwarnings('ignore')

try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.metrics import confusion_matrix, classification_report
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from aif360.datasets import BinaryLabelDataset
    from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
    from aif360.algorithms.preprocessing import Reweighing
except ImportError as e:
    print(f"Error: Required package not installed: {e}")
    print("\nPlease install required packages:")
    print("pip install numpy pandas matplotlib seaborn scikit-learn aif360")
    sys.exit(1)


class FairnessAuditor:
    """
    A class to perform fairness audits on machine learning models.
    """

    def __init__(self, output_dir: str = "outputs"):
        """
        Initialize the FairnessAuditor.

        Args:
            output_dir: Directory to save output files and visualizations
        """
        self.output_dir = output_dir
        self.df = None
        self.dataset = None
        self.metrics = {}

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")

    def load_compas_data(self, filepath: str) -> pd.DataFrame:
        """
        Load and preprocess the COMPAS dataset.

        Args:
            filepath: Path to the COMPAS CSV file

        Returns:
            Preprocessed pandas DataFrame
        """
        print(f"\nLoading data from: {filepath}")

        try:
            df = pd.read_csv(filepath)
            print(f"Loaded {len(df)} records")

            required_columns = ['race', 'sex', 'age', 'priors_count',
                              'two_year_recid', 'decile_score']
            missing_cols = [col for col in required_columns if col not in df.columns]

            if missing_cols:
                print(f"Warning: Missing columns: {missing_cols}")
                print("Available columns:", df.columns.tolist())
                return None

            df = df[
                (df['days_b_screening_arrest'] <= 30) &
                (df['days_b_screening_arrest'] >= -30) &
                (df['is_recid'] != -1) &
                (df['c_charge_degree'] != 'O') &
                (df['score_text'] != 'N/A')
            ].copy()

            df['race_binary'] = df['race'].apply(
                lambda x: 1 if x == 'African-American' else 0
            )
            df['sex_binary'] = df['sex'].apply(lambda x: 1 if x == 'Male' else 0)

            df['high_risk'] = (df['decile_score'] >= 5).astype(int)

            print(f"Preprocessed data: {len(df)} records")
            print(f"\nRace distribution:")
            print(df['race'].value_counts())
            print(f"\nGender distribution:")
            print(df['sex'].value_counts())

            self.df = df
            return df

        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def calculate_fairness_metrics(self,
                                   protected_attribute: str = 'race_binary',
                                   label_column: str = 'two_year_recid',
                                   prediction_column: str = 'high_risk') -> Dict:
        """
        Calculate comprehensive fairness metrics.

        Args:
            protected_attribute: Column name for protected attribute
            label_column: Column name for ground truth labels
            prediction_column: Column name for model predictions

        Returns:
            Dictionary containing fairness metrics
        """
        print(f"\nCalculating fairness metrics...")
        print(f"Protected attribute: {protected_attribute}")

        df = self.df
        metrics = {}

        privileged = df[df[protected_attribute] == 0]
        unprivileged = df[df[protected_attribute] == 1]

        metrics['privileged_group_size'] = len(privileged)
        metrics['unprivileged_group_size'] = len(unprivileged)

        priv_positive_rate = privileged[prediction_column].mean()
        unpriv_positive_rate = unprivileged[prediction_column].mean()

        metrics['disparate_impact'] = unpriv_positive_rate / priv_positive_rate if priv_positive_rate > 0 else 0
        metrics['statistical_parity_diff'] = unpriv_positive_rate - priv_positive_rate

        def calculate_rates(group_df):
            y_true = group_df[label_column]
            y_pred = group_df[prediction_column]

            tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

            tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
            fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
            tnr = tn / (tn + fp) if (tn + fp) > 0 else 0
            fnr = fn / (fn + tp) if (fn + tp) > 0 else 0

            return {
                'TPR': tpr, 'FPR': fpr, 'TNR': tnr, 'FNR': fnr,
                'TP': tp, 'FP': fp, 'TN': tn, 'FN': fn
            }

        priv_rates = calculate_rates(privileged)
        unpriv_rates = calculate_rates(unprivileged)

        metrics['privileged_TPR'] = priv_rates['TPR']
        metrics['unprivileged_TPR'] = unpriv_rates['TPR']
        metrics['equal_opportunity_diff'] = unpriv_rates['TPR'] - priv_rates['TPR']

        metrics['privileged_FPR'] = priv_rates['FPR']
        metrics['unprivileged_FPR'] = unpriv_rates['FPR']
        metrics['equalized_odds_diff'] = abs(unpriv_rates['TPR'] - priv_rates['TPR']) + abs(unpriv_rates['FPR'] - priv_rates['FPR'])

        metrics['privileged_rates'] = priv_rates
        metrics['unprivileged_rates'] = unpriv_rates

        self.metrics = metrics
        return metrics

    def print_fairness_report(self):
        """
        Print a formatted fairness audit report.
        """
        print("\n" + "="*70)
        print("FAIRNESS AUDIT REPORT")
        print("="*70)

        metrics = self.metrics

        print(f"\n📊 DATASET STATISTICS")
        print(f"   Privileged group size: {metrics['privileged_group_size']}")
        print(f"   Unprivileged group size: {metrics['unprivileged_group_size']}")

        print(f"\n⚖️  FAIRNESS METRICS")

        print(f"\n1. Disparate Impact: {metrics['disparate_impact']:.3f}")
        if 0.8 <= metrics['disparate_impact'] <= 1.25:
            print("   ✅ PASS - Within acceptable range (0.8-1.25)")
        else:
            print("   ❌ FAIL - Outside acceptable range (0.8-1.25)")

        print(f"\n2. Statistical Parity Difference: {metrics['statistical_parity_diff']:.3f}")
        if abs(metrics['statistical_parity_diff']) < 0.1:
            print("   ✅ PASS - Minimal difference")
        else:
            print("   ❌ FAIL - Significant difference")

        print(f"\n3. Equal Opportunity (TPR Difference): {metrics['equal_opportunity_diff']:.3f}")
        if abs(metrics['equal_opportunity_diff']) < 0.1:
            print("   ✅ PASS - Minimal difference")
        else:
            print("   ❌ FAIL - Significant difference")

        print(f"\n4. Equalized Odds Difference: {metrics['equalized_odds_diff']:.3f}")
        if metrics['equalized_odds_diff'] < 0.1:
            print("   ✅ PASS - Minimal difference")
        else:
            print("   ❌ FAIL - Significant difference")

        print(f"\n📈 DETAILED RATES")
        print(f"\n   Privileged Group:")
        print(f"      True Positive Rate (TPR): {metrics['privileged_TPR']:.3f}")
        print(f"      False Positive Rate (FPR): {metrics['privileged_FPR']:.3f}")

        print(f"\n   Unprivileged Group:")
        print(f"      True Positive Rate (TPR): {metrics['unprivileged_TPR']:.3f}")
        print(f"      False Positive Rate (FPR): {metrics['unprivileged_FPR']:.3f}")

        print("\n" + "="*70)

    def visualize_fairness_metrics(self):
        """
        Create comprehensive visualizations of fairness metrics.
        """
        print("\n📊 Generating visualizations...")

        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('COMPAS Fairness Audit - Visualization Report',
                    fontsize=16, fontweight='bold')

        metrics = self.metrics

        ax1 = axes[0, 0]
        groups = ['Privileged\n(Non-Black)', 'Unprivileged\n(Black)']
        sizes = [metrics['privileged_group_size'], metrics['unprivileged_group_size']]
        colors = ['#3498db', '#e74c3c']
        ax1.bar(groups, sizes, color=colors, alpha=0.7, edgecolor='black')
        ax1.set_ylabel('Number of Individuals', fontweight='bold')
        ax1.set_title('Dataset Distribution by Race', fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)

        for i, v in enumerate(sizes):
            ax1.text(i, v + 50, str(v), ha='center', fontweight='bold')

        ax2 = axes[0, 1]
        rates_data = {
            'Privileged': [metrics['privileged_TPR'], metrics['privileged_FPR']],
            'Unprivileged': [metrics['unprivileged_TPR'], metrics['unprivileged_FPR']]
        }
        x = np.arange(2)
        width = 0.35
        ax2.bar(x - width/2, rates_data['Privileged'], width,
               label='Privileged', color='#3498db', alpha=0.7)
        ax2.bar(x + width/2, rates_data['Unprivileged'], width,
               label='Unprivileged', color='#e74c3c', alpha=0.7)
        ax2.set_ylabel('Rate', fontweight='bold')
        ax2.set_title('True Positive Rate (TPR) and False Positive Rate (FPR)',
                     fontweight='bold')
        ax2.set_xticks(x)
        ax2.set_xticklabels(['TPR', 'FPR'])
        ax2.legend()
        ax2.grid(axis='y', alpha=0.3)

        ax3 = axes[1, 0]
        fairness_metrics_names = ['Disparate\nImpact', 'Stat. Parity\nDiff',
                                 'Equal Opp.\nDiff', 'Equal. Odds\nDiff']
        fairness_values = [
            metrics['disparate_impact'],
            metrics['statistical_parity_diff'],
            metrics['equal_opportunity_diff'],
            metrics['equalized_odds_diff']
        ]
        colors_fairness = ['#e74c3c' if abs(v - 1) > 0.2 or abs(v) > 0.1
                          else '#2ecc71' for v in fairness_values]
        ax3.bar(fairness_metrics_names, fairness_values,
               color=colors_fairness, alpha=0.7, edgecolor='black')
        ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
        ax3.axhline(y=0.8, color='orange', linestyle='--', linewidth=1,
                   label='Fairness threshold (0.8-1.25)')
        ax3.axhline(y=1.25, color='orange', linestyle='--', linewidth=1)
        ax3.set_ylabel('Metric Value', fontweight='bold')
        ax3.set_title('Fairness Metrics Summary', fontweight='bold')
        ax3.legend()
        ax3.grid(axis='y', alpha=0.3)

        ax4 = axes[1, 1]
        cm_priv = [[metrics['privileged_rates']['TN'], metrics['privileged_rates']['FP']],
                   [metrics['privileged_rates']['FN'], metrics['privileged_rates']['TP']]]
        cm_unpriv = [[metrics['unprivileged_rates']['TN'], metrics['unprivileged_rates']['FP']],
                     [metrics['unprivileged_rates']['FN'], metrics['unprivileged_rates']['TP']]]

        ax4.text(0.5, 0.95, 'Confusion Matrices Comparison',
                ha='center', va='top', transform=ax4.transAxes,
                fontsize=12, fontweight='bold')

        ax4.text(0.25, 0.75, 'Privileged Group',
                ha='center', transform=ax4.transAxes, fontweight='bold')
        ax4.text(0.25, 0.65, f"TN: {cm_priv[0][0]}  FP: {cm_priv[0][1]}",
                ha='center', transform=ax4.transAxes, fontsize=10)
        ax4.text(0.25, 0.55, f"FN: {cm_priv[1][0]}  TP: {cm_priv[1][1]}",
                ha='center', transform=ax4.transAxes, fontsize=10)

        ax4.text(0.75, 0.75, 'Unprivileged Group',
                ha='center', transform=ax4.transAxes, fontweight='bold')
        ax4.text(0.75, 0.65, f"TN: {cm_unpriv[0][0]}  FP: {cm_unpriv[0][1]}",
                ha='center', transform=ax4.transAxes, fontsize=10)
        ax4.text(0.75, 0.55, f"FN: {cm_unpriv[1][0]}  TP: {cm_unpriv[1][1]}",
                ha='center', transform=ax4.transAxes, fontsize=10)

        ax4.axis('off')

        plt.tight_layout()

        output_path = os.path.join(self.output_dir, 'fairness_audit_visualizations.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✅ Visualizations saved to: {output_path}")

        plt.show()

    def generate_recommendations(self) -> str:
        """
        Generate bias mitigation recommendations based on audit results.

        Returns:
            Formatted recommendations text
        """
        recommendations = []
        metrics = self.metrics

        recommendations.append("\n" + "="*70)
        recommendations.append("BIAS MITIGATION RECOMMENDATIONS")
        recommendations.append("="*70)

        if metrics['disparate_impact'] < 0.8 or metrics['disparate_impact'] > 1.25:
            recommendations.append("\n🔴 HIGH PRIORITY - Disparate Impact Issue Detected")
            recommendations.append("   Recommended Actions:")
            recommendations.append("   1. Apply Reweighing preprocessing to balance outcomes")
            recommendations.append("   2. Use threshold optimization for different groups")
            recommendations.append("   3. Consider collecting more representative training data")

        if abs(metrics['equal_opportunity_diff']) > 0.1:
            recommendations.append("\n🟠 MEDIUM PRIORITY - Equal Opportunity Violation")
            recommendations.append("   Recommended Actions:")
            recommendations.append("   1. Implement adversarial debiasing during training")
            recommendations.append("   2. Apply post-processing calibration techniques")
            recommendations.append("   3. Review feature selection for proxy discrimination")

        if metrics['equalized_odds_diff'] > 0.1:
            recommendations.append("\n🟠 MEDIUM PRIORITY - Equalized Odds Violation")
            recommendations.append("   Recommended Actions:")
            recommendations.append("   1. Use reject option classification (post-processing)")
            recommendations.append("   2. Apply fairness constraints during model training")
            recommendations.append("   3. Implement separate decision thresholds per group")

        recommendations.append("\n📚 GENERAL BEST PRACTICES:")
        recommendations.append("   • Conduct regular fairness audits (quarterly minimum)")
        recommendations.append("   • Maintain diverse development and testing teams")
        recommendations.append("   • Document all fairness considerations and decisions")
        recommendations.append("   • Establish clear accountability for fairness outcomes")
        recommendations.append("   • Implement human oversight for high-stakes decisions")

        recommendations.append("\n🔧 TECHNICAL INTERVENTIONS:")
        recommendations.append("   Pre-processing: Reweighing, Disparate Impact Remover")
        recommendations.append("   In-processing: Adversarial Debiasing, Prejudice Remover")
        recommendations.append("   Post-processing: Equalized Odds, Calibrated Odds")

        recommendations.append("\n" + "="*70 + "\n")

        recommendations_text = "\n".join(recommendations)
        print(recommendations_text)

        output_path = os.path.join(self.output_dir, 'recommendations.txt')
        with open(output_path, 'w') as f:
            f.write(recommendations_text)
        print(f"✅ Recommendations saved to: {output_path}")

        return recommendations_text


def main():
    """
    Main function to run the fairness audit from command line.
    """
    parser = argparse.ArgumentParser(
        description='Fairness Audit Tool for COMPAS Dataset',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python fairness_audit.py --input ../data/compas_dataset.csv
  python fairness_audit.py --input data.csv --output results/
        """
    )

    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='Path to COMPAS dataset CSV file'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='outputs',
        help='Output directory for results (default: outputs/)'
    )

    parser.add_argument(
        '--protected-attr',
        type=str,
        default='race_binary',
        help='Protected attribute column name (default: race_binary)'
    )

    args = parser.parse_args()

    print("\n" + "="*70)
    print("COMPAS FAIRNESS AUDIT TOOL")
    print("="*70)

    auditor = FairnessAuditor(output_dir=args.output)

    df = auditor.load_compas_data(args.input)
    if df is None:
        print("\n❌ Error: Failed to load data. Please check the file path and format.")
        sys.exit(1)

    metrics = auditor.calculate_fairness_metrics(
        protected_attribute=args.protected_attr
    )

    auditor.print_fairness_report()

    auditor.visualize_fairness_metrics()

    auditor.generate_recommendations()

    print("\n✅ Fairness audit completed successfully!")
    print(f"📁 Results saved to: {args.output}/")


if __name__ == "__main__":
    main()
