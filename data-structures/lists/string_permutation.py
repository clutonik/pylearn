#!python3

# code to check if two strings are permutations of each other or not
def is_permutation(string1, string2) -> bool:
    lower_string1_list = list(string1.lower())
    lower_string2_list = list(string2.lower())
    print(lower_string1_list)
    for c in lower_string1_list:
        if c not in lower_string2_list:
            return False

    for c in lower_string2_list:
        if c not in lower_string1_list:
            return False

    return True


if __name__ == '__main__':
    print(is_permutation("Sahil", "Ilahs"))
