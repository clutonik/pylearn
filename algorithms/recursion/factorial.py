#!python3

# Get Factorial of a number
def factorial(n):
    assert n >= 0 and int(n) == n, 'n should be positive integer or zero'
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    print(factorial(4))
