#!python3

# accept a number and add up all numbers from 0 to passed number

def recursive_sum(n):
    assert n >= 0 and int(n) == n, 'n should be a positive integer'
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)


if __name__ == '__main__':
    print(recursive_sum(3))
