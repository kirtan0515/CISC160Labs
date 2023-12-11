from Double_Node import DNode
from PriorityQueue_Interface import PriorityQueue_Interface


class DNode:
    def __init__(self, key, value):
        # Initialize a double node with key, value, previous, and next pointers
        self._data = (key, value)
        self._prev = None
        self._next = None


class LinkedHeapPQ(PriorityQueue_Interface):

    def __init__(self):
        # Initialize head, tail, and length
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def add(self, key, value):
        # Create a new double node with the given key and value
        new_node = DNode(key, value)
        # Handle case where the queue is empty
        if self._head is None:
            # If empty, set the new node as both the head and tail
            self._head = new_node
            self._tail = new_node
            new_node._prev = None
        else:
            # Insert the new node at the head of the queue
            new_node._next = self._head
            self._head._prev = new_node
            new_node._prev = None
            self._head = new_node
        # Handle case where the queue is empty
        self._length += 1
        # Perform up-heap operation to maintain heap property
        self._upheap(new_node)

    def min(self):
        # Check if the queue is empty
        # Return the data of the head (min element) if the queue is not empty
        if self._head is None:
            return None
        return self._head._data

    def remove_min(self):
        # Return None if the queue is empty
        if self._head is None:
            return None
        # Get the minimum node and update pointers
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
        # Return the data of the current node
        return self._data

    def is_empty(self):
        return self._head is None

    def _left_child(self, node):
        return node._next

    def _right_child(self, node):
        # Return the next node of the next node (right child), or None if it doesn't exist
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
        # Swap positions of two nodes in the priority queue
        # Update previous node's next pointer to node2 (if exists)
        if node1._prev is not None:
            node1._prev._next = node2
        else:
            self._head = node2
        # Update next node's previous pointer to node1 (if exists)
        if node2._next is not None:
            node2._next._prev = node1
        else:
            self._tail = node1
        # Swap node1 and node2
        node1._next, node2._next = node2._next, node1._next
        # Swap previous pointers of node1 and node2
        node1._prev, node2._prev = node2, node1

    def _upheap(self, node):
        # Move the node up the heap to maintain the heap property
        # Find the parent node
        parent = self._parent(node)
        # Check if there is a parent and if the node violates the heap property
        if parent is not None and self._has_parent(node) and node._data < parent._data:
            # Swap the node with its parent
            self._swap(node, parent)
            # Recursively move up the heap
            self._upheap(parent)

    def _downheap(self, node):
        # Move the node down the heap to maintain the heap property
        # Iterate while there is a left child
        while node._next:
            # Find the left child
            child = self._left_child(node)
            # Choose the larger child if there is a right child
            if node._next and node._next._data < child._data:
                child = node.next
            # Break if node satisfies heap property with its children
            if node._data < child._data:
                break
            # Swap data between the node and the chosen child
            node._data, child._data = child._data, node._data
            node = child


"""Using a doubly-linked list, I created a priority queue called LinkedHeapPQ in this Python code. A priority queue 
is like a special list where the most important things are at the top. I added a way to add new things to the queue 
while keeping it organized: add. The min method shows us the most important item without taking it off the list. The 
remove_min method, on the other hand, takes the most important item off the list and shows us it. This keeps the list 
organized.  I also made it possible to see if the list is empty, find out how long it is, and figure out how the 
things in it compare to each other. Each item is like a note with a key and a value. They are linked in an effective 
manner that makes the processes go efficiently. """