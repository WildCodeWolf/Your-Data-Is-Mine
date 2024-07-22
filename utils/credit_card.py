"""This file contains auxiliaries for handling the credit card dataset."""

import pandas as pd


class File:
    """Contains the file names for all csv files for the credit card dataset."""

    correlations = 'data/creditcard/correlations.csv'
    """The file path to the correlation coefficients for the target column."""

    original = 'data/creditcard/creditcard.csv'
    """The file path to the original credit card dataset."""

    preprocessed = 'data/creditcard/preprocessed.csv'
    """The file path to the preprocessed credit card dataset."""

    training = 'data/creditcard/training_df.csv'
    """The file path to the training data frame."""

    training_scaled = 'data/creditcard/training_df_s.csv'
    """The file path to the scaled training data frame."""

    training_undersampled = 'data/creditcard/training_df_u.csv'
    """The file path to the undersampled training data frame."""

    training_undersampled_scaled = 'data/creditcard/training_df_us.csv'
    """The file path to the undersampled scaled training data frame."""

    verification = 'data/creditcard/verification_df.csv'
    """The file path to the verification data frame."""

    verification_scaled = 'data/creditcard/verification_df_s.csv'
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
        'Time',
        'V1',
        'V2',
        'V3',
        'V4',
        'V5',
        'V6',
        'V7',
        'V8',
        'V9',
        'V10',
        'V11',
        'V12',
        'V13',
        'V14',
        'V15',
        'V16',
        'V17',
        'V18',
        'V19',
        'V20',
        'V21',
        'V22',
        'V23',
        'V24',
        'V25',
        'V26',
        'V27',
        'V28',
        'Amount',
        'Class',
    ]
    """The original column names (in order)."""

    _all_pretty = [
        'Time in h',
        'V $1$',
        'V $2$',
        'V $3$',
        'V $4$',
        'V $5$',
        'V $6$',
        'V $7$',
        'V $8$',
        'V $9$',
        'V $10$',
        'V $11$',
        'V $12$',
        'V $13$',
        'V $14$',
        'V $15$',
        'V $16$',
        'V $17$',
        'V $18$',
        'V $19$',
        'V $20$',
        'V $21$',
        'V $22$',
        'V $23$',
        'V $24$',
        'V $25$',
        'V $26$',
        'V $27$',
        'V $28$',
        'Amount in USD',
        'Fradulent ($0$ - Yes, $1$ - No)',
    ]
    """The column names (in order)."""
    time = _all_pretty[0]
    """The time column."""
    amount = _all_pretty[29]
    """The Amount column."""
    target = _all_pretty[30]
    """The Class (or Target) column."""

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
