## stack
class Stack: 
    def __init__(self): 
        self.elements = [] 
    
    def push(self, data): 
        self.elements.append(data) 
        return data 
        
    def pop(self): 
        return self.elements.pop() 
    
    def peek(self): 
        return self.elements[-1] 
        
    def is_empty(self): 
        return len(self.elements) == 0

def balance_check(expression):
    ## checking the length of the expression
    if len(expression) % 2 != 0:
        ## not balanced if the length is odd
        return False
    
    ## for checking
    opening_brackets = set('([{') 
    pairs = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    
    ## stack initialization
    stack = Stack()
    
    ## iterating through the given expression
    for bracket in expression:

        ## checking whether the current bracket is opened or not        
        if bracket in opening_brackets:
            ## adding to the stack
            stack.push(bracket)
        else:
            ## popping out the last bracket from the stack
            popped_bracket = stack.pop()
        
            ## checking whether popped and current bracket pair
            if (popped_bracket, bracket) not in pairs:
                return False
    
    return stack.is_empty()

if __name__ == '__main__':
    if balance_check('[{test}]([test])'):
        print("Balanced")
    else:
        print("Not Balanced")
    
    if balance_check('{[}]([])'):
        print("Balanced")
    else:
        print("Not Balanced")