class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node | None = None


class Stack:
    def __init__(self):
        self.head: None | Node = None

    def push(self, data: int):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack underflow")

        self.head = self.head.next

    def peek(self) -> int:
        if self.isEmpty():
            raise Exception("Stack underflow")

        return self.head.data

    def isEmpty(self):
        return self.head is None

    def __str__(self) -> str:
        s = ""
        temp = self.head
        while temp:
            if temp.next is None:
                s += f" {temp.data} ."
            else:
                s += f"{temp.data} ->"

            temp = temp.next
        return s


st = Stack()
st.push(10)
st.push(100)
st.push(1000)
print(st)
st.pop()
print(st)
print(st.isEmpty())
