from Double_Node import DNode


'''
Function which takes the head Node of two sorted linked lists and and
  combines them into a single, sorted doubly-linked list.
PARAM:   list1  The head of one sorted linked list
PARAM:   list2  The head of the other sorted linked list
RETURNS: The DNode at the head of the combined doubly-linked list.
'''


def combine_sorted(list1, list2):

    dummy = DNode(None)
    tail = dummy

    while list1 is not None and list2 is not None:

        if list1.get_element() < list2.get_element():
            dnode = DNode(list1.get_element())
            dnode.set_next(list1.get_next())

            tail.set_next(dnode)
            dnode.set_previous(tail)

            list1 = list1.get_next()

        else:
            dnode = DNode(list2.get_element())
            dnode.set_next(list2.get_next())

            tail.set_next(dnode)
            dnode.set_previous(tail)

            list2 = list2.get_next()

        tail = tail.get_next()

        while list1 is not None:
            dnode = DNode(list1.get_element())
            dnode.set_next(list1.get_next())

            tail.set_next(dnode)
            dnode.set_previous(tail)

            list1 = list1.get_next()
            tail = tail.get_next()

        while list2 is not None:
            dnode = DNode(list2.get_element())
            dnode.set_next(list2.get_next())

            tail.set_next(dnode)
            dnode.set_previous(tail)

            list2 = list2.get_next()
            tail = tail.get_next()

        return dummy.get_next()

'''
Test code can go below if you want
'''
if __name__ == '__main__':
    pass
