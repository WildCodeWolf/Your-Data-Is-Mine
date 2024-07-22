"""This file contains auxiliaries for handling the network traffic dataset."""

import pandas as pd


class File:
    """Contains the file names for all csv files for the credit card dataset."""

    #correlations = 'data/network-traffic/correlations.csv'
    #"""The file path to the correlation coefficients for the target column."""

    original_training = 'data/network-traffic/kddcup.data.csv'
    """The file path to the original network traffic dataset."""

    original_verification = 'data/network-traffic/corrected.csv'
    """The file path to the original network traffic verification dataset."""

    preprocessed_training = 'data/network-traffic/preprocessed_training.csv'
    """The file path to the preprocessed network traffic training dataset."""

    preprocessed_verification = 'data/network-traffic/preprocessed_verification.csv'
    """The file path to the preprocessed network traffic verification dataset."""

    training = 'data/network-traffic/training_df.csv'
    """The file path to the training data frame."""

    training_scaled = 'data/network-traffic/training_df_s.csv'
    """The file path to the scaled training data frame."""

    training_undersampled = 'data/network-traffic/training_df_u.csv'
    """The file path to the undersampled training data frame."""

    training_undersampled_scaled = 'data/network-traffic/training_df_us.csv'
    """The file path to the undersampled scaled training data frame."""

    verification = 'data/network-traffic/verification_df.csv'
    """The file path to the verification data frame."""

    verification_scaled = 'data/network-traffic/verification_df_s.csv'
    """The file path to the scaled verification data frame."""

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

    @staticmethod
    def top(n, correlations=True):
        """Return the top `n` features in terms of absolute correlation coefficient.

        Parameters
        ----------
        n : int
            Number of features to return.
        correlations : bool
            If `True`, use correlation coefficients. If `False`, use data from
            feature importance analysis instead.
        
        Returns
        -------
        pandas.DataFrame :
            A data frame with features and their absolute correlation coefficients with
            the target column.

        See Also
        --------
        Col.above(theshold, correlations=True)
        """
        file = File.correlations if correlations else ""
        ranking = pd.read_csv(file, index_col=None)
        return ranking[:n]
    
    @staticmethod
    def above(threshold, correlations=True):
        """Return all features with an absolute correlation coefficient above
        the given `threshold`.

        Parameters
        ----------
        threshold : float
            Lower limit of the correlation coeffients to be returned.
        correlations : bool
            If `True`, use correlation coefficients. If `False`, use data from
            feature importance analysis instead.
        
        Returns
        -------
        pandas.DataFrame :
            A data frame with features and their absolute correlation coefficients with
            the target column.

        See Also
        --------
        Col.top(n, correlations=True)
        """
        file = File.correlations if correlations else ""
        ranking = pd.read_csv(file, index_col=None)
        return ranking[ranking['Coefficient'] >= threshold]

if __name__ == '__main__':
    print('This script is not meant to be run like this!')
