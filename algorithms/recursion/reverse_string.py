#!python3

# Reverse a string
def reverse(x):
    if len(x) <= 1:
        return x
    else:
        return x[len(x)-1] + reverse(x[:len(x)-1])


if __name__ == '__main__':
    print(reverse('Karishma'))
