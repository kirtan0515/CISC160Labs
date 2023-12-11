from Binary_Node import BinaryNode
from PriorityQueue_Interface import PriorityQueue_Interface


class TreeHeapPQ(PriorityQueue_Interface):

    def __init__(self):
        self.root = None
        self._length = 0

    def add(self, key, value):
        #create a new node
        new_node = BinaryNode((key, value))

        if self.is_empty():
            self.root = new_node
        else:
            curr = self.root
            # Traverse tree to find spot for new node
            while True:
                if new_node.get_element() >= curr.get_element():
                    if curr.get_right():
                        curr = curr.get_right()
                    else:
                        # Insert as right child
                        curr.set_right(new_node)
                        break

                else:
                    if curr.get_left():
                        curr = curr.get_left()
                    else:
                        # Insert as left child
                        curr.set_left(new_node)
                        break

        self._length += 1

    def min(self):
        #check if the tree is empty
        if self.root:
            # If not empty, return element of root node
            # Since this is a min-heap, the smallest element is at the root
            return self.root.get_element()
        else:
            return None  # If empty tree, return None

    def remove_min(self):
        if self.is_empty():
            return None
        # save the reference to the min node
        min_node = self.root
        min_element = min_node.get_element()
        # root is the only node
        if self.root.get_left() is None and self.root.get_right() is None:
            self.root = None
        #root has right child
        elif self.root.get_right():
            #traverse to find the smallest node of the right subtree
            curr_parent = self.root
            curr = self.root.get_right()
            while curr.get_left():
                curr_parent = curr
                curr = curr.get_left()

            min_node.element = curr.get_element()
            #check if thecurrent node is the leaf
            if curr.get_right() is None and curr.get_left() is None:
                # Leaf node
                if curr_parent == min_node:
                    curr_parent.set_right(None)
                else:
                    curr_parent.set_left(None)

                curr.set_parent(None)

            elif curr.get_left() and curr.get_right():
                # Node with both left and right
                if curr_parent == min_node:
                    curr_parent.set_right(curr.get_left())
                else:
                    curr_parent.set_left(curr.get_left())

            elif curr.get_right():
                # Only right child
                if curr_parent == min_node:
                    curr_parent.set_right(curr.get_right())
                else:
                    curr_parent.set_left(curr.get_right())

            else:
                # Only left child
                if curr_parent == min_node:
                    curr_parent.set_right(None)
                else:
                    curr_parent.set_left(None)
        else:
            self.root = self.root.get_left()
        # Decrement size and return old min element
        self._length -= 1
        return min_element

    def is_empty(self):
        return self._length == 0

    def __len__(self):
        return self._length