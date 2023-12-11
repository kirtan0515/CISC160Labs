from Double_Node import DNode
from PriorityQueue_Interface import PriorityQueue_Interface


class DNode:
    def __init__(self, key, value):
        self._data = (key, value)
        self._prev = None
        self._next = None


class LinkedHeapPQ(PriorityQueue_Interface):

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def add(self, key, value):
        new_node = DNode(key, value)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
            new_node._prev = None
        else:
            new_node._next = self._head
            self._head._prev = new_node
            new_node._prev = None
            self._head = new_node

        self._length += 1
        self._upheap(new_node)

    def min(self):
        if self._head is None:
            return None
        return self._head._data

    def remove_min(self):
        if self._head is None:
            return None
        min_node = self._head
        if self._head == self._tail:
            self._head = None
            self._tail = None
        elif self._head._next is None:
            self._head = None
        else:
            self._head = self._head._next
            self._head._prev = None
        if min_node._next:
            min_node._next._prev = None
        min_node._next = None
        if self._head:
            self._downheap(self._head)
        self._length -= 1
        return min_node._data

    def get_element(self):
        return self._data

    def is_empty(self):
        return self._head is None

    def _left_child(self, node):
        return node._next

    def _right_child(self, node):
        if node._next and node._next._next:
            return node._next._next
        return None

    def _parent(self, node):
        return node._prev

    def _has_parent(self, node):
        return node._prev is not None

    def _has_left(self, node):
        return node._next is not None

    def _has_right(self, node):
        return node._next._next is not None

    def _swap(self, node1, node2):
        if node1._prev is not None:
            node1._prev._next = node2
        else:
            self._head = node2

        if node2._next is not None:
            node2._next._prev = node1
        else:
            self._tail = node1

        node1._next, node2._next = node2._next, node1._next
        node1._prev, node2._prev = node2, node1

    def _upheap(self, node):
        parent = self._parent(node)
        if parent is not None and self._has_parent(node) and node._data < parent._data:
            self._swap(node, parent)
            self._upheap(parent)

    def _downheap(self, node):
        while node._next:
            child = self._left_child(node)

            if node._next and node._next._data < child._data:
                child = node.next

            if node._data < child._data:
                break

            node._data, child._data = child._data, node._data
            node = child
