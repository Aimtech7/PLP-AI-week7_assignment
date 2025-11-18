# COMPAS Dataset

## Dataset Information

This directory should contain the COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) dataset used for fairness auditing in Part 3 of the assignment.

## Download Instructions

### Option 1: Automatic Download (Recommended)

The Jupyter notebook (`Fairness_Audit_COMPAS.ipynb`) includes code to automatically download the dataset. Simply run the notebook and the dataset will be fetched automatically.

### Option 2: Manual Download

1. Visit the ProPublica COMPAS Analysis repository:
   https://github.com/propublica/compas-analysis

2. Download the file: `compas-scores-two-years.csv`

3. Save it to this directory with the filename: `compas_dataset.csv`

### Option 3: Direct Download

You can download the dataset directly using this command in your terminal:

```bash
curl -o compas_dataset.csv https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv
```

Or using wget:

```bash
wget -O compas_dataset.csv https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv
```

## Dataset Description

The COMPAS dataset contains information about defendants in Broward County, Florida, including:

- **Demographic Information**: race, sex, age
- **Criminal History**: number of prior offenses, juvenile offenses
- **COMPAS Scores**: decile risk scores (1-10) and risk categories (Low, Medium, High)
- **Outcomes**: whether the person was re-arrested within 2 years

### Key Columns

- `race`: Defendant's race (African-American, Caucasian, Hispanic, Asian, Native American, Other)
- `sex`: Defendant's gender (Male, Female)
- `age`: Defendant's age at time of assessment
- `age_cat`: Age category (Less than 25, 25-45, Greater than 45)
- `priors_count`: Number of prior offenses
- `juv_fel_count`: Number of juvenile felony offenses
- `juv_misd_count`: Number of juvenile misdemeanor offenses
- `decile_score`: COMPAS risk score (1-10, where 10 is highest risk)
- `score_text`: Risk category (Low, Medium, High)
- `two_year_recid`: Whether defendant was re-arrested within 2 years (1 = Yes, 0 = No)
- `is_recid`: Whether defendant was ever re-arrested
- `c_charge_degree`: Degree of current charge (F = Felony, M = Misdemeanor)
- `days_b_screening_arrest`: Days between screening and arrest

## Dataset Size

- **Original size**: ~11,000 records
- **After preprocessing**: ~6,000 records (following ProPublica methodology)

## Ethical Considerations

This dataset contains real criminal justice data. Please handle it responsibly:

- **Privacy**: The data has been de-identified, but still represents real individuals
- **Sensitivity**: Criminal justice data is inherently sensitive
- **Purpose**: Use only for educational purposes in this assignment
- **Respect**: Remember that these records represent real people's lives

## Data Quality Notes

The dataset contains some missing values and outliers. The preprocessing steps in the notebook follow ProPublica's methodology to filter the data appropriately:

1. Screen dates within 30 days of arrest
2. Exclude cases with missing recidivism information
3. Exclude 'Other' charge degrees
4. Exclude cases with missing COMPAS scores

## Citation

If you reference this dataset in any written work, please cite:

**ProPublica Investigation:**
- Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016). "Machine Bias: There's software used across the country to predict future criminals. And it's biased against blacks." ProPublica, May 23, 2016.
- URL: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

**Original Data Source:**
- Broward County Clerk's Office, Broward County Sheriff's Office

## Additional Resources

- **ProPublica Analysis Code**: https://github.com/propublica/compas-analysis
- **Academic Paper**: Dressel, J., & Farid, H. (2018). "The accuracy, fairness, and limits of predicting recidivism." Science advances, 4(1), eaao5580.
- **Northpointe Response**: http://www.equivant.com/response-to-propublica-demonstrating-accuracy-equity-and-predictive-parity/

## Support

If you have issues downloading or loading the dataset:

1. Check your internet connection
2. Verify the file path in your notebook/script
3. Ensure you have read permissions for this directory
4. Try the manual download option
5. Contact your instructor or TA

---

**Remember**: The goal of this assignment is to learn how to identify and mitigate bias in AI systems, not to make judgments about the individuals in this dataset.
