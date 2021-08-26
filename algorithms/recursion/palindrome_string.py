#!python3

# Check if a string is a palindrome (reverse is same as original string)

def is_palindrome(x):
    if len(x) <= 1:
        return True
    elif x[0] != x[len(x)-1]:
        return False
    else:
        return is_palindrome(x[1:len(x)-1])


if __name__ == '__main__':
    print(is_palindrome('tacocat'))
