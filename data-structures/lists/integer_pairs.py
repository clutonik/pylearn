#!python3

# Program to find all pairs of integers whose sum is equal to given number.

def find_pairs(list, n):
    pairs = []
    for i in range(0, len(list)):
        for j in range(1, len(list)):
            if list[i] + list[j] == n:
                pairs.append([list[i], list[j]])

    print(pairs)


if __name__ == '__main__':
    numbers = [1, 3, 4, 6, 9, 7]
    find_pairs(numbers, 9)
