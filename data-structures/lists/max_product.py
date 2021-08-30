#!python3

# find max product of two integers in array

def find_max_product(numbers):

    max_product = 0
    for i in range(0, len(numbers)):
        for j in range(1, len(numbers)):
            if numbers[i] == numbers[j]:
                continue
            elif numbers[i] * numbers[j] > max_product:
                max_product = numbers[i] * numbers[j]
                pairs = str(numbers[i]) + ',' + str(numbers[j])

    print(pairs)
    print(max_product)


if __name__ == '__main__':
    numbers = [1, 2, 30, 57, 35, 58, 19]
    find_max_product(numbers)
