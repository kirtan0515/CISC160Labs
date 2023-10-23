from Stack_Interface import Stack_Interface
from exceptions import EmptyStackException

class ArrayStack(Stack_Interface):
    DEFAULT_CAPACITY = 10

    # Constructor. Creates a new empty stack by creating the backing array at
    #   our default capacity and setting the length to 0.
    def __init__(self):
        self._data = [None] * ArrayStack.DEFAULT_CAPACITY
        self._length = 0


    # Adds value to the "top" of the stack. Values are inserted in a
    #   last-in-first-out fashion meaning the element returned by pop
    #   will be the last element added by push.
    def push(self, new_element):
        #I) If our array is full, double the size of the backing array
        if self._length == len(self._data):
            self._resize_backing_array(2 * len(self._data))

        #II) Write our new element into our backing array
        self._data[len(self)] = new_element

        #III) Increment the length of the queue
        self._length += 1



    # Removes and returns an element from "top" of the stack. Values are
    #   inserted in a last-in-first-out fashion meaning the element returned
    #   by pop will be the last element added by push.
    def pop(self):
        #I) Try to store the element at the top of the stack
        saved_element = self.peek()

        #II) Remove the top element in the stack
        self._data[len(self) - 1] = None

        #III) Adjust our length (if we are storing it in a variable)
        self._length -= 1

        #IV) Return the stored value            
        return saved_element


    # Returns an element from "top" of the stack. Values are
    #   inserted in a last-in-first-out fashion meaning the element returned
    #   by top will be the last element added by push.
    def peek(self):
        if len(self) > 0:
            return self._data[len(self)-1]
        else:
            raise EmptyStackException("No elements in stack")

    
    # Returns the number of elements in the queue
    def __len__(self):
        return self._length


    # Helper method which resizes our manually created array with a newly
    #   specified size.
    def _resize_backing_array(self, new_size):
        #I) Store the old data that we're copying
        old_data = self._data

        #II) Overwrite our backing array with a new array of the new size
        self._data = [None] * new_size

        #III) For each element of our old circular array
        for i in range(self._length):
            #A) Copy the element from the old circular array into our new array
            self._data[i] = old_data[i]
