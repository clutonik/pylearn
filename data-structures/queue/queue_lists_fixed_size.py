#!python3

# queue using python lists with size limit

class Queue():
    def __init__(self, size):  # O(1)
        self.items = size * [None]
        self.size = size
        self.top = -1
        self.start = -1

    def __str__(self):
        return ' '.join(map(str, self.items))

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True

        return False

    def enqueue(self, value):
        # check if queue is already full
        if self.isFull():
            return False

        # check if top is at the last possible index
        # if yes, circle back to first index for insertion
        if self.top + 1 == self.size:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0

        self.items[self.top] = value
        return True

    def dequeue(self):
        # check if queue is already empty
        if self.isEmpty():
            return None

        value_to_remove = self.items[self.start]

        # if there is only 1 element i.e. self.start == self.top
        if self.start == self.top:
            self.start = self.top = -1
        elif self.start + 1 == self.size:
            self.start = 0
        else:
            self.start += 1

        self.items[self.start - 1] = None
        return value_to_remove


if __name__ == '__main__':
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)  # This will not be added

    print(queue)

    # dequeue an element
    print(queue.start)
    print(queue.dequeue())
    print(queue.top)
    print(queue)
