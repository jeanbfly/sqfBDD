import Expr
import Tools, Bdd
import Excpt as e

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
        
        return self.expr.validate()

    def toSQL(self):
        return f'SELECT * FROM ({self.expr.toSQL()}) WHERE {self.condition}'

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
        
        exprSchema = self.expr.validate()
        reduceSchema = [i[0] for i in exprSchema]
        res = []
        for attr in self.listOfAttr:
            if attr not in reduceSchema:
                raise e.AttributeNameError(f'@project({self.listOfAttr})({self.expr})', attr, exprSchema)
            else:
                res.append(exprSchema[reduceSchema.index(attr)])
        return res

    def toSQL(self):

        return f'SELECT {",".join(self.listOfAttr)} FROM ({self.expr.toSQL()})'

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
        exprSchema1 = self.expr1.validate()
        exprSchema2 = self.expr2.validate()
        commonAttributes = []

        for attribut in exprSchema1:
            if attribut in exprSchema2:
                commonAttributes.append(attribut)
                exprSchema2.remove(attribut)

        if len(commonAttributes) == 0:
            raise e.InvalidExpressionError(f'@join({self.expr1}, {self.expr2}', self.expr1, exprSchema1, self.expr2, exprSchema2)

        else:
            return exprSchema1 + exprSchema2

    def toSQL(self):

        return f'SELECT * FROM ({self.expr1.toSQL()}) NATURAL JOIN ({self.expr2.toSQL()})'

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

    def validate(self):

        exprSchema = self.expr.validate()
        self.reduceSchema = [i[0] for i in exprSchema]
        
        print(self.oldName)
        if not str(self.oldName) in self.reduceSchema:
            raise e.AttributeNameError(f'@rename({self.oldName}:{self.newName})({self.expr})', self.oldName, exprSchema)
        
        index = self.reduceSchema.index(str(self.oldName))
        exprSchema[index] = (self.newName, exprSchema[index][1])

        return exprSchema

    def toSQL(self):

        attributs = ''
        for index in range(len(self.reduceSchema)-1):
            if self.reduceSchema[index] == self.oldName:
                attributs += f'{self.oldName} AS {self.newName}, '
            else:
                attributs += f'{self.reduceSchema[index]}, '
        if self.reduceSchema[-1] == self.oldName:
                attributs += f'{self.oldName} AS {self.newName}'
        else:
            attributs += f'{self.reduceSchema[-1]}'

        return f'SELECT {attributs} FROM ({self.expr.toSQL()})'

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

        exprSchema1 =  self.expr1.validate()
        exprSchema2 = self.expr2.validate()

        if exprSchema1 != exprSchema2:
            raise e.InvalidExpressionError(f'@union({self.expr1}, {self.expr2}', self.expr1, exprSchema1, self.expr2, exprSchema2)
        
        return exprSchema1

    def toSQL(self):

        return f'SELECT * FROM ({self.expr1.toSQL()}) UNION SELECT * FROM ({self.expr2.toSQL()})'

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
        
        exprSchema1 =  self.expr1.validate()
        exprSchema2 = self.expr2.validate()

        if exprSchema1 != exprSchema2:
            raise e.InvalidExpressionError(f'@diff({self.expr1}, {self.expr2}', self.expr1, exprSchema1, self.expr2, exprSchema2)
        
        return exprSchema1

    def toSQL(self):

        return f'SELECT * FROM ({self.expr1.toSQL()}) EXCEPT SELECT * FROM ({self.expr2.toSQL()})'