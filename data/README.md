# Credit Card Fraud detection Dataset

## Source

[Kaggle Link](https://www.kaggle.com/code/samkirkiles/credit-card-fraud/data)

## Preprocessing

The dataset comes as a preprocessed .csv file and needs no further
preprocessing before being loaded into a data frame.

# Network Traffic/ Network Intrusion Detection Dataset

## Sources

[Task Description](./KDD-CUP-99%20Task%20Description.pdf)<br/>
Origin: http://kdd.ics.uci.edu/databases/kddcup99/task.html

[Column Names](./kddcup.names.dat)<br/>
Origin: http://kdd.ics.uci.edu/databases/kddcup99/kddcup.names

[Training Attack Types](./Training%20Attack%20Types.pdf)<br/>
Origin: http://kdd.ics.uci.edu/databases/kddcup99/training_attack_types

[Training Dataset](./kddcup.csv)<br/>
Origin: http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz

[Testing Dataset](./corrected.csv)<br/>
Origin: http://kdd.ics.uci.edu/databases/kddcup99/corrected.gz


## Preprocessing

The training and testing datasets can be downloaded in `.gz` format.
To unpack them (on macOS), we used
```sh
network-traffic % gunzip corrected.gz
network-traffic % gunzip kddcup.data.gz
```
Then, we made copies to turn them into `csv` format and applied a regular
expression to remove the trailing period from each line.  (Each line of the
original data files closes with a period character (`.`).)
```sh
network-traffic % cp corrected corrected.csv
network-traffic % sed -i '' -e 's/\.$//g' corrected.csv
network-traffic % cp kddcup.data kddcup.data.csv
network-traffic % sed -i '' -e 's/\.$//g' kddcup.data.csv
```