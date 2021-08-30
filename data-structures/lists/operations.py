#!python3

def traverse_list(items):
    # range function goes till n-1
    for i in range(len(items)):
        print(i)


if __name__ == '__main__':
    traverse_list([1, 2, 3, 4, 5])

    a = [1, 2, 3, 4]

    # Insert an element to list at any position
    a.insert(4, 5)
    print(a)

    # insert an element to list at end
    a.append(6)
    print(a)

    # extending a list
    b = [7, 8]
    a.extend(b)
    print(a)

    # Slicing a list
    print(a[1:3])

    # Delete an element from list
    # pop() method returns the deleted element
    a.pop(1)  # Index to remove
    print(a.pop())  # last one
    print(a)

    # Delete an element using delete() method
    # Delete method does not return anything
    # del can be used with slicing to delete multiple elements
    del a[1]
    print(a)

    # delete an element using remove() method
    # provide an element instead of an index
    # remove() does not return anything
    a.remove(1)
    print(a)

    # searching an element in list
    # method-1 (using 'in' keyword)
    if 4 in a:
        print(f'4 is present at index: {a.index(4)}')

    # method-2 (using searching algorithms)
    for i in a:
        if i == 4:
            print(f'4 found using search algorithm at {a.index(4)}')
            break

    # Create a string from list
    string_list = ['join', 'test']
    delimiter = '-'
    print(delimiter.join(string_list))

    # sort a list using sorted method
    unsorted_list = [1, 3, 2, 7, 6, 5]
    print(f'sorted list: {sorted(unsorted_list)}')
    print(f'original list: {unsorted_list}')
