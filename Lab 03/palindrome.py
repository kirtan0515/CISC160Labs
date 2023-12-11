

'''
Function which takes a string and uses a stack to validate if the string,
    without any spaces or punctuation and normalized for capitalization, is a
    palindrome.
RETURNS: True if the string would be considered a palindrome, false otherwise
'''


def is_palindrome_stack(string):
    if not isinstance(string, str) or len(string) <= 1:
        return True

    stack = []

    string = "".join(char.lower() for char in string if char.isalnum())

    for char in string:
        stack.append(char)

    while len(stack) > 1:
        if stack.pop() != stack[-1]:
            return False

    return True

'''
Function which takes a string and uses queues to validate if the string,
    without any spaces or punctuation and normalized for capitalization, is a
    palindrome.
RETURNS: True if the string would be considered a palindrome, false otherwise
'''


def is_palindrome_queue(string):
    queue = []

    string = ''.join(char.lower() for char in string if char.isalnum())

    for char in string:
        queue.insert(0, char)

    while len(queue) > 1:
        if queue.pop() != queue[-1]:
            return False

    return True


'''
Test code can go below if you want
'''
if __name__ == '__main__':
    pass
