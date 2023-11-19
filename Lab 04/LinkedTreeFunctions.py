# Kirtan Patel
# CISC 160-0
# Lab 04

from Binary_Node import BinaryNode

'''
Function which takes the root node of a sorted binary tree and an element.
  This function finds where in the binary tree that the element should be
  inserted (by using the algorithm provided in the lab booklet) so that the
  the tree stays in order.
PARAM:   root_node      The root of the linked list
PARAM:   new_element    The new element to be added into the list
RETURNS: The node at the root of the sorted binary tree.
'''


def insert(root_node: BinaryNode, new_element):
    # check if the tree is empty
    if root_node is None:
        # If empty, create a new node as root
        new_node = BinaryNode(new_element)
        return new_node
    # Start at root to traverse tree
    current = root_node
    # Loop to find the place to insert
    while True:
        # if the new element is less than the current element
        if new_element < current.get_element():
            parent = current
            current = current.get_left()
            if current is None:
                new_node = BinaryNode(new_element)
                new_node.set_parent(parent)
                parent.set_left(new_node)
                return root_node

        elif new_element > current.get_element():
            parent = current
            current = current.get_right()
            if current is None:
                new_node = BinaryNode(new_element)
                new_node.set_parent(parent)
                parent.set_right(new_node)
                return root_node
        # Return if duplicate
        else:
            return root_node
    # Return new root if inserted at root
    return new_node


'''
Function which takes the root node of a binary tree and prints the tree using
  inorder traversal. Inorder traversal prints the left subtree first, then
  prints the element in the current node, then prints the right subtree.
PARAM:   root_node      The root of the linked list
'''


def _print_tree_inorder(current_node):
    if current_node.get_left():
        _print_tree_inorder(current_node.get_left())

    print(current_node.get_element())

    if current_node.get_right() is not None:
        _print_tree_inorder(current_node.get_right())


'''
Function which takes the root node of a sorted binary tree and an element.
  This function searchs the tree for that element using an iterative
  methodology. As it goes, the function creates a path of element in the nodes
  traversed and returns that path at the end.
PARAM:   root_node      The root of the linked list
PARAM:   element        The element to be found in the tree
RETURNS: The path through the tree from the root to the element's node, or
           None if the element cannot be found in the tree.
'''


def iterative_path(root_node, element):
    path = []
    current = root_node

    while current:

        path.append(current.get_element())

        if element < current.get_element():
            current = current.get_left()

        elif element > current.get_element():
            current = current.get_right()

        else:
            return [node for node in path]

    return None



'''
Function which takes the root node of a sorted binary tree and an element.
  This function searchs the tree for that element using a recursive
  methodology. As it goes, the function creates a path of element in the nodes
  traversed and returns that path at the end.
PARAM:   root_node      The root of the linked list
PARAM:   element        The element to be found in the tree
RETURNS: The path through the tree from the root to the element's node, or
           None if the element cannot be found in the tree.
'''


def recursive_path(root_node: BinaryNode, element):
    # Initialize empty path list
    path = []

    # Recursive helper function
    def recurse(current_node: BinaryNode):

        # Base case if node is None
        if current_node is None:
            return False

        # Add current node to path list
        path.append(current_node.get_element())

        # Check if current node element matches target
        if element == current_node.get_element():
            return True

        # Recursively search left subtree if less than current
        if element < current_node.get_element() and recurse(current_node.get_left()):
            return True

        # Recursively search right subtree if greater than current
        if element > current_node.get_element() and recurse(current_node.get_right()):
            return True

        # Not found, remove node from path and return False
        path.pop()
        return False

    # Start recursion at root node
    if recurse(root_node):
        return [node for node in path]

    return None

'''
Test code can go below if you want
'''
if __name__ == '__main__':
    # Test code goes here
    pass
