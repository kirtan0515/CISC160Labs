# Import statements go here


'''
Function which takes a string and uses a stack to calculate the value of the
equation passed in. This equation is assumed to be in postfix/reverse Polish
notation.
RETURNS: The value that the equation evaluates to using postfix notation
'''
def postfix_calculator(string):
    #I) For each token in the expression
    #    A) If the token is a number
    #        1) Push the token on the stack
    #    B) Else, if the token is an operator
    #        1) Pop 2 tokens off the stack
    #        2) Perform the operation on those 2 tokens (first token operator second token)
    #        3) Push the resulting token back onto the stack
    #II) Return the 1 token remaining on the stack


'''
Test code can go below if you want
'''
if __name__ == '__main__':
    #Test code goes here
