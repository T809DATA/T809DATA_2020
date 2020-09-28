import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split


def load_cancer():
    '''
    Return the breast cancer dataset split into
    train and test sets.
    '''
    cancer = datasets.load_breast_cancer()
    X_train, X_test, t_train, t_test = train_test_split(
        cancer.data, cancer.target,
        test_size=0.3)
    return (X_train, t_train), (X_test, t_test)


def load_binary_iris():
    '''
    Load the iris dataset that contains N input features
    of dimension F and N target classes. Only load classes
    0 an 1.

    Returns:
    * inputs (np.ndarray): A [N x F] array of input features
    * targets (np.ndarray): A [N,] array of target classes
    '''
    iris = datasets.load_iris()
    index = np.hstack((
        np.where(iris.target == 0),
        np.where(iris.target == 1)))
    iris.data = iris.data[index[0], :]
    iris.target = iris.target[index[0]]
    X_train, X_test, t_train, t_test = train_test_split(
        iris.data, iris.target,
        test_size=0.3)
    return (X_train, t_train), (X_test, t_test)


def plot_svm_margin(
    svc,
    X: np.ndarray,
    t: np.ndarray
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
    plt.scatter(X[:, 0], X[:, 1], c=t, s=30,
                cmap=plt.cm.Paired)

    # plot the decision function
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # create grid to evaluate model
    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T

    Z = svc.decision_function(xy).reshape(XX.shape)

    # plot decision boundary and margins
    ax.contour(
        XX, YY, Z,
        colors='k', levels=[-1, 0, 1],
        alpha=0.5, linestyles=['--', '-', '--'])

    # plot support vectors
    ax.scatter(
        svc.support_vectors_[:, 0],
        svc.support_vectors_[:, 1],
        s=100, linewidth=1, facecolors='none', edgecolors='k')
    plt.show()
