from PriorityQueue_Interface import PriorityQueue_Interface
from Node import Node


class Node:
    def __init__(self, key=None, value=None, next_node=None):
        self._key = key
        self._value = value
        self._next = next_node


class LinkedLinkedPQ(PriorityQueue_Interface):
    def __init__(self):
        # Initialize head and length
        self._head = None
        self.length = 0

    def add(self, key, value):
        # Create a new Node with key and value
        new_node = Node(key, value)
        # Handle case where queue is empty or new node has smaller key than head
        if self._head is None or key < self._head._key:
            new_node._next = self._head
            self._head = new_node
        else:
            # Traverse to find the correct position and insert the new node
            current = self._head
            while current._next is not None and key >= current._next._key:
                current = current._next
            new_node._next = current._next
            current._next = new_node
        self.length += 1

    def min(self):
        # Return tuple with key and value of the head (min element)
        if self._head is not None:
            return self._head._key, self._head._value

    def remove_min(self):
        # Return None if queue is empty
        if self._head is None:
            return None
        # Remove and return tuple with key and value of the min element
        min_node = self._head
        if min_node._next is None:
            self._head = None
        else:
            self._head = min_node._next

        self.length -= 1
        return min_node._key, min_node._value

    def __len__(self):
        # Return the length of the priority queue
        return self.length

    def is_empty(self):
        # Return True if the priority queue is empty, False otherwise
        return len(self) == 0


"""Using a linked list structure, I made a priority queue called LinkedLinkedPQ in this code. It was important to 
keep parts in higher priority based on their keys. I made sure that the order stayed the same when I added a new 
element. If the queue was empty or the new element had a smaller key than the current head, it became the new head; 
otherwise, I found the correct position in the linked list to insert the new element. The min method returns a tuple 
with the smallest element's key and value, so we can see it without removing it. The remove_min method, on the other 
hand, gets rid of the tuple that has the key and value of the lowest element and returns it. It also updates the head 
of the linked list as needed. The class has ways to get the length of the queue and check if it is empty. It also has 
the correct interface for a priority queue. """
