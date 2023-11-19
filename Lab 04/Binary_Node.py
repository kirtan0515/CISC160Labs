from Double_Node import DNode


class BinaryNode(DNode):

    def __init__(self, element, parent=None, left=None, right=None):
        super().__init__(element)
        self._element = element
        self._parent = parent
        self._left = left
        self._right = right

    def get_element(self):
        return self._element

    def get_parent(self):
        return self._parent

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def set_element(self, element):
        self._element = element

    def set_parent(self, parent):
        self._parent = parent

    def set_left(self, left):
        self._left = left

    def set_right(self, right):
        self._right = right

