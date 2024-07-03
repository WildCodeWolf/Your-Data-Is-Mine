# Description

Feature importance analysis on credit card fraud dataset.

---

# Goal

Does the time column contribute significant information to the target column?
Does the amount column contribute significant information to the target column?
Which are the most informative columns among the `V<N>`s?
Can accuracy or f1 be increased by removing any of those from the models' training?

Model score on training data: 1.0
Model score on testing data: 0.9995201479348805

All features - Accuracy: 0.9995201479348805, F1 Score: 0.8452830188679246
Without 'Time' and 'Amount' - Accuracy: 0.9994967405170698, F1 Score: 0.8352490421455939
Least important features: ['V23', 'V24', 'V25', 'V27', 'V28']
Without least important features - Accuracy: 0.9995201479348805, F1 Score: 0.8452830188679246

---

# Owner

Nilgün
