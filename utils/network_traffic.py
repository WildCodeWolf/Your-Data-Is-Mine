"""This file contains auxiliaries for handling the network traffic dataset."""

import pandas as pd


class File:
    """Contains the file names for all csv files for the credit card dataset."""

    correlations_attack_identification_label = 'data/network-traffic/correlations_id_l.csv'
    """The file path to the correlation coefficients for the attack identification column for the label encoded training data."""

    correlations_attack_identification_label_scaled = 'data/network-traffic/correlations_id_ls.csv'
    """The file path to the correlation coefficients for the attack identification column for the scaled and label encoded training data."""

    correlations_attack_identification_1hot = 'data/network-traffic/correlations_id_1h.csv'
    """The file path to the correlation coefficients for the attack identification column for the one-hot encoded training data."""

    correlations_attack_identification_1hot_scaled = 'data/network-traffic/correlations_id_1hs.csv'
    """The file path to the correlation coefficients for the attack identification column for the scaled and one-hot encoded training data."""

    correlations_attack_classification_label = 'data/network-traffic/correlations_cl_l.csv'
    """The file path to the correlation coefficients for the attack classification column for the label encoded training data."""

    correlations_attack_classification_label_scaled = 'data/network-traffic/correlations_cl_ls.csv'
    """The file path to the correlation coefficients for the attack classification column for the scaled and label encoded training data."""

    correlations_attack_classification_1hot_dos = 'data/network-traffic/correlations_cl_1h_dos.csv'
    """The file path to the correlation coefficients for the attack classification column for the one-hot encoded DOS target training data."""

    correlations_attack_classification_1hot_dos_scaled = 'data/network-traffic/correlations_cl_1hs_dos.csv'
    """The file path to the correlation coefficients for the attack classification column for the scaled and one-hot encoded DOS target training data."""

    correlations_attack_classification_1hot_probe = 'data/network-traffic/correlations_cl_1h_probe.csv'
    """The file path to the correlation coefficients for the attack classification column for the one-hot encoded Probe target training data."""

    correlations_attack_classification_1hot_probe_scaled = 'data/network-traffic/correlations_cl_1hs_probe.csv'
    """The file path to the correlation coefficients for the attack classification column for the scaled and one-hot encoded Probe target training data."""

    correlations_attack_classification_1hot_r2l = 'data/network-traffic/correlations_cl_1h_r2l.csv'
    """The file path to the correlation coefficients for the attack classification column for the one-hot encoded R2L target training data."""

    correlations_attack_classification_1hot_r2l_scaled = 'data/network-traffic/correlations_cl_1hs_r2l.csv'
    """The file path to the correlation coefficients for the attack classification column for the scaled and one-hot encoded R2L target training data."""

    correlations_attack_classification_1hot_u2r = 'data/network-traffic/correlations_cl_1h_u2r.csv'
    """The file path to the correlation coefficients for the attack classification column for the one-hot encoded U2R target training data."""

    correlations_attack_classification_1hot_u2r_scaled = 'data/network-traffic/correlations_cl_1hs_u2r.csv'
    """The file path to the correlation coefficients for the attack classification column for the scaled and one-hot encoded U2R target training data."""

    original_training = 'data/network-traffic/kddcup.data.csv'
    """The file path to the original network traffic dataset."""

    original_verification = 'data/network-traffic/corrected.csv'
    """The file path to the original network traffic verification dataset."""

    training_attack_identification = 'data/network-traffic/training_id.csv'
    """The file path to the attack identification training data frame."""

    training_attack_identification_1hot = 'data/network-traffic/training_id_1h.csv'
    """The file path to the one-hot encoded attack identification training data frame."""

    training_attack_identification_1hot_scaled = 'data/network-traffic/training_id_1hs.csv'
    """The file path to the scaled and one-hot encoded attack identification training data frame."""

    training_attack_identification_label = 'data/network-traffic/training_id_l.csv'
    """The file path to the label encoded attack identification training data frame."""

    training_attack_identification_label_scaled = 'data/network-traffic/training_id_ls.csv'
    """The file path to the scaled and label encoded attack identification training data frame."""

    training_attack_identification_scaled = 'data/network-traffic/training_id_s.csv'
    """The file path to the scaled attack identification training data frame."""

    training_attack_classification = 'data/network-traffic/training_cl.csv'
    """The file path to the attack classification training data frame."""

    training_attack_classification_1hot = 'data/network-traffic/training_cl_1h.csv'
    """The file path to the one-hot encoded attack classification training data frame."""

    training_attack_classification_1hot_scaled = 'data/network-traffic/training_cl_1hs.csv'
    """The file path to the scaled and one-hot encoded attack classification training data frame."""

    training_attack_classification_label = 'data/network-traffic/training_cl_l.csv'
    """The file path to the label encoded attack classification training data frame."""

    training_attack_classification_label_scaled = 'data/network-traffic/training_cl_ls.csv'
    """The file path to the scaled and label encoded attack classification training data frame."""

    training_attack_classification_scaled = 'data/network-traffic/training_cl_s.csv'
    """The file path to the scaled attack classification training data frame."""

    verification_attack_identification = 'data/network-traffic/verification_id.csv'
    """The file path to the attack identification verification data frame."""

    verification_attack_identification_1hot = 'data/network-traffic/verification_id_1h.csv'
    """The file path to the one-hot encoded attack identification verification data frame."""

    verification_attack_identification_1hot_scaled = 'data/network-traffic/verification_id_1hs.csv'
    """The file path to the scaled and one-hot encoded attack identification verification data frame."""

    verification_attack_identification_label = 'data/network-traffic/verification_id_l.csv'
    """The file path to the label encoded attack identification verification data frame."""

    verification_attack_identification_label_scaled = 'data/network-traffic/verification_id_ls.csv'
    """The file path to the scaled and label encoded attack identification verification data frame."""

    verification_attack_identification_scaled = 'data/network-traffic/verification_id_s.csv'
    """The file path to the scaled attack identification verification data frame."""

    verification_attack_classification = 'data/network-traffic/verification_cl.csv'
    """The file path to the attack classification verification data frame."""

    verification_attack_classification_1hot = 'data/network-traffic/verification_cl_1h.csv'
    """The file path to the one-hot encoded attack classification verification data frame."""

    verification_attack_classification_1hot_scaled = 'data/network-traffic/verification_cl_1hs.csv'
    """The file path to the scaled and one-hot encoded attack classification verification data frame."""

    verification_attack_classification_label = 'data/network-traffic/verification_cl_l.csv'
    """The file path to the label encoded attack classification verification data frame."""

    verification_attack_classification_label_scaled = 'data/network-traffic/verification_cl_ls.csv'
    """The file path to the scaled and label encoded attack classification verification data frame."""

    verification_attack_classification_scaled = 'data/network-traffic/verification_cl_s.csv'
    """The file path to the scaled attack classification verification data frame."""

    @staticmethod
    def load(file):
        """Return the selected file as a data frame or series.
        
        Examples
        --------

            >>> data = File.load(File.training)
            >>> data.head() # prints the first five rows
        """
        return pd.read_csv(file, index_col=None)


