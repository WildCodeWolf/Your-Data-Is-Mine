# Description

Apply Random Forest classification on network traffic dataset.

---

# Goal

Get initial scores as benchmark for upcoming hyperparameter tuning.

overall accuracy: 0.617083

Looking into individual labels:

| attack type     | accuracy | $F_\beta$ | $F_\beta^\mathrm{total}$ |
| --------------- | -------- | --------- | ------------------------ |
| normal          | 0.920754 | 0.993075  | 0.993298                 |
| snmpgetattack   | 0.997645 | 0.000000  | 0.000000                 |
| named           | 0.999767 | 0.000000  | 0.000000                 |
| xlock           | 0.999884 | 0.000000  | 0.000000                 |
| smurf           | 0.755030 | 0.000000  | 0.000000                 |
| ipsweep         | 0.985897 | 0.006145  | 0.006147                 |
| multihop        | 0.999767 | 0.000000  | 0.000000                 |
| xsnoop          | 0.999237 | 0.000000  | 0.000000                 |
| sendmail        | 0.999806 | 0.000000  | 0.000000                 |
| guess_passwd    | 0.981046 | 0.000000  | 0.000000                 |
| saint           | 0.993841 | 0.118668  | 0.118645                 |
| buffer_overflow | 0.999715 | 0.000000  | 0.000000                 |
| portsweep       | 0.997749 | 0.000000  | 0.000000                 |
| pod             | 0.997723 | 0.000000  | 0.000000                 |
| apache2         | 0.989727 | 0.000000  | 0.000000                 |
| phf             | 0.987088 | 0.000000  | 0.000000                 |
| udpstorm        | 0.999974 | 0.000000  | 0.000000                 |
| warezmaster     | 0.986273 | 0.000000  | 0.000000                 |
| perl            | 0.999974 | 0.000000  | 0.000000                 |
| satan           | 0.988873 | 0.000000  | 0.000000                 |
| xterm           | 0.999470 | 0.227136  | 0.076573                 |
| mscan           | 0.986428 | 0.000000  | 0.000000                 |
| processtable    | 0.990374 | 0.000000  | 0.000000                 |
| ps              | 0.999793 | 0.000000  | 0.000000                 |
| nmap            | 0.998965 | 0.000000  | 0.000000                 |
| rootkit         | 0.999832 | 0.000000  | 0.000000                 |
| neptune         | 0.736942 | 0.000000  | 0.000000                 |
| loadmodule      | 0.999974 | 0.000000  | 0.000000                 |
| imap            | 0.999987 | 0.000000  | 0.000000                 |
| back            | 0.995006 | 0.000000  | 0.000000                 |
| httptunnel      | 0.998124 | 0.000000  | 0.000000                 |
| worm            | 0.999974 | 0.000000  | 0.000000                 |
| mailbomb        | 0.996015 | 0.000000  | 0.000000                 |
| ftp_write       | 0.999961 | 0.000000  | 0.000000                 |
| teardrop        | 0.999845 | 0.000000  | 0.000000                 |
| land            | 0.999884 | 0.000000  | 0.000000                 |
| sqlattack       | 0.999974 | 0.000000  | 0.000000                 |
| snmpguess       | 0.995355 | 0.000000  | 0.000000                 |

($\beta = 10$)

($F_\beta^\mathrm{total}$ is obtained by considering the target labels
in a non-binary scenario.)

---

# Owner

Dustin
