#!python3

# Calculation of the power of a number.
def power_of_number(n, p):
    assert p > 0 and int(p) == p
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return n * power_of_number(n, p-1)


if __name__ == '__main__':
    print(power_of_number(2, 4))
