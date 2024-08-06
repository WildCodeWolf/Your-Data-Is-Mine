"""This file contains functions used to evaluate models and tuning processes."""

from collections import namedtuple
from sklearn.metrics import accuracy_score, fbeta_score, confusion_matrix, classification_report

model_result = namedtuple('ModelEvaluationResult', ['model', 'accuracy', 'fbeta', 'predictions'])
"""Construct a tuple containing the results of evaluating an ML model."""

def evaluate_model(model, X_test, y_true, beta=10., average='weighted', display_false_negatives=None, threshold=None):
    """Make predictions, compute and display metrics for a given `model` and return the result.
    
    Parameters
    ----------
    model : scikit-learn or `tensorflow.keras` model
        
        The model to evaluate.  The method `predict(X_test)` will be passed to this object.
    
    X_test : array-like

        The verification data for the `model` to make predictions.  Needs to have the same number of
        features as the training data has.
    
    y_true : array-like
        
        The expected prediction for `X_test`.
    
    beta : `float`, default: `10.0`
        
        The beta parameter for computing the `fbeta_score`.
    
    average : {`'weighted'`, `'binary'`, `'micro'`, `'macro'`}, default: `'weighted'`

        The method to average fbeta scores for multi-classification scenarios.
    
    display_false_negatives : `bool` | `None`, default: `None`

        If `true`, print a line that contains the number of false negative predictions as well
        as its percentage with respect to the true negative cases.  Only valid for binary
        classification scenarios.

        If `false`, no such line is produced.

        If `None`, this line is produced if `y_true` is one-dimensional.
    
    threshold : `float` | `None`, default: `None`

        If given a floating point number (between `0.0` and `1.0`), predictions on the test input
        will be computed using probability predictions and comparing those to the given value.
        This only works for binary predictions.
        The lower the value, the more likely the result to be interpreted as positive.
    
    Returns
    -------

    `ModelEvaluationResult` :
        Named tuple with the fields `model`, `accuracy`, `fbeta` and `predictions`.
    """
    display_false_negatives_ = display_false_negatives if display_false_negatives is not None else len(y_true.shape) == 1
    pred = model.predict(X_test) if threshold is None else (model.predict_proba(X_test)[:, 1] >= threshold).astype(int)
    acc = accuracy_score(y_true, pred)
    fbeta = fbeta_score(y_true, pred, beta=beta, average=average, zero_division=0.0)
    print('\n-- Testing Results --')
    print(f'Accuracy    on Verification Data:\t{acc:.6f}')
    print(f'Fbeta scroe on Verification Data:\t{fbeta:.6f}\n')
    print(classification_report(y_true, pred, zero_division=0.0))
    if display_false_negatives_:
        total_attacks = y_true.value_counts().iloc[1]
        confusion = confusion_matrix(y_true, pred)
        false_negatives = confusion[1, 0]
        print(f'False negatives: {false_negatives} ({100 * false_negatives / total_attacks:.3f}% out of {total_attacks} true positives, {100 * false_negatives / len(y_true):.3f}% overall)\n')
    return model_result(model, acc, fbeta, pred)

hpt_result = namedtuple('HperparameterTuningResult', ['model', 'best_params', 'best_score', 'accuracy', 'fbeta', 'predictions'])
"""Construct a tuple containing the results of evaluating a hyperparameter tuning process."""

def evaluate_hpt(model, X_test, y_true, beta=10., average='weighted', display_false_negatives=None, threshold=None):
    """Make predictions, compute and display metrics for a given `model` and return the result.

    The behaviour is similar to `evaluate_model(model, X_test, y_true, beta, average, display_false_negatives)`,
    but it expects `model` to be a `GridSearchCV` object from `sklearn.model_selection` and
    extracts some additional information from that.
    
    Parameters
    ----------
    model : `sklearn.model_selection.GridSearchCV`
        
        The model to evaluate.
    
    X_test : array-like

        The verification data for the `model` to make predictions.  Needs to have the same number of
        features as the training data has.
    
    y_true : array-like
        
        The expected prediction for `X_test`.
    
    beta : `float`, default: `10.0`
        
        The beta parameter for computing the `fbeta_score`.
    
    average : {`'weighted'`, `'binary'`, `'micro'`, `'macro'`}, default: `'weighted'`

        The method to average fbeta scores for multi-classification scenarios.
    
    display_false_negatives : `bool` | `None`, default: `None`

        If `true`, print a line that contains the number of false negative predictions as well
        as its percentage with respect to the true negative cases.  Only valid for binary
        classification scenarios.

        If `false`, no such line is produced.

        If `None`, this line is produced if `y_true` is one-dimensional.

    threshold : `float` | `None`, default: `None`

        If given a floating point number (between `0.0` and `1.0`), predictions on the test input
        will be computed using probability predictions and comparing those to the given value.
        This only works for binary predictions.
        The lower the value, the more likely the result to be interpreted as positive.
    
    Returns
    -------

    `HyperparameterTuningResult` :
        Named tuple with the fields `model`, `best_params`, `best_score`, `accuracy`, `fbeta` and `predictions`.
    """
    best_params = model.best_params_
    param_string = ''.join((f'\t{key}:\t{value}\n' for key, value in best_params.items()))
    best_score = model.best_score_
    print('-- Training Results --')
    print(f'Best Parameters:\n{param_string}', end='')
    print(f'Best Score:\n\t{best_score:.6f}')
    model_result = evaluate_model(model, X_test, y_true, beta, average, display_false_negatives, threshold)
    acc = model_result.accuracy
    fbeta = model_result.fbeta
    pred = model_result.predictions
    return hpt_result(model, best_params, best_score, acc, fbeta, pred)

def compare_models(new_results, old_results, compare_fbeta=True):
    """Compare two given results (obtained from either `evaluate_model()` or `evaluate_hpt()`),
    print information on which is better and return the better model and the better score.

    Parameters
    ----------
    new_results : `ModelEvaluationResult` | `HyperparameterTuningResult`
    
        The results of the new model's evaluation.

    new_results : `ModelEvaluationResult` | `HyperparameterTuningResult`

        The results of the old model's evaluation.
    
    compare_fbeta : `bool`, default: `True`

        If `True`, use fbeta score to determine the better model.  Otherwise, use accuracy score.
    
    Returns
    -------

    `ModelEvaluationResult` | `HyperparameterTuningResult` :
        The better of the two results.
    """
    is_improved = new_results.fbeta > old_results.fbeta if compare_fbeta else new_results.accuracy > old_results.accuracy
    is_hpt_comparison = isinstance(new_results, hpt_result) and isinstance(old_results, hpt_result)

    print('-- HPT Evaluation --') if is_hpt_comparison else print('-- Model Comparison --')
    print(f'{new_results.fbeta - old_results.fbeta = :.6f}', end='')
    print(' --> Improvement!') if new_results.fbeta > old_results.fbeta else print(' --> Worsened!')
    print(f'{new_results.accuracy - old_results.accuracy = :.6f}', end='')
    print(' --> Improvement!') if new_results.accuracy > old_results.accuracy else print(' --> Worsened!')

    print(f'\nBest model so far:')
    best_results = new_results if is_improved else old_results
    if is_hpt_comparison:
        best_model = f'{best_results.model.best_estimator_} with Parameters\n{best_results.best_params}'
    else:
        best_model = f'{best_results.model}' if isinstance(best_results, model_result) else f'{best_results.model.best_estimator_}'
    best_score = best_results.fbeta if compare_fbeta else best_results.accuracy
    print(f'{best_model}\nIts score: {best_score:.6f}')

    return new_results if is_improved else old_results
