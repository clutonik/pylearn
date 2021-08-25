#!python3

# get nth number from fibonacci sequence
def fib(n):
    assert n >= 0 and int(n) == n, 'n should be a positive integer'
    if n in [0, 1]:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(4))
