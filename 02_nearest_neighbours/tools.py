from typing import Union

import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets as datasets

def load_iris():
    '''
    Load the iris dataset that contains N input features
    of dimension F and N target classes.

    Returns:
    * inputs (np.ndarray): A [N x F] array of input features
    * targets (np.ndarray): A [N,] array of target classes
    '''
    iris = datasets.load_iris()
    return iris.data, iris.target, [0,1,2]

def split_train_test(features: np.ndarray, targets: np.ndarray,
    train_ratio:float=0.8) -> Union[tuple, tuple]:
    '''
    Shuffle the features and targets in unison and return
    two tuples of datasets, first being the training set,
    where the number of items in the training set is according
    to the given train_ratio
    '''
    np.random.seed(123)
    p = np.random.permutation(features.shape[0])
    features = features[p]
    targets = targets[p]

    split_index = int(features.shape[0] * train_ratio)

    train_features, train_targets = features[0:split_index, :],\
    targets[0:split_index]
    test_features, test_targets = features[split_index:-1, :],\
        targets[split_index: -1]

    return (train_features, train_targets), (test_features, test_targets)

def plot_points(points, point_targets):
    '''
    Plot a scatter plot of the first two feature dimensions
    in the point set
    '''
    colors = ['yellow', 'purple', 'blue']
    for i in range(points.shape[0]):
        [x, y] = points[i,:2]
        plt.scatter(x, y, c=colors[point_targets[i]], edgecolors='black',
            linewidths=2)
    plt.title('Yellow=0, Purple=1, Blue=2')
    plt.show()