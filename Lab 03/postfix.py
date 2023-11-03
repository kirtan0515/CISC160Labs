from Linked_Stack import LinkedStack
from exceptions import RPNError

'''
Function which takes a string and uses a stack to calculate the value of the
equation passed in. This equation is assumed to be in postfix/reverse Polish
notation.
RETURNS: The value that the equation evaluates to using postfix notation
'''


def postfix_calculator(expression):
    # I) For each token in the expression
    stack = LinkedStack()
    tokens = expression.split()

    # Check for an empty expression
    if not tokens:
        raise RPNError("Empty expression")

    for token in tokens:
        # A) If the token is a number
        if token.isdigit():
            # 1) Push the token on the stack
            stack.push(float(token))
        # B) Else, if the token is an operator
        else:
            # 1) Pop 2 tokens off the stack
            if stack.is_empty() or stack.peek() is None:
                raise RPNError("Not enough values on stack")
            value2 = stack.pop()
            value1 = stack.pop()
            # 2) Perform the operation on those 2 tokens (first token operator second token)
            if token == '+':
                result = value1 + value2
            elif token == '-':
                result = value1 - value2
            elif token == '*':
                result = value1 * value2
            elif token == '/':
                if value2 == 0:
                    raise RPNError("Divide by zero")
                result = value1 / value2
            # 3) Push the resulting token back onto the stack
            stack.push(result)

    # II) Return the 1 token remaining on the stack
    return stack.pop()


'''
Test code can go below if you want
'''
if __name__ == '__main__':
    pass
