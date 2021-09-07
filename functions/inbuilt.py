#!python3
from functools import reduce

# Exploring inbuilt functions
# 1. map()
# 2. filter()
# 3. zip()


def multiply(item: int, factor: int = 2):
    """
    multiplies an item with given factor(default=2)
    this method has been created to work with map() 

    Args:
        item (int): [description]
        factor (int, optional): [description]. Defaults to 2.

    Returns:
        int: result after multiplication
    """
    return item * factor


def is_odd(item: int) -> bool:
    """
    checks if a number is odd.
    this method has been created to work with filter()

    Args:
        item (int): input number

    Returns:
        bool: True if number is odd
    """
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]

    print(f'Original List: {test_list}')

    print(f'using map(): {list(map(multiply, test_list))}')

    # using map() with lambda expression
    print(
        f'map() using lambda expression: {list(map(lambda value: value*2, test_list))}')  # value comes from test_list

    # using filter() to get only odd numbers from the list
    print(f'using filter(): {list(filter(is_odd, test_list))}')
    print(f'filter() return type: {type(filter(is_odd, test_list))}')

    # lists for zip()
    # zip() combines data from multiple iterables together in the same order as tuples
    students = ['sahil', 'vinood', 'prem']
    age = [30, 31, 25]
    print(f'zipped data: {list(zip(students, age))}')

    # reduce()
    # this will return a single digit result of operation (item + acc)
    print(reduce(accumulator, test_list, 0))
