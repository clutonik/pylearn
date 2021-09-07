#!python3

# Comprehensions
# 1. List comprehension
# 2. Set comprehension
# 3. Dictionary comprehension

if __name__ == '__main__':
    # list comprehension
    comp_list = [item for item in range(1, 5)]
    print(f'list() created using list comprehension: {comp_list}')

    # set comprehension
    comp_set = {char for char in 'apple'}  # creates {'e', 'p', 'l', 'a'}
    print(f'set() created through set comprehension: {comp_set}')

    # exercise: create a set of duplicate characters from an existing list
    input_list = ['a', 'b', 'c', 'b', 'e', 'a', 's']
    duplicates = {char for char in input_list if input_list.count(char) > 1}
    print(f'duplicates from input list: {duplicates}')

    # dictionary comprehension
    original_dict = {
        'age': 30,
        'name': 'Sahil'
    }

    # this one will create a new dict if value is of type int
    comp_dict = {key: value for key,
                 value in original_dict.items() if type(value) == int}
    print(f'dict() created using dictionary comprehension: {comp_dict}')
