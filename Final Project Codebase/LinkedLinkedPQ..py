from PriorityQueue_Interface import PriorityQueue_Interface
from Node import Node


class LinkedLinkedPQ(PriorityQueue_Interface):
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, key, value):
        new_node = Node((key, value))
        if self.head is None or key < self.head.data[0]:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and key >= current.next.data[0]:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1

    def min(self):
        if self.head is None:
            raise KeyError("Priority queue is empty")
        return self.head.data

    def remove_min(self):
        if self.head is None:
            raise KeyError("Priority queue is empty")
        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return data

    def __len__(self):
        return self.length

    def is_empty(self):
        return len(self) == 0