# Description

Feature importance analysis on credit card fraud dataset.

---

# Goal

Does the time column contribute significant information to the target column?
Does the amount column contribute significant information to the target column?
Which are the most informative columns among the `V<N>`s?
Can accuracy or f1 be increased by removing any of those from the models' training?

Model score on training data: 1.0 <br/>
Model score on testing data: 0.9995318516437859 <br/>
<br/>
All features - Accuracy: 0.9995201479348805, F1 Score: 0.8452830188679246 <br/>
Without 'Time' and 'Amount' - Accuracy: 0.9994967405170698, F1 Score: 0.8352490421455939 <br/>
Least important features: ['V23', 'V24', 'V25', 'V27', 'V28'] <br/>
Without least important features - Accuracy: 0.9995201479348805, F1 Score: 0.8452830188679246 <br/>
<br/>
All features - Accuracy: 0.9995318516437859, F-beta Score (beta=10): 0.7850442240686143 <br/>
Without 'Time' and 'Amount' - Accuracy: 0.9995318516437859, F-beta Score (beta=10): 0.7783809140865836 <br/>
Least important features: ['V23', 'V25', 'V22', 'V28', 'V15'] <br/>
Without least important features - Accuracy: 0.9995318516437859, F-beta Score (beta=10): 0.7850442240686143 <br/>
---

# Owner

Nilgün
