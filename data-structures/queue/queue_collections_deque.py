#!python3
# queue using collections.deque Class in python

from collections import deque

queue = deque(maxlen=3)
print(queue)

# Insert element at end
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# dequeue an element
print(f'removing: {queue.popleft()}')
print(queue)

# delete all elements
queue.clear()
print(queue)
