#!python3

# tuple basics


if __name__ == '__main__':
    # creating a tuple
    basic_tuple = 1, 2, 3
    print(f'basic_tuple: {basic_tuple}')

    # creating a tuple with single element
    # ',' at the end is important otherwise it will be a primitive data type (string/int etc)
    single_element_tuple = 1,
    print(f'single element tuple: {single_element_tuple}')

    # creating a tuple using built-in tuple() method
    built_in_tuple = tuple((1, 2))
    print(f'builtin tuple: {built_in_tuple}')
