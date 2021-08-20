#!python3

def power(base, exponent):
    assert base > 0 and int(base) == base, 'base has to be a positive integer'
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)


if __name__ == '__main__':
    print(power(2, 4))  # This should return 16
