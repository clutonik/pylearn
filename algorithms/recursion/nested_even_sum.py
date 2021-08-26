#!python3

# Create a method to traverse a dict object and return the sum of all
# even numbers

def nested_even_sum(obj):
    sum = 0
    for key in obj:
        if type(obj[key]) is dict:
            sum += nested_even_sum(obj[key])
        elif type(obj[key]) is int and obj[key] % 2 == 0:
            sum += obj[key]

    return sum


if __name__ == '__main__':
    obj1 = {
        "parent": 2,
        "inner": {
            "number_here": 4,
            "boolean": True,
            "String": "yes",
            "nested": {
                "number_there": 6
            }
        }
    }
    print(nested_even_sum(obj1))
