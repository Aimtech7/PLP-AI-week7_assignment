# AI Ethics Assignment: Designing Responsible and Fair AI Systems

## 📚 Project Overview

This comprehensive assignment explores the fundamental principles of ethical AI development, algorithmic fairness, and responsible deployment of machine learning systems. Students will engage with theoretical concepts, analyze real-world case studies, and conduct hands-on fairness audits using industry-standard tools.

## 🎯 Learning Objectives

- Understand key concepts in AI ethics: bias, fairness, transparency, and accountability
- Analyze real-world ethical failures in AI systems
- Conduct quantitative fairness audits using Python and AIF360
- Develop ethical guidelines for AI deployment in sensitive domains
- Reflect on personal responsibility in AI development

## 📁 Project Structure

```
ai-ethics-assignment/
├── docs/
│   ├── AI_Ethics_Assignment_Main.pdf
│   └── Healthcare_Ethical_AI_Guidelines.pdf
├── notebooks/
│   └── Fairness_Audit_COMPAS.ipynb
├── src/
│   └── fairness_audit.py
├── data/
│   └── compas_dataset.csv
└── README.md
```

## 🔧 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- pip package manager

### Installation

1. Clone or download this project directory

2. Install required Python packages:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn aif360 jupyter
```

3. Download the COMPAS dataset:
   - Visit: https://github.com/propublica/compas-analysis
   - Download `compas-scores-two-years.csv`
   - Place it in the `data/` folder and rename to `compas_dataset.csv`
   - Or use the provided script in the notebook to download automatically

## 🚀 Running the Assignment Components

### Part 1 & 2: Written Responses

Open and review `docs/AI_Ethics_Assignment_Main.pdf` for theoretical questions and case study analyses. Complete your responses in the provided template.

### Part 3: Fairness Audit (Practical Component)

#### Option A: Using Jupyter Notebook (Recommended for beginners)

```bash
cd notebooks
jupyter notebook Fairness_Audit_COMPAS.ipynb
```

Follow the step-by-step instructions in the notebook to:
- Load and explore the COMPAS dataset
- Calculate fairness metrics
- Visualize bias across demographic groups
- Apply bias mitigation techniques
- Write your audit report

#### Option B: Using Python Script (For advanced users)

```bash
cd src
python fairness_audit.py --input ../data/compas_dataset.csv
```

This will generate:
- Fairness metrics report (console output)
- Visualization charts (saved to `outputs/` folder)

### Part 4: Ethical Reflection

Complete the reflection section in `docs/AI_Ethics_Assignment_Main.pdf` based on your experiences with the practical audit.

### Bonus Task: Healthcare Guidelines

Review and customize `docs/Healthcare_Ethical_AI_Guidelines.pdf` to develop domain-specific ethical guidelines.

## 📊 Key Concepts Covered

### Fairness Metrics

- **Disparate Impact**: Ratio of favorable outcomes between groups
- **Equal Opportunity**: Equal true positive rates across groups
- **Equalized Odds**: Equal TPR and FPR across groups
- **Demographic Parity**: Equal prediction rates across groups

### Bias Mitigation Techniques

- **Pre-processing**: Reweighing, sampling, data augmentation
- **In-processing**: Adversarial debiasing, prejudice remover
- **Post-processing**: Threshold optimization, calibration

## 🤝 Group Work Guidelines

If completing this as a group assignment:

1. **Part 1 & 2**: Collaborate on written responses, but each member should contribute unique perspectives
2. **Part 3**: Work together on the code, but each member should run the notebook independently
3. **Part 4**: Individual reflections required
4. **Bonus Task**: Can be completed collaboratively with clear role divisions

Document individual contributions in your submission.

## 📚 Recommended Resources

### Books & Papers
- "Weapons of Math Destruction" by Cathy O'Neil
- "Fairness and Machine Learning" by Barocas, Hardt, and Narayanan
- "The Alignment Problem" by Brian Christian

### Online Resources
- ProPublica COMPAS Analysis: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
- Google's Responsible AI Practices: https://ai.google/responsibilities/responsible-ai-practices/
- Microsoft's AI Fairness Checklist: https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/
- IBM AI Fairness 360: http://aif360.mybluemix.net/

### Tools & Libraries
- AIF360: https://aif360.readthedocs.io/
- Fairlearn: https://fairlearn.org/
- What-If Tool: https://pair-code.github.io/what-if-tool/

## ⚠️ Important Notes

- **Academic Integrity**: This assignment must reflect your own understanding and analysis
- **Data Privacy**: The COMPAS dataset contains real criminal justice data. Handle responsibly
- **Ethical Considerations**: Consider the implications of your findings throughout the assignment
- **Deadlines**: Check your course syllabus for submission deadlines

## 🆘 Troubleshooting

### Common Issues

**AIF360 Installation Errors:**
```bash
# Try installing with conda instead:
conda install -c conda-forge aif360
```

**Dataset Loading Issues:**
- Ensure the CSV file is in the correct location
- Check file permissions
- Verify the file is not corrupted

**Jupyter Kernel Issues:**
```bash
python -m ipykernel install --user --name=ai-ethics
```

## 📧 Support

For technical issues with the code or notebooks, consult:
- AIF360 documentation
- Stack Overflow (tag: fairness-ml)
- Course instructor or TA

## 📝 Submission Checklist

Before submitting, ensure you have:

- [ ] Completed all written responses in Part 1 & 2
- [ ] Conducted the fairness audit (Part 3)
- [ ] Generated all required visualizations
- [ ] Written the audit report (300 words)
- [ ] Completed ethical reflection (Part 4)
- [ ] (Optional) Completed bonus healthcare guidelines
- [ ] Included all code files and notebooks
- [ ] Added any additional analysis or insights

## 📄 License

This educational project is provided for academic use. The COMPAS dataset is used for educational purposes only. Please cite original sources when referencing this work.

---

**Good luck with your assignment! Remember: Building ethical AI is not just about technical skills—it's about cultivating moral reasoning and social responsibility in technology development.**
