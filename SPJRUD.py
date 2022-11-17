import Expr
import Tools

class Select(Expr.Expr):
    
    def __init__(self, condition, expr):

        if isinstance(condition, Tools.Condition) and isinstance(expr, Expr.Expr):
            self.condition = condition
            self.expr = expr
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaires : une condition et une expression')

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
            raise TypeError('\033[93m [E] : 2 paramètres nécessaires : une liste d\'attributs et une expression')

    def __str__(self):

        self.listOfAttr = [str(i) for i in self.listOfAttr]
        return f'Proj({str(self.listOfAttr)}, {str(self.expr)})'

class Join(Expr.Expr):
    
    def __init__(self, expr1, expr2):

        if isinstance(expr1, Expr.Expr) and isinstance(expr2, Expr.Expr):
            self.expr1 = expr1
            self.expr2 = expr2
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaire : 2 expressions')

    def __str__(self):

        return f'{self.expr1} ⋈ {self.expr2}'

class Rename(Expr.Expr):
    
    def __init__(self, oldName, newName, expr):

        if isinstance(oldName, Tools.Attr) and isinstance(newName, Tools.Attr) and isinstance(expr, Expr.Expr):
            self.oldName = oldName
            self.newName = newName
            self.expr = expr
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaire : un ancien nom et un nouveau nom')

    def __str__(self):

        return f'Rename({self.oldName} -> {self.newName}, {str(self.expr)})'

class Union(Expr.Expr):
    
    def __init__(self, expr1, expr2):

        if isinstance(expr1, Expr.Expr) and isinstance(expr2, Expr.Expr):
            self.expr1 = expr1
            self.expr2 = expr2
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaire : 2 expressions')

    def __str__(self):

        return f'{self.expr1} U {self.expr2}'

class Difference(Expr.Expr):

    def __init__(self, expr1, expr2):

        if isinstance(expr1, Expr.Expr) and isinstance(expr2, Expr.Expr):
            self.expr1 = expr1
            self.expr2 = expr2
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaire : 2 expressions')

    def __str__(self):

        return f'{self.expr1} - {self.expr2}'