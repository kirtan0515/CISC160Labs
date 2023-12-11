from PriorityQueue_Interface import PriorityQueue_Interface
from Node import Node


class Node:
    def __init__(self, key=None, value=None, next_node=None):
        self._key = key
        self._value = value
        self._next = next_node


class LinkedLinkedPQ(PriorityQueue_Interface):
    def __init__(self):
        self._head = None
        self.length = 0

    def add(self, key, value):
        new_node = Node(key, value)
        if self._head is None or key < self._head._key:
            new_node._next = self._head
            self._head = new_node
        else:
            current = self._head
            while current._next is not None and key >= current._next._key:
                current = current._next
            new_node._next = current._next
            current._next = new_node
        self.length += 1

    def min(self):
        if self._head is not None:
            return self._head._key, self._head._value

    def remove_min(self):
        if self._head is None:
            return None

        min_node = self._head
        if min_node._next is None:
            self._head = None
        else:
            self._head = min_node._next

        self.length -= 1
        return min_node._key, min_node._value

    def __len__(self):
        return self.length

    def is_empty(self):
        return len(self) == 0
