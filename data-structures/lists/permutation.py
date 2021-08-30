#!python3


# checking permutation for 2 lists
def is_permutation(list1, list2) -> bool:
    # if number of elements is not same, return False
    if len(list1) != len(list2):
        return False

    # sort both lists
    list1.sort()
    list2.sort()

    # compare both lists
    if list1 != list2:
        return False

    return True


if __name__ == '__main__':
    int_list1 = [1, 2, 3]
    int_list2 = [1, 3, 2]
    string_list1 = ['a', 'b', 'c']
    string_list2 = ['c', 'c', 'a']
    print(is_permutation(int_list1, int_list2))  # returns True
    print(is_permutation(string_list1, string_list2))  # returns False
