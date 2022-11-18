import Expr

class Attr(Expr.Expr):
    """
        Class representing a basic attribute/relation
        attr -- a str object
    """
    def __init__(self, attr):

        if isinstance(attr, str):
            self.value = attr
        else:
            raise TypeError('\033[93m [E] : 1 paramètres nécessaire : 1 attributs/relation')

    def __str__(self):
        return self.value

class Condition:
    """
        Class representing a condition
        attr1, attr2 -- 2 attributes objects
        comparateur  -- a string comparator
    """
    def __init__(self, attr1, comparateur, attr2):

        if isinstance(attr1, Attr) and isinstance(attr2, Attr) and comparateur in ['=', '>', '<', '<>']:
            self.attr1 = attr1
            self.attr2 = attr2
            self.comparateur = comparateur
        else:
            raise TypeError('\033[93m [E] : 3 paramètres nécessaires : 2 attributs et un comparateur')

    def __str__(self):

        return f'{self.attr1} {self.comparateur} {self.attr2}'