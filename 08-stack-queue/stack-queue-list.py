class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)

    def print(self):
        print(self.stack)


stack = Stack()


class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, val):
        self.queue.insert(0, val)

    def pop(self):
        self.queue.pop(0)

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.queue)

    def print(self):
        print(self.queue)


queue = Queue()
queue.insert(10)

queue.pop()
print(queue.print())
