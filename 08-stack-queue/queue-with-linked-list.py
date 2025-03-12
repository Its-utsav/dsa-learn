class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node | None = None


class Queue:
    """
    Linear Data sturucture that store data in linear order
    Insertion from one side and deletion from other side
    Follow principle of FIFO (First In First Out)
    """

    def __init__(self):
        self.front: None | Node = None
        self.rear: None | Node = None

    def enqueue(self, data: int):
        """
        Insert new node in Queue
        """
        new_node = Node(data)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            temp = self.rear

            while temp.next != None:
                temp = temp.next

            temp.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue Underflow")

        self.front = self.front.next

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue Underflow")

        return self.front.data

    def last(self):
        if self.isEmpty():
            raise Exception("Queue Underflow")

        return self.rear.data

    def isEmpty(self):
        return self.front is None

    def __str__(self):
        s = ""
        temp = self.front
        while temp:
            if temp.next is None:
                s += f"{temp.data} ."
            else:
                s += f"{temp.data} -> "
            temp = temp.next
        return s


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
# q.dequeue()
print(q.last())
print(q.peek())
print(q.isEmpty())
