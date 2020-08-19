import numpy as np

def remove_one(points: np.ndarray, i: int):
    '''
    Removes the i-th from points and returns
    the new array
    '''
    return np.concatenate((points[0:i], points[i+1:]))

if __name__ == '__main__':
    points = np.array([0,1,2,3,4,5])
    for i in range(points.shape[0]):
        print(remove_one(points, i))