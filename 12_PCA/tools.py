import sklearn.datasets as datasets


def load_cancer():
    '''
    Return the breast cancer dataset split into
    train and test sets.
    '''
    cancer = datasets.load_breast_cancer()
    return cancer.data, cancer.target
