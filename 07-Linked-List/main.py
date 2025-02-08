from typing import List


class Node:
    def __init__(self, data: any) -> None:
        """
        A Linked List Node conatins two things
        1. data
        2. reference to the next node by default null
        """
        self.data: any = data
        self.next: None | Node = None


class LinkedList:
    def __init__(self) -> None:
        self.head: None | Node = None
        # self.tail: None | Node = None
        self.size: int = 0

    def insert_at_tail(self, data: any) -> Node:
        """
        This method insert element at end of the linked list
        Parameters:
        data (any): Data that will store into the node
        """
        temp = Node(data)

        if not self.head:
            self.head = temp
        else:
            headNode = self.head

            while headNode:
                headNode

        self.size += 1

    def insert_at_head(self, data: any) -> Node:
        temp = Node(data)
        if not self.head:
            self.head = temp


    def create_a_ll(self, nums: List[int]) -> Node:
        head_node = Node(nums[0])
        mv = head_node
        for i in range(1, len(nums)):
            new_node = Node(nums[i])
            mv.next = new_node
            mv = new_node

        return head_node

    @property
    def get_len(self):
        return self.size

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
ll.insert_at_tail(10)
ll.insert_at_tail(100)
ll.insert_at_tail(1000)
print(ll)
a = [4, 2, 5, 1]
k = ll.create_a_ll(a)
