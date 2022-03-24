from collections import deque
# deque is like a list, except that it's optimized in terms of removing the first element
# which is useful for a Queue


class Queue:

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.popleft()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        items = [element for element in self.items]
        return str(items)




