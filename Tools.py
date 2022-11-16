import Expr

class Attr(Expr.Expr):

    def __init__(self, attr):

        if isinstance(attr, str):
            self.value = attr
        else:
            raise TypeError

    def __str__(self):
        return self.value

class Rel:

    def __init__(self, tableName):

        if isinstance(tableName, str):
            self.value = tableName
        else:
            raise TypeError

class Condition:

    def __init__(self, attr1, comparateur, attr2):

        if isinstance(attr1, Attr) and isinstance(attr2, Attr) and comparateur in ['=', '>', '<', '<>']:
            self.attr1 = attr1
            self.attr2 = attr2
            self.comparateur = comparateur
        else:
            raise TypeError

    def __str__(self):

        return f'{self.attr1} {self.comparateur} {self.attr2}'