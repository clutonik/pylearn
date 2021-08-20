#!python3

# Calculate product of all elements within an array
def product_of_array(x):
    if len(x) == 0:
        return 1
    else:
        return x[0] * product_of_array(x[1:])


if __name__ == '__main__':
    print(product_of_array([1, 2, 3]))
