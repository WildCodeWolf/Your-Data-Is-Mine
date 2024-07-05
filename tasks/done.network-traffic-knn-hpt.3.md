# Description

Hyperparameter Tuning for the KNN model on the network
traffic dataset.

---

# Goal

Improvement of the current score(s).

Original scores for *attack detection*:
```
Accuracy: 0.9361503926718505, F-beta Score: 0.8408800248692995
              precision    recall  f1-score   support

           0       0.91      1.00      0.95     47913
           1       0.99      0.84      0.91     29378

    accuracy                           0.94     77291
   macro avg       0.95      0.92      0.93     77291
weighted avg       0.94      0.94      0.93     77291
```

Tuned scores for *attack detection:*
```
-- Training Results --
Best Parameters:
	n_jobs:	-1
	n_neighbors:	20
	weights:	distance
Best Score:
	0.996397

-- Testing Results --
Accuracy    on Verification Data:	0.926628
Fbeta scroe on Verification Data:	0.926530

              precision    recall  f1-score   support

       False       0.90      0.99      0.94     47913
        True       0.98      0.82      0.90     29378

    accuracy                           0.93     77291
   macro avg       0.94      0.91      0.92     77291
weighted avg       0.93      0.93      0.93     77291
```

Original scores for *attack classification*:
```
/// MISSING DATA ///
```

Tuned scores for *attack classification*:
```
-- Training Results --
Best Parameters:
	n_jobs:	-1
	n_neighbors:	100
	weights:	uniform
Best Score:
	0.977412

-- Testing Results --
Accuracy    on Verification Data:	0.854245
Fbeta scroe on Verification Data:	0.853874

              precision    recall  f1-score   support

           0       0.94      0.95      0.95     23747
           2       0.42      0.67      0.52      3041
           3       0.90      0.18      0.30      2533
           4       0.00      0.00      0.00        57

    accuracy                           0.85     29378
   macro avg       0.57      0.45      0.44     29378
weighted avg       0.88      0.85      0.84     29378
```

---

# Owner

Dustin
