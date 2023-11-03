from Stack_Interface import Stack
from Queue_Interface import Queue


'''
Function which takes a string and uses a stack to validate if the string,
    without any spaces or punctuation and normalized for capitalization, is a
    palindrome.
RETURNS: True if the string would be considered a palindrome, false otherwise
'''


def is_palindrome_stack(string):
    s = Stack()
    if len(string) == 0:
        return True

    string = "".join(char.lower() for char in string if char.isalnum())

    for char in string:
        s.push(char)

    for i in range(len(string) // 2):
        if s.pop() != string[len(string) - i - 1]:
            return False

    return True

'''
Function which takes a string and uses queues to validate if the string,
    without any spaces or punctuation and normalized for capitalization, is a
    palindrome.
RETURNS: True if the string would be considered a palindrome, false otherwise
'''


def is_palindrome_queue(string):
    q = Queue()

    if len(string) == 0:
        return True

    string = "".join(char.lower() for char in string if char.isalnum())

    for char in string:
        q.enqueue(char)

    while not q.is_empty():
        if q.dequeue() != string[0]:
            return False
        string = string[1:]
    return True


'''
Test code can go below if you want
'''
if __name__ == '__main__':
    pass
