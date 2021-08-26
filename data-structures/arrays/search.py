#!python3
from array import *


def search(arr, value) -> int:
    '''
    searches for a value in an array and returns its index

    Big O: O(n)

    params:
    arr: Array to search the value in
    value: value to search

    returns: index at which this value is located
    '''
    for i in arr:
        if i == value:
            return arr.index(i)

    return -1


if __name__ == '__main__':
    arr1 = array('i', [1, 2, 3, 6, 9])
    value_to_search = 6
    position = search(arr1, value_to_search)
    if position == -1:
        print(f'value {value_to_search} is not present in array {arr1}')
    else:
        print(f'value {value_to_search} is at index {position}')
