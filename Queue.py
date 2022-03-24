from collections import deque
# deque is like a list, except that it's optimized in terms of removing the first element
# which is useful for a Queue


class Queue:

    def __init__(self, values=[]):
        self.values = deque()
        for value in values: 
            dequeue.append(value)

    def is_empty(self):
        return not self.values

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.values.popleft()

    def peek(self):
        return self.values[0]

    def size(self):
        return len(self.values)

    def __str__(self):
        values = [element for element in self.values]
        return str(values)




