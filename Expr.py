class Expr:

    def __init__(expr):

        self.expr = expr

    def __str__(self):

        return str(self.expr)

    def __sub__(self, other):

        if isinstance(self, Expr) and isinstance(other, Expr):
            pass
        else:
            raise TypeError