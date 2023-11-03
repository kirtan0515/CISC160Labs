from abc import abstractmethod, ABC


class Stack_Interface(ABC):

    # Constructor. Creates a new empty stack.
    @abstractmethod
    def __init__(self):
        pass

    # Adds value to the "top" of the stack. Values are inserted in a
    #   last-in-first-out fashion meaning the element returned by pop
    #   will be the last element added by push
    @abstractmethod
    def push(self, value):
        pass

    # Removes and returns an element from "top" of the stack. Values are
    #   inserted in a last-in-first-out fashion meaning the element returned
    #   by pop will be the last element added by push
    @abstractmethod
    def pop(self):
        pass

    # Returns an element from "top" of the stack. Values are
    #   inserted in a last-in-first-out fashion meaning the element returned
    #   by top will be the last element added by push
    @abstractmethod
    def peek(self):
        pass

    # Returns the number of elements in the stack
    @abstractmethod
    def __len__(self):
        pass

    # Returns True if there are any elements in the stack, false otherwise
    def is_empty(self):
        return len(self) == 0


class Stack(Stack_Interface):
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek on empty stack")
        return self.items[-1]

    def __len__(self):
        return len(self.items)