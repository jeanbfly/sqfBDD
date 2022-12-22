import Expr
import Tools

class Select(Expr.Expr):
    """
        Class representing the Select command
        condition -- a condition object
        expr      -- a subRequest/relation, expression object
    """
    def __init__(self, condition, expr):

        if isinstance(condition, Tools.Condition) and isinstance(expr, Expr.Expr):
            self.condition = condition
            self.expr = expr
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaires : une condition et une expression\033[97m')

    def __str__(self):

        return f'Select({str(self.condition)}, {str(self.expr)})'

    def validate(self):
        if False:
            raise Excpt.ValidationError(f"{self.expr1} isn't compatible with {self.expr2}")
        self.expr1.validate()

    def toSQL(self):
        #self.expr.toSQL() ???
        return f'SELECT * FROM {self.expr} WHERE {self.condition}'

class Project(Expr.Expr):
    """
        Class representing the Project command
        condition -- a list of Attributes object
        expr      -- a subRequest/relation, expression object
    """
    def __init__(self, listOfAttr, expr):

        if isinstance(listOfAttr, list) and isinstance(expr, Expr.Expr):
            for i in listOfAttr:
                if not isinstance(i, Tools.Attr):
                    raise TypeError
            self.listOfAttr = listOfAttr
            self.expr = expr
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaires : une liste d\'attributs et une expression\033[97m')

    def __str__(self):

        self.listOfAttr = [str(i) for i in self.listOfAttr]
        return f'Proj({str(self.listOfAttr)}, {str(self.expr)})'

    def validate(self):
        if False:
            raise Excpt.ValidationError(f"{self.expr1} isn't compatible with {self.expr2}")
        self.expr1.validate()

    def toSQL(self):

        return f'SELECT {",".join(self.listOfAttr)} FROM {self.expr}'

class Join(Expr.Expr):
    """
        Class representing the Join command
        expr1, expr2 -- two subRequests/relations, expression object
    """
    def __init__(self, expr1, expr2):

        if isinstance(expr1, Expr.Expr) and isinstance(expr2, Expr.Expr):
            self.expr1 = expr1
            self.expr2 = expr2
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaire : 2 expressions\033[97m')

    def __str__(self):

        return f'{self.expr1} ⋈ {self.expr2}'

    def validate(self):
        if False:
            raise Excpt.ValidationError(f"{self.expr1} isn't compatible with {self.expr2}")
        self.expr1.validate()
        self.expr2.validate()

    def toSQL(self):

        return f'SELECT * FROM {self.expr1} NATURAL JOIN {self.expr2}'

class Rename(Expr.Expr):
    """
        Class representing the Rename command
        oldName -- the old name of the column
        newName -- the new name of the column
    """
    def __init__(self, oldName, newName, expr):

        if isinstance(oldName, Tools.Attr) and isinstance(newName, Tools.Attr) and isinstance(expr, Expr.Expr):
            self.oldName = oldName
            self.newName = newName
            self.expr = expr
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaire : un ancien nom et un nouveau nom\033[97m')

    def __str__(self):

        return f'Rename({self.oldName} -> {self.newName}, {str(self.expr)})'

    def toSQL(self):

        return f'ALTER TABLE {self.expr} RENAME COLUMN {self.oldName} TO {self.newName}'

class Union(Expr.Expr):
    """
        Class representing the Union command
        expr1, expr2 -- two subRequests/relations, expression object
    """
    def __init__(self, expr1, expr2):

        if isinstance(expr1, Expr.Expr) and isinstance(expr2, Expr.Expr):
            self.expr1 = expr1
            self.expr2 = expr2
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaire : 2 expressions\033[97m')

    def __str__(self):

        return f'{self.expr1} U {self.expr2}'

    def validate(self):
        if False:
            raise Excpt.ValidationError(f"{self.expr1} isn't compatible with {self.expr2}")
        self.expr1.validate()
        self.expr2.validate()

    def toSQL(self):

        return f'{self.expr1} UNION {self.expr2}'

class Difference(Expr.Expr):
    """
        Class representing the Union command
        expr1, expr2 -- two subRequests/relations, expression object
    """
    def __init__(self, expr1, expr2):

        if isinstance(expr1, Expr.Expr) and isinstance(expr2, Expr.Expr):
            self.expr1 = expr1
            self.expr2 = expr2
        else:
            raise TypeError('\033[93m [E] : 2 paramètres nécessaire : 2 expressions\033[97m')

    def __str__(self):

        return f'{self.expr1} - {self.expr2}'

    def validate(self):
        if False:
            raise Excpt.ValidationError(f"{self.expr1} isn't compatible with {self.expr2}")
        self.expr1.validate()
        self.expr2.validate()

    def toSQL(self):

        return f'SELECT * FROM {self.expr1} MINUS SELECT * FROM {self.expr2}'