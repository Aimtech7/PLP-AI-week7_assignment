# Instructor Guide: AI Ethics Assignment

## Assignment Overview

This comprehensive AI ethics assignment engages students with theoretical concepts, real-world case studies, and hands-on fairness auditing. It's designed for undergraduate or graduate courses in AI, computer science, data science, or ethics.

**Estimated Time**: 8-12 hours
**Difficulty Level**: Intermediate
**Prerequisites**: Basic Python programming, familiarity with machine learning concepts

---

## Learning Objectives

By completing this assignment, students will be able to:

1. Define and explain key AI ethics concepts (bias, fairness, transparency, accountability)
2. Analyze real-world case studies of algorithmic bias
3. Calculate and interpret quantitative fairness metrics
4. Use industry-standard tools (AIF360) for fairness auditing
5. Propose evidence-based bias mitigation strategies
6. Reflect critically on ethical responsibilities in AI development
7. Develop domain-specific ethical guidelines

---

## Assignment Structure

### Part 1: Theoretical Understanding (25 points, ~2 hours)

**Topics Covered:**
- Algorithmic bias definition and examples
- Transparency vs. explainability
- GDPR's impact on AI
- Ethical principles (justice, non-maleficence, autonomy, sustainability)

**Assessment Criteria:**
- Accuracy of definitions (40%)
- Quality of real-world examples (30%)
- Understanding of regulatory frameworks (20%)
- Clarity of writing (10%)

**Teaching Tips:**
- Provide supplemental readings on recent AI bias incidents
- Encourage students to find examples beyond those discussed in class
- Discuss the EU AI Act alongside GDPR for contemporary context

---

### Part 2: Case Study Analysis (30 points, ~3 hours)

**Case Studies:**

**Case 1: Amazon Hiring Tool (15 points)**
- Source of bias identification
- Technical/procedural fixes
- Fairness metrics selection

**Case 2: Facial Recognition in Policing (15 points)**
- Ethical risk analysis
- Policy framework development

**Assessment Criteria:**
- Depth of analysis (40%)
- Technical accuracy (30%)
- Practical feasibility of solutions (20%)
- Writing quality and organization (10%)

**Teaching Tips:**
- Share original news articles and company responses
- Facilitate class discussion on trade-offs between fairness and accuracy
- Invite guest speakers from industry or advocacy organizations
- Discuss recent facial recognition bans (e.g., San Francisco, Boston)

**Additional Resources for Students:**
- ProPublica's "Machine Bias" series
- Buolamwini & Gebru (2018) "Gender Shades" study
- Reuters' investigation into Amazon hiring tool
- ACLU reports on facial recognition

---

### Part 3: Practical Fairness Audit (30 points, ~4-5 hours)

**Technical Components:**
1. Data loading and preprocessing (5 points)
2. Fairness metrics calculation (10 points)
3. Visualization creation (5 points)
4. Bias mitigation application (5 points)
5. Written audit report (5 points)

**Assessment Criteria:**
- Code functionality and correctness (40%)
- Accurate metric interpretation (25%)
- Quality of visualizations (15%)
- Report clarity and insight (20%)

**Teaching Tips:**
- Conduct a lab session demonstrating AIF360 basics
- Provide debugging office hours
- Emphasize importance of understanding metrics, not just calculating them
- Discuss limitations of fairness metrics (impossibility theorem)

**Common Student Challenges:**
1. **AIF360 installation issues**: Provide conda environment file
2. **Understanding fairness metrics**: Create comparison table handout
3. **Interpreting results**: Require students to explain metrics in plain English
4. **Report writing**: Provide example audit reports from real audits

**Code Review Checklist:**
- [ ] Dataset loads correctly with appropriate filtering
- [ ] All fairness metrics calculated accurately
- [ ] Visualizations are clear and properly labeled
- [ ] Bias mitigation technique applied correctly
- [ ] Code is well-commented and organized

---

### Part 4: Ethical Reflection (15 points, ~1 hour)

**Requirements:**
- 300+ words
- Personal connection to AI ethics
- Specific practices student will adopt
- Future-oriented thinking

**Assessment Criteria:**
- Depth of reflection (40%)
- Personal insight and authenticity (30%)
- Connection to course concepts (20%)
- Writing quality (10%)

**Teaching Tips:**
- Share your own ethical challenges in research/practice
- Avoid penalizing students for honest reflections
- Encourage specificity over platitudes
- Consider making this section anonymous if students prefer

---

### Bonus Task: Healthcare Guidelines (10 bonus points, ~1-2 hours)

**Requirements:**
- One-page guideline document
- Domain-specific considerations
- Practical implementation details

**Assessment Criteria:**
- Comprehensiveness (40%)
- Specificity to healthcare domain (30%)
- Practicality (20%)
- Professional presentation (10%)

---

## Technical Setup

### Environment Setup

**Recommended Approach: Conda**

```bash
conda create -n ai-ethics python=3.9
conda activate ai-ethics
pip install -r requirements.txt
```

**Alternative: Virtual Environment**

