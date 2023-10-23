from Queue_Interface import Queue_Interface
from exceptions import EmptyQueueException
from Node import Node

class LinkedQueue(Queue_Interface):

    # Constructor. Creates a new empty queue using a linked list.
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0


    # Adds value to the "tail" of the queue. Values are inserted in a
    #   first-in-first-out fashion meaning the element returned by dequeue
    #   will be the first element added by enqueue
    def enqueue(self, new_element):
        #I) If the length of the list is 0
        if len(self) == 0:
            #A) Create a new node that is both the head and tail of the queue
            self._head = self._tail = Node(new_element)
        #II) Else, there is at least 1 element in the queue
        else:
            #A) Create a new tail with the new element and update the tail
            self._tail.set_next(Node(new_element))
            self._tail = self._tail.get_next()
            

        #III) Increment the length of the queue
        self._length += 1


    # Removes and returns an element from "head" of the queue. Values are
    #   inserted in a first-in-first-out fashion meaning the element returned
    #   by dequeue will be the first element added by enqueue
    def dequeue(self):
        #I) Try to store the element at the front of the queue
        return_value = self.first()
        
        #II) Remove the first element in the queue
        self._head = self._head.get_next()

        #III) Adjust our length
        self._length -= 1

        #IV) If the queue is now empty, set the tail to None
        if self.is_empty():
            self._tail = None

        #V) Return the value
        return return_value


    # Returns an element from "head" of the queue. Values are
    #   inserted in a first-in-first-out fashion meaning the element returned
    #   by dequeue will be the first element added by enqueue
    def first(self):
        #I) If the queue is empty, throw an exception
        if self.is_empty():
            raise EmptyQueueException("No elements in queue")

        #II) Return the element at the top of the stack
        return self._head.get_element()


    # Returns the number of elements in the queue
    def __len__(self):
        return self._length
