from typing import List


class Node:
    """
    A Linked List Node contains two things
    1. data
    2. reference to the next node by default null
    """

    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: None | Node = None


class LinkedList:
    """
    linked list using only head node
    -> Aka it became a kind of stack implementation using the linked list
    """

    def __init__(self) -> None:
        """
        -> Constructor that initialize Liked list by head node by default it is set to the null or none along with here i am maintain the length of the linked list
        """
        self.head: None | Node = None
        self.__size: int = 0

    def insert_at_head(self, data: int) -> Node:
        """
        -> Insert the New Node at beginning of the Linked List
        -> Time Complexity O(1)
        """
        temp_node = Node(data)
        if not self.head:
            self.head = temp_node
        else:
            temp_node.next = self.head
            self.head = temp_node

        self.__size += 1

        return self.head

    def insert_at_tail(self, data: int) -> Node:
        """
        -> Insert the New Node at end of the Linked List
        -> Time Complexity O(n) because of need liner traverse
        """
        temp_node = Node(data)
        if not self.head:
            self.head = temp_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = temp_node

        self.__size += 1

        return self.head

    def insert_after_x_value(self, data: int, x: int) -> Node:
        """
        -> Method that add the node after the x value
        -> if x value not found than will end of the linked list
        -> if linked list is empty than x value will ignore
        """
        temp_node = Node(data)
        if not self.head:
            self.head = temp_node
        else:
            current = self.head
            while current.next:
                # print(current.data)
                if current.data == x:
                    temp_node.next = current.next
                    current.next = temp_node
                    break
                current = current.next

            current.next = temp_node
            self.__size += 1

        return self.head

    def insert_after_x_node(self, data: int, x: int = 0) -> Node:
        """
        -> Method that add the node after the x nodes
        -> if x value is greater than total number of nodes than new node will added at last
        -> if linked list is empty than x value will ignore
        """
        new_node = Node(data)
        count = 0
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                print(temp.data, count, x)
                if count == x:
                    print(temp.data, "MAtched")
                    new_node.next = temp.next
                    temp.next = new_node
                    break

                count += 1
                temp = temp.next

            temp.next = new_node

        self.__size += 1

        return self.head

    def create_a_ll(self, nums: List[int]) -> Node:
        pass

    @property
    def get_len(self):
        return self.__size

    def __str__(self):
        node = self.head
        s = ""
        while node:
            if node.next is None:
                s += f"{node.data} -> None."
            else:
                s += f"{node.data} -> "
            node = node.next

        return s


ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_head(100)
ll.insert_at_tail(1000)
ll.insert_at_tail(10000)
ll.insert_after_x_value(90, 1000)
ll.insert_after_x_node(900, 1)

print(ll)
a = [4, 2, 5, 1]
# k = ll.create_a_ll(a)
