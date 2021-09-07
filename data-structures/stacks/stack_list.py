#!python3

# stack implementation using python lists

class Stack():
    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return 'empty list'
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'empty list'
        return self.list[-1]

    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def delete(self):
        self.list = []


if __name__ == '__main__':
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    print(stack1.list)

    print(f'popped: {stack1.pop()}')
    print(stack1.list)

    # peek()
    print(f'last element: {stack1.peek()}')
    print(stack1.list)
