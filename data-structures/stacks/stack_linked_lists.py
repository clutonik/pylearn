#!python3

# Stack implemented using linked list

class StackNode():
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{str(self.data)}'


class Stack():
    def __init__(self, head=None):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __str__(self):
        nodes = []
        for node in self:
            nodes.append(node)

        return '\n'.join(map(str, nodes))

    def push(self, value: int):
        # Create node
        new_node = StackNode(data=value)

        # check if stack is empty
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node
        return

    def pop(self):
        if self.head is None:
            return

        current_node = self.head
        self.head = self.head.next

        return current_node.data

    def peek(self):
        if self.head is None:
            return

        return self.head

    def delete(self):
        self.head = None


if __name__ == '__main__':
    # Create Stack
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f'stack after pushing 3 elements: \n{stack}')
    print(f'popped: {stack.pop()}')
    print(f'updated stack:\n{stack}')
    print(f'peek(): {stack.peek()}')
