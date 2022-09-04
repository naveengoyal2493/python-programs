from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, element):
        self.buffer.appendleft(element)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


queue = Queue()
for i in range(10):
    queue.enqueue(bin(i))

print(queue.size())