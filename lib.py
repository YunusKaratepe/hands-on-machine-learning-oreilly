import numpy as np


def train_test_split(data, test_prop, seed=0):

    np.random.seed(seed)
    length = len(data)
    shuffled_indices = np.random.permutation(length)
    
    test_indices = shuffled_indices[:int(test_prop * length)]
    train_indices = shuffled_indices[int(test_prop * length):]
    return data.iloc[train_indices], data.iloc[test_indices]
    