# Description

Use Hyperparameter Tuning to improve scores on Random Forest classification
on network traffic dataset.

---

# Goal

Improvement of benchmark scores.

Original scores for *attack detection*:<br/>
```
(rf_is_attack_accuracy := accuracy_score(y_true_is_attack, rf_is_attack_pred)) = 0.9297330866465695
(rf_is_attack_fbeta := fbeta_score(y_true_is_attack, rf_is_attack_pred, beta=beta, average=None)) = array([0.99329947, 0.82578597])

              precision    recall  f1-score   support

       False       0.90      0.99      0.95     47913
        True       0.99      0.82      0.90     29378

    accuracy                           0.93     77291
   macro avg       0.95      0.91      0.92     77291
weighted avg       0.94      0.93      0.93     77291
```

Results for tuned *attack detection*:<br/>
```
-- Training Results --
Best Parameters:
	criterion:	entropy
	max_depth:	10
	n_estimators:	100
	n_jobs:	-1
	random_state:	404
Best Score:
	0.990874

-- Testing Results --
Accuracy    on Verification Data:	0.925606
Fbeta scroe on Verification Data:	0.925486

              precision    recall  f1-score   support

       False       0.90      0.99      0.94     47913
        True       0.99      0.81      0.89     29378

    accuracy                           0.93     77291
   macro avg       0.94      0.90      0.92     77291
weighted avg       0.93      0.93      0.92     77291
```

Original scores for *attack classification*:<br/>
```
(rf_attack_group_accuracy := accuracy_score(y_true_attack_group, rf_attack_group_pred)) = 0.9072775546327183
(rf_attack_group_fbeta := fbeta_score(y_true_attack_group, rf_attack_group_pred, beta=beta, average=None)) = array([0.96321101, 0.82095444, 0.50242443, 0.14018043])

              precision    recall  f1-score   support

           0       0.96      0.96      0.96     23747
           2       0.60      0.82      0.69      3041
           3       0.91      0.50      0.64      2533
           4       0.12      0.14      0.13        57

    accuracy                           0.91     29378
   macro avg       0.65      0.61      0.61     29378
weighted avg       0.92      0.91      0.91     29378
```

Results for *attack classification*:<br/>
```
-- Training Results --
Best Parameters:
	criterion:	gini
	max_depth:	20
	n_estimators:	20
	n_jobs:	-1
	random_state:	404
Best Score:
	0.844451

-- Testing Results --
Accuracy    on Verification Data:	0.906767
Fbeta scroe on Verification Data:	0.906661

              precision    recall  f1-score   support

           0       0.96      0.96      0.96     23747
           2       0.62      0.82      0.70      3041
           3       0.82      0.50      0.62      2533
           4       0.14      0.16      0.15        57

    accuracy                           0.91     29378
   macro avg       0.64      0.61      0.61     29378
weighted avg       0.91      0.91      0.91     29378
```

---

# Owner

Dustin
