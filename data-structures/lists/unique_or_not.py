#!python3

# Check if all elements in list are unique or not
def is_unique(list):
    existing_elements = []
    for i in range(0, len(list)):
        if list[i] in existing_elements:
            return False, list[i]
        else:
            existing_elements.append(list[i])

    return True, None


if __name__ == '__main__':
    numbers = [1, 3, 2, 4, 5]
    unique, number = is_unique(numbers)
    if not unique:
        print(f'{number} has been encountered again')
    else:
        print(f'{numbers} is unique')
