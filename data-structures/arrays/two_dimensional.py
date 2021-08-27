#!python3
import numpy


def traverse_two_d_array(arr):
    # Time complexity is O(N^2) quadratic if no. of rows = no. of columns
    for i in range(len(arr)):  # Time complexity O(mn)
        print(f'Looping over row: {i}')
        for j in range(len(arr[0])):
            print(arr[i][j])


def linear_search(arr, value):
    for i in range(len(arr)):  # Time complexity O(mn)
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                return f'[{str(i)}][{str(j)}]'

    return -1


if __name__ == '__main__':
    # Two dimensional array
    two_d_array = numpy.array(
        [[33, 31, 32, 21], [12, 15, 17, 13], [22, 24, 25, 28]])

    print('Original:')
    print(two_d_array, '\n')

    # Insert a row to two dimensional array at a particular index
    # 0: position
    # axis: row/column
    new_array = numpy.insert(two_d_array, 0, [[13, 28, 23, 14]], axis=0)
    print('After adding a row: ')
    print(new_array, '\n')

    # Insert a column to two dimensional array at a particular index
    new_column_array = numpy.insert(two_d_array, 0, [[13, 28, 23]], axis=1)
    print('After adding a column: ')
    print(new_column_array, '\n')

    # Adding a row/column at the end
    new_column_array = numpy.append(two_d_array, [[1, 2, 3, 4]], axis=0)
    print('After adding a row at the end: ')
    print(new_column_array, '\n')

    # Getting number of rows in a 2 dimensional array
    print(f'Number of rows in original array: {len(two_d_array)}')

    # Getting number of columns in a 2 dimensional array
    print(f'Number of columns in original array: {len(two_d_array[0])}')

    # Traversing a 2 dimensional array
    print(f'Traversed array: \n')
    traverse_two_d_array(two_d_array)

    # Linear search for an element
    value_to_search = 17
    search = linear_search(two_d_array, value_to_search)
    if search == -1:
        print(f'value {value_to_search} not found')
    else:
        print(f'value {value_to_search} found at index {search}')

    # Deleting a row from a two dimensional array
    new_deleted_row_array = numpy.delete(two_d_array, 0, axis=0)
    print('Original:')
    print(two_d_array, '\n')
    print('Deleted Row: ')
    print(new_deleted_row_array, '\n')

    # Deleting a column from a two dimensional array
    new_deleted_row_array = numpy.delete(two_d_array, 0, axis=1)
    print('Original:')
    print(two_d_array, '\n')
    print('Deleted column: ')
    print(new_deleted_row_array, '\n')
