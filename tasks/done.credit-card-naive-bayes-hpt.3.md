# Description

Hyperparameter Tuning for the Naive Bayes model on the credit card
dataset.

---

# Goal

Improvement of the current score(s).<br/>
un-boosted accuracy:    0.976848<br/>
un-boosted f1 score:    0.108567<br/>

Switched to $F_\beta$ Score ($\beta = 10$).<br/>
Original $F_\beta$ score:  0.746127<br/>
Best     $F_\beta$ score:  0.783534<br/>
Best            accuracy:  0.985960

**NOTE** NB is happy to produce a lot of *false positives* on this
dataset! (We are talking a range from 3,000 to over 5,000, whereas
the entire dataset contains only 492 positive cases altogether!)

---

# Owner

Dustin
