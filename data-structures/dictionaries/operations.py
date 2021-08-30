#!python3

# Dict operations

if __name__ == '__main__':
    test_dict = {
        "name": "Sahil",
        "age": 30,
        "country": "CA"
    }

    print(f'original dict: \n{test_dict}')

    # Adding a key
    test_dict['mother_tongue'] = "punjabi"
    print(f'dict after inserting a key: \n{test_dict}')

    # Removing a key using pop() which returns the deleted value (not key)
    dict_for_pop = test_dict.copy()
    deleted_element = test_dict.pop('mother_tongue')
    print(f'Deleted element: {deleted_element}')

    # Removing a key using popitem() which returns key and value as tuple
    dict_for_popitem = test_dict.copy()
    deleted_element = dict_for_popitem.popitem()
    print(f'Deleted element: {deleted_element}')

    # Removing a key using del keyword
    # This can be used to delete the entire dict
    dict_for_del = test_dict.copy()
    del dict_for_del['age']
    print(f'dict after deleting a key using del keyword: \n{dict_for_del}')

    # Removing all elements/keys using clear method
    dict_for_clear = test_dict.copy()
    dict_for_clear.clear()
    print(
        f'dict after deleting all keys using clear keyword: \n{dict_for_clear}')

    # using in operator to check if a key exists
    if 'age' in test_dict:  # or test_dict.keys()
        print("used 'in' operator to check if 'age' key exists")

    # all() method to check if all elements in dict are true
    bool_dict = {
        "field1": True,
        "field2": False
    }
    if all(test_dict):
        print('checked string dict using all() method...')

    if all(bool_dict.values()):
        print('checked bool dict using all() method...')

    # len() method returns number of pairs for dict
    print(f'pairs in our test dict: {len(test_dict)}')

    # sorted() method sorts elements in specific order
    print(f'sorted dict: {sorted(test_dict, reverse=False)}')
