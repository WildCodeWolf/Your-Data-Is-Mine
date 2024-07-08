# Description

Feature importance analysis on network traffic dataset.

---

# Goal

Which are the most informative columns to the target value?
Does the time column contribute significant information to the target column?
Can accuracy or fbeta be increased by removing any of the less
informative columns from the models' training?

Attack Detection:<br/>
Model score on training data: 0.9999916278446723<br/>
Model score on testing data: 0.9266796910377664<br/>

Impotant Features List in Notebook!<br/>
All features - Accuracy: 0.9266796910377664, F-beta Score (beta=10): 0.9054951021766391<br/>
Without least important features - Accuracy: 0.9262527331772133, F-beta Score (beta=10): 0.9049860816660242<br/>

Attack Class Prediction:<br/>
Model score on training data: 1.0<br/>
Model score on testing data: 0.9617290499540697<br/>

Impotant Features List in Notebook!<br/>
All features - Accuracy: 0.9617290499540697<br/>
Without least important features - Accuracy: 0.9657398662198704<br/>

---

# Owner
Nilgün
