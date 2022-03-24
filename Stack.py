class Stack:

    def __init__(self, values=[]):
        self.values = values.copy()

    def is_empty(self):
        return not self.values

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.values.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.values[-1]

    def size(self):
        return len(self.values)

    def __str__(self):
        return str(self.values)










