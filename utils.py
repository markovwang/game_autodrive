import keyboard.input_keys as input_keys
import keyboard.key_get as key_get
import numpy as np


def keys_to_output(keys: np.ndarray) -> np.ndarray:
    """
       Convert keys to a ...multi-hot... array
       Input:
        - np.ndarray of strings ["A","W"]
       Ouput:
        - multi-hot array of integers (0,1) representing which keys are pressed (1). Array: [A,D,W,S]
       """
    output = np.asarray([0, 0, 0, 0])

    if "A" in keys:
        output[0] = 1
    if "D" in keys:
        output[1] = 1
    if "W" in keys:
        output[2] = 1
    if "S" in keys:
        output[3] = 1

    return output


def counter_keys(key: np.ndarray) -> int:
    """
    multi-hot-vevtor to one hot vector
    input a np.array like [1,1,1,1]
    output index
    """
    if np.array_equal(key, [0, 0, 0, 0]):
        return 0
    elif np.array_equal(key, [1, 0, 0, 0]):
        return 1
    elif np.array_equal(key, [0, 1, 0, 0]):
        return 2
    elif np.array_equal(key, [0, 0, 1, 0]):
        return 3
    elif np.array_equal(key, [0, 0, 0, 1]):
        return 4
    elif np.array_equal(key, [1, 0, 1, 0]):
        return 5
    elif np.array_equal(key, [1, 0, 0, 1]):
        return 6
    elif np.array_equal(key, [0, 1, 1, 0]):
        return 7
    elif np.array_equal(key, [0, 1, 0, 1]):
        return 8
    else:
        return -1


def key_convert(keys: np.ndarray) -> int:
    multi_hot = keys_to_output(keys)
    return counter_keys(multi_hot)
