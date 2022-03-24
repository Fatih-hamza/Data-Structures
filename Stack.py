class Stack:

    def __init__(self, items=[]):
        self.items = items.copy()

    def is_empty(self):
        return not self.items

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)










