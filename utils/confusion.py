"""This file contains the `confusion_matrix` function to display a simple
confusion matrix, but with the style settings from the `style` script."""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix as matrix
from .style import Colors

def confusion_matrix(y_true, y_pred, model=None):
    """Displays a confusion matrix.

    Parameters
    ----------
    y_true : array-like

        The true labels.
    
    y_pred : array-like

        The models' predicted labels.
    
    model : `str` | `None`, default: `None`

        If given, the title will contain the text as the model for which the
        confusion matrix gets constructed.
    """
    plt.figure(figsize=(5.5,4))
    sns.heatmap(data=matrix(y_true, y_pred), annot=True, cmap=Colors.blues_c)
    title = f"Confusion Matrix for {model}" if model else "Confusion Matrix"
    plt.title(title)
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.show()