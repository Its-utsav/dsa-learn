class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: None | Node = None


class CircularSinglyLinkedList:
    """Variation of Linked list where last node connect to the first node"""

    def __init__(self):
        self.head: Node | None = None
        self.__size: int = 0

    def insert_at_start(self, value: int) -> Node:
        new_node = Node(value)
        if self.head == None:
            # no linked list
            self.head = new_node
            new_node.next = self.head
        else:
            # Means we have already nodes
            # Go till where current node same as head node

            current = self.head

            while current.next != self.head:
                current = current.next

            new_node.next = self.head
            current.next = new_node
            self.head = new_node

        self.__size += 1
        return self.head

    def insert_at_end(self, value: int) -> Node:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            # reach at last node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

        self.__size += 1
        return self.head

    def remove_from_start(self) -> Node:
        temp = self.head
        if not self.head:
            raise Exception("Empty Linked list")

        if self.head == self.head.next:
            self.head = None
            self.__size -= 1
            return self.head

        while temp.next != self.head:
            temp = temp.next
        self.head = self.head.next
        temp.next = self.head
        self.__size -= 1
        return self.head

    def remove_from_end(self) -> Node:
        if not self.head:
            raise Exception("Empty Linked list")

        if self.head == self.head.next:
            self.head = None
            self.__size -= 1
            return
        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head
        self.__size -= 1
        return self.head

    @property
    def get_len(self):
        return self.__size

    def __str__(self):
        node = self.head
        s = ""
        while True:
            s += f"{node.data} ->"
            # print(node.data)
            node = node.next
            if node == self.head:
                s += " back ."
                break
        return s


cll = CircularSinglyLinkedList()

cll.insert_at_start(1)
cll.insert_at_start(2)
cll.insert_at_end(20)
cll.insert_at_end(200)
print(cll)
cll.remove_from_end()
print(cll)
