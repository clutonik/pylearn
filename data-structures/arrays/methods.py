#!python3
from array import *

# Exploring array methods


if __name__ == '__main__':
    arr1 = array('i', [1, 2, 3])

    # Extend an array using extend() method
    arr2 = array('i', [4, 5])
    arr1.extend(arr2)
    print(arr1)

    # Extend array from a list
    extend_list = [6, 7]
    arr1.fromlist(extend_list)
    print(arr1)

    # Remove an element from array
    arr1.remove(7)
    print(arr1)

    # Remove last element from array
    arr1.pop()
    print(arr1)

    # Get index of an element
    print(f'3 is at index {arr1.index(3)}')

    # Get Array buffer info (memory address, number of elements)
    print(arr1.buffer_info())

    # Count number of occurences of an element
    arr1.append(2)
    print(f'2 appears {arr1.count(2)} times')

    # Convert array to bytes
    tempString = arr1.tobytes()
    print(tempString)

    # Create array from bytes
    array_from_bytes = array('i')
    array_from_bytes.frombytes(tempString)
    print(array_from_bytes)

    # Convert array to python list
    arr1_list = arr1.tolist()
    print(arr1_list)

    # Slicing an array
    print(arr1[1:3])
