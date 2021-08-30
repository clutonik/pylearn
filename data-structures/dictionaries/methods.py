#!python3

# Dict operations

if __name__ == '__main__':
    test_dict = {
        "name": "Sahil",
        "age": 30,
        "country": "CA"
    }

    print(f'original dict: {test_dict}')

    # returns a new dict
    copied_dict = test_dict.copy()
    print(f'copied dict: {copied_dict}')

    # fromkeys()
    # you can optionally initialize all keys using a single value
    from_keys_dict = {}.fromkeys(['name', 'age', 'city'])
    print(f'dict created using fromkeys(): {from_keys_dict}')

    # get() to get value of a given key
    print(
        f"value for key named 'state' using get() method: {test_dict.get('state', 'ON')}")

    # items() - returns list of key value pairs as tuple
    print(f'items() method: {test_dict.items()}')

    # keys() - returns list of all keys
    print(f'keys() method: {test_dict.keys()}')

    # values() - returns list of all values
    print(f'values() method: {test_dict.values()}')

    # setdefault()
    # search for a key in dict and if missing, add it to dict with an optional default value
    test_dict.setdefault('state', 'ON')
    print(f'modified dict after setdefault(): {test_dict}')

    # update() - takes another dict or tuple as parameter
    dict_to_add = {
        "gender": "male",
        "occupation": "software engineer"
    }
    test_dict.update(dict_to_add)
    print(f'updated dict after using update(): {test_dict}')
