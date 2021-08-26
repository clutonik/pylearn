#!python3

from array import *


def traverseArray(arr):
    for i in arr:
        print(arr[i])


if __name__ == '__main__':
    arr1 = array('i', [1, 2, 3, 4, 5])
    print(arr1)

    # Insert an element at a specific index
    arr1.insert(0, 0)
    print(arr1)

    # traverse an array
    traverseArray(arr1)
