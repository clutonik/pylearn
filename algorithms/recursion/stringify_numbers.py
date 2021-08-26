#!python3

# Create a method which accepts a dict object and converts all numbers to string

def stringify_numbers(obj):
    string_dict = obj

    for key in obj:
        if type(obj[key]) is dict:
            string_dict[key] = stringify_numbers(obj[key])
        elif type(obj[key]) is int:
            string_dict[key] = str(obj[key])

    return string_dict


if __name__ == '__main__':
    obj1 = {
        "num": 2,
        "string": "test",
        "nested": {
            "nested_number": 5,
            "nested_string": "nested"
        }
    }
    print(stringify_numbers(obj1))
