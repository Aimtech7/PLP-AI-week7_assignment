# Quick Start Guide

## For Students: Getting Started in 5 Minutes

### Step 1: Install Dependencies (2 minutes)

```bash
# Navigate to project directory
cd ai-ethics-assignment

# Install required packages
pip install -r requirements.txt
```

### Step 2: Start with Written Work (Parts 1, 2, 4)

Open `docs/AI_Ethics_Assignment_Main.md` and complete:
- Part 1: Theoretical questions (25 points)
- Part 2: Case study analysis (30 points)
- Part 4: Ethical reflection (15 points)

### Step 3: Complete Practical Audit (Part 3)

```bash
# Navigate to notebooks directory
cd notebooks

# Launch Jupyter
jupyter notebook Fairness_Audit_COMPAS.ipynb
```

Follow the notebook step-by-step. It will:
- Download the COMPAS dataset automatically
- Guide you through fairness analysis
- Generate visualizations
- Help you write your audit report

### Step 4: (Optional) Bonus Task

Open `docs/Healthcare_Ethical_AI_Guidelines.md` and develop domain-specific guidelines for 10 bonus points.

### Step 5: Submit

Check the submission checklist in the main README before submitting!

---

## For Instructors: Deploying in 10 Minutes

### Step 1: Review Materials (3 minutes)

- Read `INSTRUCTOR_GUIDE.md` for comprehensive teaching details
- Review `docs/AI_Ethics_Assignment_Main.md` to see student deliverables
- Check `PROJECT_SUMMARY.md` for complete overview

### Step 2: Customize (3 minutes)

Edit `docs/AI_Ethics_Assignment_Main.md`:
- Add your course name and semester
- Set due dates
- Adjust point values if needed
- Add any course-specific requirements

### Step 3: Set Up Student Support (2 minutes)

- Schedule office hours for technical help
- Create discussion forum (Piazza, Discord, etc.)
- Share troubleshooting guides from README

### Step 4: Test Technical Setup (2 minutes)

```bash
# Verify environment
pip install -r requirements.txt

# Test notebook
jupyter notebook notebooks/Fairness_Audit_COMPAS.ipynb

# Test CLI tool
python src/fairness_audit.py --help
```

### Step 5: Deploy

- Share the entire `ai-ethics-assignment/` directory with students
- Announce assignment with timeline from INSTRUCTOR_GUIDE.md
- Monitor student questions and update FAQ

---

## Troubleshooting

### Common Issue 1: AIF360 Won't Install

**Solution:**
```bash
# Try conda instead
conda install -c conda-forge aif360
```

### Common Issue 2: Dataset Won't Download

**Solution:**
The notebook includes automatic download. If it fails:
```bash
cd data
curl -o compas_dataset.csv https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv
```

### Common Issue 3: Jupyter Kernel Issues

**Solution:**
```bash
python -m ipykernel install --user --name=ai-ethics
```

---

## Need More Help?

- **Students**: See full README.md and notebook instructions
- **Instructors**: See INSTRUCTOR_GUIDE.md
- **Technical Issues**: Check data/README.md

---

**Ready to build responsible AI systems!** 🚀
