#!python3

# Method to convert all list elements to uppercase

def uppercase_array(arr):
    uppercased_array = []

    if len(arr) == 0:
        return uppercased_array

    assert type(arr[0]) is str, f'Element: {arr[0]} is not a str'

    uppercased_array.append(arr[0].upper())
    return uppercased_array + uppercase_array(arr[1:])


if __name__ == '__main__':
    print(uppercase_array(['Sahil', 'Vinood', 'Claire']))
