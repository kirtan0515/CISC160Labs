from Stack_Interface import Stack_Interface
from exceptions import EmptyStackException
from Node import Node

class LinkedStack(Stack_Interface):

    # Constructor. Creates a new empty stack.
    def __init__(self):
       self._head = None
       self._length = 0

    # Adds value to the "top" of the stack. Values are inserted in a
    #   last-in-first-out fashion meaning the element returned by pop
    #   will be the last element added by push.
    def push(self, new_element):
        self._head = Node(new_element, self._head)
        self._length += 1

    # Removes and returns an element from "top" of the stack. Values are
    #   inserted in a last-in-first-out fashion meaning the element returned
    #   by pop will be the last element added by push.
    def pop(self):
        #I) Try to store the element at the top of the stack
        saved_element = self.peek()

        #II) Remove the top element in the stack
        self._head = self._head.get_next()

        #III) Adjust our length
        self._length -= 1

        #IV) Return the stored value            
        return saved_element


    # Returns an element from "top" of the stack. Values are
    #   inserted in a last-in-first-out fashion meaning the element returned
    #   by top will be the last element added by push.
    def peek(self):
        if len(self) > 0:
            return self._head.get_element()
        else:
            raise EmptyStackException("No elements in stack")


    # Returns the number of elements in the stack
    def __len__(self):
        return self._length
