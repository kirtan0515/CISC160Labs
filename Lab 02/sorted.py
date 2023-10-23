from Node import Node

'''
Function which takes the head Node of a sorted linked list and an element.
  This function finds where in the linked list that the element should be
  inserted so that the linked list stays in order.
PARAM:   head_node      The head of the linked list
PARAM:   new_element    The new element to be added into the list
RETURNS: The node at the head of the linked list.
'''


def insert_sorted(head, element):
    new_node = Node(element)

    if head is None:
        new_node.set_next(None)
        return new_node

    curr = head
    prev = None

    while curr is not None and curr.get_element() < element:
        prev = curr
        curr = curr.get_next()

    if prev is None:
        new_node.set_next(head)
        head = new_node
    else:
        prev.set_next(new_node)
        new_node.set_next(curr)

    return head


'''
Test code can go below if you want
'''
if __name__ == '__main__':
    pass
