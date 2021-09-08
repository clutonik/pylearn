#!python3

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __str__(self):
        nodes = [node for node in self]
        nodes.append("None")
        return ' -> '.join(map(str, nodes))

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def enqueue(self, value: int):
        # create new node from value
        new_node = Node(data=value)
        # check if empty
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
        return

    def dequeue(self) -> Node:
        # check if empty
        if self.isEmpty():
            return None

        # remove a node from head
        first_node = self.head
        if self.head.data == self.tail.data:
            self.head = None
            self.tail = None
        else:
            self.head = first_node.next

        return first_node

    def peek(self):
        if self.isEmpty():
            return None

        return self.head.data

    def delete(self):
        self.head = None
        self.tail = None
        return


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue)

    print(f'removed: {queue.dequeue()}')
    print(f'removed: {queue.dequeue()}')
    print(f'removed: {queue.dequeue()}')
    print(f'removed: {queue.dequeue()}')
    print(f'queue after removal:\n{queue}')
