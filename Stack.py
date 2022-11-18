
class Stack: 
    """
        Class representing a stack pile
    """
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
    """
        method to check the correct balance of brackets
        expression -- a sequence of brackets
    """
    if len(expression) % 2 != 0:
        return False
    
    opening_brackets = set('([{') 
    pairs = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    stack = Stack()
    
    for bracket in expression:
  
        if bracket in opening_brackets:
            stack.push(bracket)
        else:
            popped_bracket = stack.pop()
            if (popped_bracket, bracket) not in pairs:
                return False
    
    return stack.is_empty()