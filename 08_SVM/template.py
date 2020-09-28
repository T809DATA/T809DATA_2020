from tools import plot_svm_margin, load_cancer
from sklearn import svm
from sklearn.datasets import make_blobs
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score)

import numpy as np
import matplotlib.pyplot as plt


def _plot_linear_kernel():
    X, t = make_blobs(...)
    ...
    plot_svm_margin(...)


def _subplot_svm_margin(
    svc,
    X: np.ndarray,
    t: np.ndarray,
    num_plots: int,
    index: int
):
    '''
    Plots the decision boundary and decision margins
    for a dataset of features X and labels t and a support
    vector machine svc.

    Input arguments:
    * svc: An instance of sklearn.svm.SVC: a C-support Vector
    classification model
    * X: [N x f] array of features
    * t: [N] array of target labels
    '''
    # similar to tools.plot_svm_margin but added num_plots and
    # index where num_plots should be the total number of plots
    # and index is the index of the current plot being generated
    ...


def _compare_gamma():
    X, t = make_blobs(n_samples=40, centers=2, random_state=6)

    clf = svm.SVC(...)
    ...
    _subplot_svm_margin(clf, X, t, 3, 1)

    clf = ...
    ...
    _subplot_svm_margin(clf, X, t, 3, 2)

    ...

    plt.show()


def _compare_C():
    ...


def train_test_SVM(
    svc,
    X_train: np.ndarray,
    t_train: np.ndarray,
    X_test: np.ndarray,
    t_test: np.ndarray,
):
    '''
    Train a configured SVM on <X_train> and <t_train>
    and then measure accuracy, precision and recall on
    the test set

    This function should return (accuracy, precision, recall)
    '''
    ...
