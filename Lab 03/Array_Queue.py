from Queue_Interface import Queue_Interface
from exceptions import EmptyQueueException


class ArrayQueue(Queue_Interface):
    DEFAULT_CAPACITY = 10

    # Constructor. Creates a new empty queue by creating the backing array at
    #   our default capacity, setting the length to 0, and setting the front
    #   of the circular array to 0 as well.
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._length = 0
        self._front = 0

    # Adds value to the end of the queue. Values are inserted in a
    #   first-in-first-out fashion meaning the element returned by dequeue
    #   will be the first element added by enqueue.
    def enqueue(self, new_element):
        # I) If our circular array is full, double the size of the backing array
        if self._length == len(self._data):
            self._resize_backing_array(2 * len(self._data))

        # II) Determine the position within the backing array where we are going
        #       to write our data (one past the end of the queue)
        new_end = (self._front + self._length) % len(self._data)

        # III) Write our new element into our backing array
        self._data[new_end] = new_element

        # IV) Increment the length of the queue
        self._length += 1

    # Removes and returns an element from the front of the queue. Values are inserted in a
    #   first-in-first-out fashion meaning the element returned by dequeue
    #   will be the first element added by .
    def dequeue(self):
        # I) Try to store the first element in the queue
        return_value = self.first()

        # II) Remove the first element from the front of the queue
        self._data[self._front] = None

        # III) Adjust the position of the front of our circular array
        self._front = (self._front + 1) % len(self._data)

        # IV) Adjust our length
        self._length -= 1

        # V) Return the stored value
        return return_value

    # Returns an element from the front of the queue. Values are inserted in a
    #   first-in-first-out fashion meaning the element returned by dequeue
    #   will be the first element added by .
    def first(self):
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        return self._data[self._front]

    # Returns the number of elements in the queue
    def __len__(self):
        return self._length

    # Helper method which resizes our manually created array with a newly
    #   specified size. The newly created array will take the currently
    #   array and reset it so that first element in the queue is it at index 0
    #   of the new array.
    def _resize_backing_array(self, new_size):
        # I) Store the old data that we're copying
        old_data = self._data

        # II) Overwrite our backing array with a new array of the new size
        self._data = [None] * new_size

        # III) Store the position of the front of the old circular array
        current_index = self._front

        # IV) For each element of our old circular array
        for i in range(self._length):
            # A) Copy the element from the old circular array into our new array
            self._data[i] = old_data[current_index]

            # B) Increment our current index but be sure to account for the
            #   circular array indexing
            current_index = (1 + current_index) % len(old_data)

        # V) Once all the data is copied into our new array, set the front to 0
        self._front = 0
