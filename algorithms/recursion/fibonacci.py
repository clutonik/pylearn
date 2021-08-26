#!python3

# Fibonacci sequence using recursion

# What is Fibonacci sequence?
# Fibonacci sequence is a sequence of numbers where each number
# is the sum of the two preceding numbers.
# e.g. 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,...

def fibonacci(n):
    """Return nth Fibonacci number."""
    assert n >= 0 and int(
        n) == n, 'n has to be greater than or equal to 0 and has to be an integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(5))