class Col:
    """This class contains auxiliary fields that help dealing and displaying column names."""
    _all = [
        'duration',
        'protocol_type',
        'service',
        'flag',
        'src_bytes',
        'dst_bytes',
        'land',
        'wrong_fragment',
        'urgent',
        'hot',
        'num_failed_logins',
        'logged_in',
        'num_compromised',
        'root_shell',
        'su_attempted',
        'num_root',
        'num_file_creations',
        'num_shells',
        'num_access_files',
        'num_outbound_cmds',
        'is_host_login',
        'is_guest_login',
        'count',
        'srv_count',
        'serror_rate',
        'srv_serror_rate',
        'rerror_rate',
        'srv_rerror_rate',
        'same_srv_rate',
        'diff_srv_rate',
        'srv_diff_host_rate',
        'dst_host_count',
        'dst_host_srv_count',
        'dst_host_same_srv_rate',
        'dst_host_diff_srv_rate',
        'dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate',
        'dst_host_serror_rate',
        'dst_host_srv_serror_rate',
        'dst_host_rerror_rate',
        'dst_host_srv_rerror_rate',
        'target_type',
        'target_group',
        'is_attack',
    ]
    """The original column names (in order)."""

    _all_pretty = [
        'Duration (s)',
        'Protocol Type',
        'Service',
        'Flag',
        '#Bytes from source to destination',
        '#Bytes from destination to source',
        'Same host/ port? (0 - No, 1 - Yes)',
        '#Wrong Fragments',
        '#Urgent packets',
        '#Hot indicators',
        '#Failed login attempts',
        'Logged in? (0 - No, 1 - Yes)',
        '#Compromised Conditions',
        'Is root shell obtained? (0 - No, 1 - Yes)',
        'Is `su` command attempted? (0 - No, 1 - Yes)',
        '#Root accesses',
        '#File creation operations',
        '#Shell prompts',
        '#Operations on access control files',
        '#Outbound commands in ftp session',
        'Login belongs to host list? (0 - No, 1 - Yes)',
        'Login belongs to guest list? (0 - No, 1 - Yes)',
        '#Connections to same host in past 2s',
        '#Connections to same host and service in past 2s',
        r'% of same-host connections with `SYN` errors',
        r'% of same-service connections with `SYN` errors',
        r'% of same-host connections with `REJ` errors',
        r'% of same-service connections with `REJ` errors',
        r'% of same-host connections to the same service',
        r'% of same-host connections to different services',
        r'% of same-service connections to different hosts',
        '#Connections to same host from destination in past 2s',
        '#Connections to same host and service from destination in past 2s',
        r'% of same-host connections from destination to the same service',
        r'% of same-host connections from destination to different services',
        r'% of same-host connections from destination to the same service and port',
        r'% of same-service connections from destination to different hosts',
        r'% of same-host connections from destination with `SYN` errors',
        r'% of same-service connections from destination with `SYN` errors',
        r'% of same-host connections from destination with `REJ` errors',
        r'% of same-service connections from destination with `REJ` errors',
        'Target type',
        'Target group',
        'Is attack?',
    ]
    """The column names (in order)."""

    target_type = _all_pretty[-3]
    """The target type column."""
    target_classification = _all_pretty[-2]
    """The target classification column."""
    target_identification = _all_pretty[-1]
    """The target identification column."""

    target_dos = target_classification + '_dos'
    """The one-hot encoded DOS target column."""
    target_probe = target_classification + '_probe'
    """The one-hot encoded Probe target column."""
    target_r2l = target_classification + '_r2l'
    """The one-hot encoded R2L target column."""
    target_u2r = target_classification + '_u2r'
    """The one-hot encoded U2R target column."""

    @staticmethod
    def top(n, target_identification=True, correlations=True, label_encoded=True, one_hot_target='dos'):
        """Return the top `n` features in terms of absolute correlation coefficient.

        Parameters
        ----------
        n : int
            Number of features to return.
        target_identification : bool
            If `True`, retrieve a feature ranking for the attack detection target.
            If `False`, do so for a ranking for the attack classification target.
        correlations : bool
            If `True`, use correlation coefficients. If `False`, use data from
            feature importance analysis instead.
        label_encoded : bool
            If `True`, retrieve data from a ranking based on label encoded data.
            If `False`, do so on a ranking based on one-hot encoded data.
        one_hot_target : `{'dos', 'probe', 'r2l', 'u2r'}`, default: `'dos'`
            If `label_encoded=False`, then this value is used to pick the correlation
            matching the desired target column.  Has no effect for other types of
            encodings.
        
        Returns
        -------
        pandas.DataFrame :
            A data frame with features and their absolute correlation coefficients with
            the target column.

        See Also
        --------
        Col.above(threshold, target_identification=True, correlations=True, label_encoded=True, one_hot_target='dos')
        """
        match target_identification, correlations, label_encoded:
            case False, False, False:
                file = ''
            case False, False, True:
                file = ''
            case False, True, False:
                match one_hot_target.lower():
                    case 'dos':
                        file = File.correlations_attack_classification_1hot_dos
                    case 'probe':
                        file = File.correlations_attack_classification_1hot_probe
                    case 'r2l':
                        file = File.correlations_attack_classification_1hot_r2l
                    case 'u2r':
                        file = File.correlations_attack_classification_1hot_u2r
            case False, True, True:
                file = File.correlations_attack_classification_label
            case True, False, False:
                file = ''
            case True, False, True:
                file = ''
            case True, True, False:
                file = File.correlations_attack_identification_1hot
            case True, True, True:
                file = File.correlations_attack_identification_label
        ranking = pd.read_csv(file, index_col=None)
        return ranking[:n]
    
    @staticmethod
    def above(threshold, target_identification=True, correlations=True, label_encoded=True, one_hot_target='dos'):
        """Return all features with an absolute correlation coefficient above
        the given `threshold`.

        Parameters
        ----------
        threshold : float
            Lower limit of the correlation coeffients to be returned.
        target_identification : bool
            If `True`, retrieve a feature ranking for the attack detection target.
            If `False`, do so for a ranking for the attack classification target.
        correlations : bool
            If `True`, use correlation coefficients. If `False`, use data from
            feature importance analysis instead.
        label_encoded : bool
            If `True`, retrieve data from a ranking based on label encoded data.
            If `False`, do so on a ranking based on one-hot encoded data.
        one_hot_target : `{'dos', 'probe', 'r2l', 'u2r'}`, default: `'dos'`
            If `label_encoded=False`, then this value is used to pick the correlation
            matching the desired target column.  Has no effect for other types of
            encodings.
        
        Returns
        -------
        pandas.DataFrame :
            A data frame with features and their absolute correlation coefficients with
            the target column.

        See Also
        --------
        Col.top(n, target_identification=True, correlations=True, label_encoded=True, one_hot_target='dos')
        """
        match target_identification, correlations, label_encoded:
            case False, False, False:
                file = ''
            case False, False, True:
                file = ''
            case False, True, False:
                match one_hot_target.lower():
                    case 'dos':
                        file = File.correlations_attack_classification_1hot_dos
                    case 'probe':
                        file = File.correlations_attack_classification_1hot_probe
                    case 'r2l':
                        file = File.correlations_attack_classification_1hot_r2l
                    case 'u2r':
                        file = File.correlations_attack_classification_1hot_u2r
            case False, True, True:
                file = File.correlations_attack_classification_label
            case True, False, False:
                file = ''
            case True, False, True:
                file = ''
            case True, True, False:
                file = File.correlations_attack_identification_1hot
            case True, True, True:
                file = File.correlations_attack_identification_label
        ranking = pd.read_csv(file, index_col=None)
        return ranking[ranking['Coefficient'] >= threshold]

if __name__ == '__main__':
    print('This script is not meant to be run like this!')
