#!python3
# Recursion is a way of solving a problem by having a function calling itself

# Idea:
# Perform same operation multiple times with different inputs
# In every step we try smaller inputs to make problem smaller.
# Base condition is needed to stop the recursion, otherwise infinite loop will be formed.

# When to use Recursion?
# - If the problem can be broken down into similar sub problems
# - Trees and graphs are good candidates for recursion
# - Divide and conquer, greedy and dynamic programming use recursion

# How recursion works?
# - Recursive function calls itself
# - Recursive function calls itself until base condition is met

# Pros and Cons of Recursion
# Pros:
#   - Recursive functions are easy to implement and understand
#   - Recursive functions are easy to debug
# Cons:
#   - Recursive functions are not space efficient as they stay in stack memory
#   - Recursive functions are not time efficient and there is an additional overhead to push
#     and pop function calls from stack memory.

# Syntax:
"""
def function_name(parameters):
    # Base condition
    if condition:
        exit
    else:
        # Recursive call
        function_name(parameters)
"""


def openRussianDoll(doll: int):
    """
    This function will open russian doll.

    :param doll: int
    :return: NONE
    """
    # Just playing with custom error, I will never use this in Prod I promise :)
    assert doll > 0 and int(
        doll) == doll, "do you think I am dumb ? Pass a integer plz."
    # Base condition
    if doll == 1:
        print("All dolls have been opened")
    else:
        # Recursive call
        print("Opening doll with length:", doll)
        openRussianDoll(doll - 1)
        print(f"Doll with length {doll} is being closed again")


if __name__ == "__main__":
    """
    Output:
    ----------
    Opening doll with length: 4
    Opening doll with length: 3
    Opening doll with length: 2
    All dolls have been opened
    Doll with length 2 is being closed again
    Doll with length 3 is being closed again
    Doll with length 4 is being closed again

    This represents how recursive function calls are stored in a stack.
    Note: Last in first out.
    """
    openRussianDoll(4)
