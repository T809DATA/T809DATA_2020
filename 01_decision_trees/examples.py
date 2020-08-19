import numpy as np
import matplotlib.pyplot as plt

from tools import load_iris, split_train_test

def exclusive_interval():
    '''
    Create 50 linearly spaced values between the minimum
    and maximum values in a given list. We also want to
    exclude the min and the max in the interval.
    '''
    num_points = 5
    values = np.array([3, 5, 4, 6, 2, 0, 1, 1, 6, 2, 5])
    min_value = values.min()
    max_value = values.max()
    print(f'Interval is : [{min_value}, {max_value}]')

    interval = np.linspace(min_value, max_value, num_points+2)[1:-1]
    print(f'{num_points} linearly spaced within the range: {interval}')

def using_iris():
    '''
    Shows how load_iris works
    '''
    # 1. Load the Iris dataset:
    features, targets, classes = load_iris()

    [n, f_dim] = features.shape

    print(f'* The dataset contains {n} samples')
    print(f'* Each sample has {f_dim} features')

    # 2. get the first datapoint
    first_feature_set = features[0, :]
    first_target = targets[0]

    print(f'* The first sample has the features:\n{first_feature_set} '+\
        f'and belongs to the class {first_target}')

    print('* Each datapoint can belong to any of the following classes:'+\
        f'\n{classes}')

    # 3. Split into train and test sets
    (train_features, train_targets), (test_features, test_targets) =\
        split_train_test(features, targets, train_ratio=0.9)

    train_n, test_n = train_features.shape[0], test_features.shape[0]
    print(f'* The train set contains {train_n} samples')
    print(f'* The test set contains {test_n} samples')

def using_classes():
    # 1. define a simple class
    class Vehicle:
        # the initialization method:
        def __init__(self,
            num_wheels:int,
            num_doors:int,
            color:str
        ):
            self.num_wheels = num_wheels
            self.num_doors = num_doors
            self.color = color

        # define some class methods
        def add_wheel(self):
            self.num_wheels += 1

        def remove_wheel(self):
            self.num_wheels -= 1

        # adding @property to class methods converts them to
        # properties so we can do Vehicle.is_car instead of
        # Vehicle.is_car()
        @property
        def is_car(self):
            '''A car should have at least 4 wheels and 2 doors
            '''
            return self.num_wheels >= 4 and self.num_doors >= 2

        def say_hello(self):
            print('Hey! I am a vehicle with '+\
                f'{self.num_wheels} wheels, {self.num_doors} '+\
                f'doors and I am {self.color}!')
            if self.is_car:
                print('Oh, and also I am a car.')

    # 2. Create two instances of Vehicle
    eighteen_wheeler = Vehicle(18, 2, 'black')
    bicycle = Vehicle(2, 0, 'red')

    eighteen_wheeler.say_hello()
    eighteen_wheeler.remove_wheel()
    print(f'The wheeler now has {eighteen_wheeler.num_wheels} wheels')

    bicycle.say_hello()
    bicycle.add_wheel()
    print(f'The bike now has {bicycle.num_wheels} wheels')



if __name__ == '__main__':
    exclusive_interval()
    print('-'*60)
    using_iris()
    print('-'*60)
    using_classes()
