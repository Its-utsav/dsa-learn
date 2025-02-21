from typing import List


class EmptyLinkedList(Exception):
    def __init__(self, msg: str = "Linked List is empty"):
        super().__init__(msg)


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

        Parameter:
            data (int) : node value
        """
        new_node = Node(data)
        count = 0
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                # print(temp.data, count, x)
                if count == x:
                    # print(temp.data, "MAtched")
                    new_node.next = temp.next
                    temp.next = new_node
                    break

                count += 1
                temp = temp.next

            temp.next = new_node

        self.__size += 1

        return self.head

    def delete_at_head(self) -> Node:
        """
        -> Delete a first node from linked list
        """
        if not self.head:
            raise EmptyLinkedList()

        if self.head.next:
            self.head = self.head.next
        else:
            raise EmptyLinkedList("Linked list contains only one node")

        self.__size -= 1
        return self.head

    def delete_from_tail(self) -> Node:
        """
        -> Delete last node from linked list
        Parameters:
            argument1 (none): Description of arg1

        """
        if not self.head:
            raise EmptyLinkedList()

        # reach at second last
        current = self.head

        while current.next.next:
            print(current.data)
            current = current.next
        current.next = None
        self.__size += 1
        return self.head

    def delete_as_per_value(self, num: int) -> Node:
        if not self.head:
            raise EmptyLinkedList()
        if num == self.head.data:
            return self.delete_at_head()

        current = self.head

        while current.next:
            if current.next.data == num:
                current.next = current.next.next
            else:
                current = current.next

        return self.head

    def delete_as_per_count(self, count: int) -> Node:
        """
        Remove node as per count index
        """
        if not self.head:
            raise EmptyLinkedList()

        if count >= self.__size or count == self.__size - 1:
            return self.delete_from_tail()

        temp_count = 0

        current = self.head

        while current:
            if count - 1 == temp_count:
                current.next = current.next.next
            temp_count += 1
            current = current.next

        self.__size += 1

        return self.head

    def remove_duplicates_from_sroted_list_i(self):
        """
        -> Leetcode 83
        -> travese the linked list check current node data with current node's next data
            -> if same than current node next will be current node next and its next node
            -> not same than maintain the nodes currnt node will be current node's next
        -> travese TC O(n)
        -> Space complexity O(1)
        """
        if not self.head:
            return self.head

        temp = self.head
        while temp and temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return self.head

    def is_node_Exists(self, value: int) -> bool:
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def create_a_ll(self, nums: List[int]) -> Node:
        """
        -> you are given an array and your task is create a new linked list with that array elements
        -> Time Complexity O(n)
        """
        self.head = Node(nums[0])
        current = self.head

        for i in range(1, len(nums)):
            new_node = Node(nums[i])
            current.next = new_node
            current = new_node

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
ll.insert_at_head(1)
ll.insert_at_tail(2)
ll.insert_at_tail(3)
ll.insert_at_tail(4)
ll.insert_at_tail(5)
# ll.insert_at_head(2)
# ll.insert_at_head(3)
# ll.insert_at_head(4)
# ll.insert_at_head(5)

# ll.insert_at_tail(1000)
# ll.insert_at_tail(10000)
# ll.insert_after_x_value(90, 1000)
# ll.insert_after_x_node(900, 1)

print(ll)
ll.delete_as_per_count(2)
print(ll)
# ll.create_a_ll([1, 2, 3, 4])
# ll.remove_duplicates_from_sroted_list_i()
# print(ll)
# a = [4, 2, 5, 1]
# k = ll.create_a_ll(a)
