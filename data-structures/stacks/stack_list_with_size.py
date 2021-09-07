#!python3

# stack implemented using python list with size limit

class Stack():
    def __init__(self, size):
        self.size = size
        self.list = []

    def push(self, value):
        if len(self.list) == self.size:
            print(f'list full, could not insert {value}')
            return

        self.list.append(value)

    def __str__(self):
        return ' <- '.join(map(str, self.list))

    def pop(self):
        return self.list.pop()


if __name__ == '__main__':
    stack1 = Stack(5)
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    stack1.push(6)
    stack1.pop()
    print(stack1)
