#!python3

# Program to find missing number from a series of numbers

def find_missing_number(list, n):
    expected_sum = n*(n+1)/2
    actual_sum = 0

    # loop over the list and calculate sum
    for i in list:
        actual_sum += i

    missing_number = round(expected_sum - actual_sum)

    if missing_number > 0:
        print(f'missing number: {round(expected_sum - actual_sum)}')
    else:
        print(f'the list has all the numbers in it....Are you trying to test me?')


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    find_missing_number(numbers, 10)
