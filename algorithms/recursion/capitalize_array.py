#!python3

# Accept an array of strings and capitialize each string
def capitialize_array(arr):
    capitialized_array = []
    if len(arr) == 0:
        return capitialized_array
    assert type(arr[0]) == str, f'Array element {arr[0]} has to be a string'

    capitialized_array.append(arr[0].capitalize())
    return capitialized_array + capitialize_array(arr[1:])


if __name__ == '__main__':
    print(capitialize_array([1, 'sahil', 'vinood', 'claire']))
