#!python3

def gcd(x, y):
    assert int(x) == x and int(y) == y, 'x, y have to be positive integers'
    if y == 0:
        return x
    elif x == 0:
        return 0
    else:
        # y becomes x, and it is the remainder of the previous modulo operation
        # this follows Euclidean Algorithm
        return gcd(y, x % y)


if __name__ == '__main__':
    print(gcd(48, 18))
    print(gcd(50, 10))
    print(gcd(500, 100))
    print(gcd(0, 5))
