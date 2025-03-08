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
        pass

    def insert_at_end(self, value: int) -> Node:
        pass

    def remove_from_start(self) -> Node:
        pass

    def remove_from_end(self) -> Node:
        pass

    def __str__(self):
        pass


dll = DoublyLinkedList()
