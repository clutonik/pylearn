#!python3

# Sum of Digits of an integer

def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "n must be a positive integer"
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(int(n // 10))


if __name__ == "__main__":
    print(sum_of_digits(123))
    print(sum_of_digits(0))
    print(sum_of_digits(98))
    print(sum_of_digits(9876))
