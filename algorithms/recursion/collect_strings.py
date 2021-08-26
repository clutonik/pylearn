#!python3

# Function to collect all strings from a dict obj and return them
# as list

def collect_strings(obj):
    result = []
    for key in obj:
        if type(obj[key]) is str:
            result.append(obj[key])
        elif type(obj[key]) is dict:
            result = result + collect_strings(obj[key])

    return result


if __name__ == '__main__':
    obj1 = {
        "field1": "foo",
        "field2": "bar",
        "field3": 10,
        "boolean": True,
        "nested_field": {
            "field1": "nested-foo",
            "field2": "nested-bar"
        }
    }

    print(collect_strings(obj1))
