#!python3
# queue using collections.deque Class in python

from multiprocessing import Queue

queue = Queue(maxsize=3)
queue.put(1)
queue.put(2)
print(queue.get())
