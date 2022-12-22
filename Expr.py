class Expr:

    def __init__(self, expr):

        self.expr = expr

    def __str__(self):

        return str(self.expr)

    def toSQL(self):
        return self

    #does nothing as a regular expression doesnt need to be validated
    def validate():
        pass