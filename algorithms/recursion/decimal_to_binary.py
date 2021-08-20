#!python3

# Convert Decimal to binary using recursion

def decimal_to_binary(n):
    assert n >= 0 and int(
        n) == n, 'n has to be greater than 0 and integer only'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(int(n/2))


if __name__ == '__main__':
    print(decimal_to_binary(13))
    print(decimal_to_binary(10))