```bash
python -m venv ai-ethics-env
source ai-ethics-env/bin/activate  # On Windows: ai-ethics-env\Scripts\activate
pip install -r requirements.txt
```

### Known Installation Issues

**Issue 1: AIF360 Dependencies**
- **Symptom**: Installation fails with compilation errors
- **Solution**: Use conda instead of pip, or install dependencies manually

**Issue 2: TensorFlow Version Conflicts**
- **Symptom**: Adversarial debiasing fails
- **Solution**: This is optional; students can skip in-processing mitigation

**Issue 3: Dataset Download Fails**
- **Symptom**: 404 error or connection timeout
- **Solution**: Provide local copy or alternative mirror

### Testing the Setup

Provide students with this test script:

```python
# test_setup.py
import sys

try:
    import numpy as np
    print("✓ NumPy installed")
except:
    print("✗ NumPy missing")

try:
    import pandas as pd
    print("✓ Pandas installed")
except:
    print("✗ Pandas missing")

try:
    import matplotlib.pyplot as plt
    print("✓ Matplotlib installed")
except:
    print("✗ Matplotlib missing")

try:
    from aif360.datasets import BinaryLabelDataset
    print("✓ AIF360 installed")
except:
    print("✗ AIF360 missing")

print("\nSetup test complete!")
```

---

## Grading Guidelines

### Detailed Rubric

**Part 1: Theoretical Understanding (25 points)**

| Criterion | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Needs Improvement (<70%) |
|-----------|-------------------|---------------|---------------------|----------------------|
| Definitions | Precise, nuanced definitions with academic rigor | Accurate definitions with minor gaps | Basic but correct definitions | Significant inaccuracies |
| Examples | Highly relevant, detailed real-world cases | Good examples with adequate detail | Generic or oversimplified examples | Incorrect or irrelevant examples |
| Regulatory Knowledge | Deep understanding of GDPR implications | Good grasp of main concepts | Surface-level understanding | Significant misconceptions |

**Part 2: Case Study Analysis (30 points)**

| Criterion | Excellent | Good | Satisfactory | Needs Improvement |
|-----------|-----------|------|--------------|-------------------|
| Problem Identification | Root causes clearly identified | Main issues identified | Surface issues only | Misses key problems |
| Solutions | Innovative, feasible, comprehensive | Practical and relevant | Basic but workable | Impractical or vague |
| Critical Thinking | Considers multiple perspectives and trade-offs | Good analysis with some depth | Limited analysis | Superficial thinking |

**Part 3: Practical Audit (30 points)**

| Criterion | Excellent | Good | Satisfactory | Needs Improvement |
|-----------|-----------|------|--------------|-------------------|
| Technical Execution | Code runs flawlessly, metrics correct | Minor issues, mostly correct | Significant bugs but core works | Code fails to run |
| Data Analysis | Insightful interpretation of results | Good understanding shown | Basic interpretation | Misinterprets results |
| Visualizations | Publication-quality, highly informative | Clear and appropriate | Adequate but basic | Confusing or incorrect |
| Report Quality | Professional, comprehensive, insightful | Well-written and complete | Meets minimum requirements | Incomplete or unclear |

**Part 4: Ethical Reflection (15 points)**

| Criterion | Excellent | Good | Satisfactory | Needs Improvement |
|-----------|-----------|------|--------------|-------------------|
| Depth | Profound personal insight and growth | Thoughtful reflection | Surface reflection | Minimal effort |
| Specificity | Concrete practices and examples | Some specific commitments | Vague statements | Only platitudes |
| Authenticity | Genuine personal voice | Mostly authentic | Somewhat generic | Clearly rushed |

---

## Common Student Questions & Answers

**Q: Can we work in groups?**
A: Parts 1-3 can be collaborative, but each student must submit their own Part 4 reflection. Document individual contributions.

**Q: What if the dataset won't download?**
A: Try the manual download method in data/README.md. If that fails, contact the instructor for a local copy.

**Q: How strict is the 300-word minimum for reports?**
A: It's a minimum. Quality matters more than quantity, but comprehensive reports typically need 400-600 words.

**Q: Can we use different fairness metrics?**
A: Yes! Feel free to explore additional metrics beyond those provided. Explain why you chose them.

**Q: What if bias mitigation makes accuracy worse?**
A: This is an important finding! Discuss this trade-off in your report. There's no expectation that mitigation must improve all metrics.

**Q: Can we analyze gender bias instead of racial bias?**
A: You must complete the racial bias analysis, but gender analysis is a great addition (and can be part of the bonus).

**Q: Is the bonus task required?**
A: No, it's optional extra credit. Complete it if you're interested in healthcare AI.

---

## Extension Ideas

For advanced students or extended assignments:

### Additional Analyses
1. **Intersectionality**: Examine bias for race + gender combinations
2. **Multiple Algorithms**: Compare COMPAS with student-trained models
3. **Alternative Definitions**: Implement fairness under different philosophical frameworks
4. **Temporal Analysis**: Study how bias changes over time in the dataset

### Alternative Datasets
- **Credit Default**: UCI Credit Card Default dataset
- **Hiring**: Synthetic resume dataset
- **Healthcare**: MIMIC-III (requires data use agreement)
- **Education**: College admission data

