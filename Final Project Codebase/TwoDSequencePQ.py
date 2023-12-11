from PriorityQueue_Interface import PriorityQueue_Interface


class TwoDSequencePQ(PriorityQueue_Interface):
    def __init__(self):
        self.pq = []                        # priority queue
        self._length = 0                     # number of elements

    # Adds element to the queue
    def add(self, key, value):
        # Dynamically grow 2D list so priority index exists
        while len(self.pq) <= key:
            self.pq.append([])               # add new row to if needed
        #insert value at prioity level index
        self.pq[key].append(value)
        self._length += 1                    # Increment total length

    # Finds minimum and priority key
    def min(self):
        # Iterate over all priority lists
        for i, row in enumerate(self.pq):
            if row:
                return i, row[0]            # return the first element in the row
        return None, None                   # return None if there is no minimum

    def remove_min(self):                   # Removes and returns min element
        for i in range(len(self.pq)):       # Iterate through each row
            if self.pq[i]:
                item = self.pq[i].pop(0)   # Pop value from the priority queue
                self._length -= 1
                if not self.pq[i]:         # Check if row is now empty after removing item
                    del self.pq[i]         # Remove row
                return i, item             # Return key and popped min element
        return None, None                  # If no min item found, return None

    def is_empty(self):
        return self._length == 0

    def __len__(self):
        return self._length
