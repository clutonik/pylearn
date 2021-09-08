#!python3

# using python lists to implement queues without size limit

class Queue(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(i) for i in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True

        return False

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.isEmpty():
            return False

        # O(n) time consuming as all elements will shift left
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]

    def delete(self):
        self.items = []


if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue)

    queue.dequeue()
    print(queue)

    print(f'first element: {queue.peek()}')