### Advanced Topics
- Implement custom fairness metrics
- Explore fairness-accuracy frontier (Pareto curves)
- Study impossibility of satisfying all fairness definitions
- Compare different mitigation techniques quantitatively

---

## Course Integration

### Module 1: Introduction to AI Ethics (Week 1-2)
- Assign Part 1 (Theoretical Understanding)
- Lecture on algorithmic bias
- Reading: O'Neil's "Weapons of Math Destruction" (selected chapters)

### Module 2: Case Studies in AI Bias (Week 3-4)
- Assign Part 2 (Case Study Analysis)
- Guest speaker from industry
- Discussion: Trade-offs in fairness

### Module 3: Quantitative Fairness (Week 5-7)
- Lab: Introduction to AIF360
- Assign Part 3 (Practical Audit)
- Workshop: Debugging session

### Module 4: Building Ethical AI (Week 8)
- Assign Part 4 (Ethical Reflection)
- Optional: Bonus task for interested students
- Final presentations of findings

---

## Assessment Timeline

**Recommended Schedule (8-week course):**

- **Week 3**: Part 1 due (theoretical foundations established)
- **Week 5**: Part 2 due (case study analysis skills developed)
- **Week 7**: Part 3 due (technical skills applied)
- **Week 8**: Part 4 due (reflection completed)
- **Week 8**: Bonus task due (optional)

**Accelerated Schedule (4-week intensive):**
- **Week 2**: Parts 1 & 2 due
- **Week 4**: Parts 3 & 4 due

---

## Resources for Instructors

### Recommended Textbooks
- Barocas, Hardt, Narayanan: "Fairness and Machine Learning" (free online)
- O'Neil: "Weapons of Math Destruction"
- Noble: "Algorithms of Oppression"
- Benjamin: "Race After Technology"

### Research Papers
- Buolamwini & Gebru (2018): "Gender Shades"
- Corbett-Davies & Goel (2018): "The Measure and Mismeasure of Fairness"
- Chouldechova (2017): "Fair prediction with disparate impact"
- Hardt et al. (2016): "Equality of Opportunity in Supervised Learning"

### Online Resources
- **AI Fairness 360**: http://aif360.mybluemix.net/
- **Fairlearn**: https://fairlearn.org/
- **What-If Tool**: https://pair-code.github.io/what-if-tool/
- **Google PAIR**: https://pair.withgoogle.com/

### Professional Organizations
- **ACM FAccT Conference**: Focus on fairness, accountability, transparency
- **AI Ethics Organizations**: Partnership on AI, AI Now Institute
- **IEEE Standards**: P7000 series on algorithmic bias

---

## Adapting for Different Audiences

### For Computer Science Students
- Emphasize technical implementation
- Require additional algorithm comparisons
- Add complexity to bias mitigation techniques

### For Social Science Students
- Reduce technical requirements
- Emphasize case study analysis and policy recommendations
- Allow qualitative analysis alongside quantitative

### For Professional Students (MBA, MPA)
- Focus on governance and organizational policies
- Add business case analysis
- Emphasize stakeholder management

### For Interdisciplinary Courses
- Form mixed teams with complementary skills
- Require both technical and policy deliverables
- Add presentation component

---

## Academic Integrity

### Permitted Collaboration
- Discussing concepts and approaches
- Sharing debugging strategies
- Reviewing each other's code for errors

### Not Permitted
- Copying code or written responses
- Sharing completed assignments
- Using unauthorized external help (e.g., homework services)

### AI Tool Policy (ChatGPT, etc.)
Recommended approach:
- Permit for brainstorming and debugging
- Require citation of AI assistance
- Prohibit for final written answers
- Focus assessment on analysis and interpretation (harder for AI to replicate)

---

## Continuous Improvement

### Gathering Student Feedback
- Mid-assignment check-in survey
- Post-submission reflection questions
- Anonymous feedback form

### Key Questions
1. Were the instructions clear?
2. Was the technical setup manageable?
3. What was most valuable for your learning?
4. What would you change about the assignment?
5. How much time did you actually spend?

### Iteration Ideas
- Update case studies annually with current events
- Adjust point distribution based on student performance
- Add more scaffolding for struggling students
- Create advanced track for experienced students

---

## Support Materials

Create these supplemental materials:

1. **Lecture Slides**: Cover key concepts before each part
2. **Video Tutorials**: Screen recordings of technical setup and AIF360 basics
3. **Example Solutions**: From previous semesters (anonymized)
4. **Office Hours**: Scheduled debugging sessions
5. **Discussion Forum**: Piazza or similar for peer support

---

## Contact & Questions

For questions about this assignment or suggestions for improvement:

- Create issues on the assignment repository
- Share adaptations with the community
- Contribute improvements via pull requests

---

## License

This assignment is released under MIT License for educational use. You are free to:
- Use in your courses
- Modify for your context
- Share with colleagues

Please attribute the original source and share improvements with the community.

---

**Good luck with the course! Building ethical AI starts with education.**
