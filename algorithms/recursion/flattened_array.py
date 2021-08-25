#!python3

# Accept array of arrays and return a flattend array

def flatten(arr):
    resultArr = []
    for i in arr:
        if type(i) is list:
            resultArr.extend(flatten(i))
        else:
            resultArr.append(i)
    return resultArr


if __name__ == '__main__':
    print(flatten([1, 2, 3, [4, 5]]))
