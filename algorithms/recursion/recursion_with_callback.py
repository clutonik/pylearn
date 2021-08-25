#!python3

# Accept an array and a callback method

def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def recursion_with_cb(arr, cb):
    if len(arr) == 0:
        return False
    elif is_odd(arr[len(arr)-1]):
        return True
    else:
        return recursion_with_cb(arr[:len(arr)-1], cb)


if __name__ == '__main__':
    print(recursion_with_cb([2, 4], is_odd))
