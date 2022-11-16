import Expr
import Tools

class Select(Expr.Expr):
    
    def __init__(self, condition, expr):

        if isinstance(condition, Tools.Condition) and isinstance(expr, Expr.Expr):
            self.condition = condition
            self.expr = expr
        else:
            raise TypeError

    def __str__(self):

        return f'Select({str(self.condition)}, {str(self.expr)})'

class Project(Expr.Expr):

    def __init__(self, listOfAttr, expr):

        if isinstance(listOfAttr, list) and isinstance(expr, Expr.Expr):
            for i in listOfAttr:
                if not isinstance(i, Tools.Attr):
                    raise TypeError
            self.listOfAttr = listOfAttr
            self.expr = expr
        else:
            raise TypeError

    def __str__(self):

        self.listOfAttr = [str(i) for i in self.listOfAttr]
        return f'Proj({str(self.listOfAttr)}, {str(self.expr)})'

class Join(Expr.Expr):
    
    def __init__(self, expr1, expr2):

        if isinstance(expr1, Expr.Expr) and isinstance(expr2, Expr.Expr):
            pass
        else:
            raise TypeError

class Rename(Expr.Expr):
    
    def __init__(self, oldName, newName):

        if isinstance(oldName, Tools.Attr) and isinstance(newName, Tools.Attr):
            pass
        else:
            raise TypeError

class Union(Expr.Expr):
    
    def __init__(self, expr1, expr2):

        if isinstance(expr1, Expr.Expr) and isinstance(expr2, Expr.Expr):
            pass
        else:
            raise TypeError