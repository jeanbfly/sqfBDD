import Expr
import Tools

class Select(Expr.Expr):
    
    def __init__(condition, expr):

        if isinstance(condition, Tools.Condition) and isinstance(expr, Expr):
            self.condition = condition
            self.expr = expr
        else:
            raise TypeError

class Project(Expr.Expr):
    
    def __init__(listOfAttr, expr):
        
        if isinstance(listOfAttr, list) and isinstance(expr, Expr):
            for i in listOfAttr:
                if not isinstance(i, Tools.Attr):
                    raise TypeError
        else:
            raise TypeError

class Join(Expr.Expr):
    
    def __init__(expr1, expr2):

        if isinstance(expr1, Expr) and isinstance(expr2, Expr):
            pass
        else:
            raise TypeError

class Rename(Expr.Expr):
    
    def __init__(oldName, newName):

        if isinstance(oldName, Tools.Attr) and isinstance(newName, Tools.Attr):
            pass
        else:
            raise TypeError

class Union(Expr.Expr):
    
    def __init__(expr1, expr2):

        if isinstance(expr1, Expr) and isinstance(expr2, Expr):
            pass
        else:
            raise TypeError