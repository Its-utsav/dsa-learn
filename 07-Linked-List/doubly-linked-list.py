class Node:
    def __init__(self, value: int):
        self.prev: Node | None = None
        self.data = value
        self.next: Node | None = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.__size: int = 0

    def insert_at_start(self, value: int) -> Node:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.__size += 1
        return self.head

    def insert_at_end(self, value: int) -> Node:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head

            while temp.next != None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        self.__size += 1
        return self.head

    def remove_from_start(self) -> Node:
        if not self.head:
            raise Exception("Empty Linked List")

        temp = self.head
        self.head = temp.next
        temp.next.prev = self.head

    def remove_from_end(self) -> Node:
        if not self.head:
            raise Exception("Empty Linked List")

        temp = self.head

        while temp.next.next != None:
            temp = temp.next

        temp.next = None

    def __str__(self):
        s = "Null"
        temp = self.head
        while temp:
            s += "->"

            if temp.next == None:
                s += f"{temp.data} ."
            else:
                s += f"{temp.data}"
                s += "<-"

            temp = temp.next
        return s


dll = DoublyLinkedList()
dll.insert_at_start(10)
dll.insert_at_start(100)
dll.insert_at_end(20)
dll.insert_at_end(200)
dll.remove_from_end()
print(dll)
