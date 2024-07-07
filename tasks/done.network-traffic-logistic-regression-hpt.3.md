# Description

Hyperparameter Tuning for the Logistic Regression model on the network
traffic dataset.

---

# Goal

Improvement of the current score(s).

Original scores for *attack detection*:
```
/// NO DATA AVAILABLE ///
```

New scores for *attack detection*:
```
-- Training Results --
Best Parameters:
	C:	1.2000000000000002
	fit_intercept:	True
	max_iter:	10000
	n_jobs:	-1
	penalty:	l2
	random_state:	404
	tol:	0.0001
Best Score:
	0.986085

-- Testing Results --
Accuracy    on Verification Data:	0.905720
Fbeta scroe on Verification Data:	0.905563

              precision    recall  f1-score   support

       False       0.88      0.99      0.93     47913
        True       0.97      0.78      0.86     29378

    accuracy                           0.91     77291
   macro avg       0.92      0.88      0.90     77291
weighted avg       0.91      0.91      0.90     77291
```

Original scores for *attack classification*:
```
/// NO DATA AVAILABLE ///
```

New scores for *attack classification*:
```
-- Training Results --
Best Parameters:
	C:	0.8
	fit_intercept:	False
	max_iter:	10000
	n_jobs:	-1
	penalty:	l2
	random_state:	404
	tol:	0.0001
Best Score:
	0.823290

-- Testing Results --
Accuracy    on Verification Data:	0.843999
Fbeta scroe on Verification Data:	0.843201

              precision    recall  f1-score   support

           0       0.90      0.99      0.94     23747
           2       0.41      0.45      0.43      3041
           3       0.00      0.00      0.00      2533
           4       0.00      0.00      0.00        57

    accuracy                           0.84     29378
   macro avg       0.33      0.36      0.34     29378
weighted avg       0.77      0.84      0.81     29378
```

---

# Owner

Dustin
