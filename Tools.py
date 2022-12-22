import Expr, Bdd

class Attr(Expr.Expr):
    """
        Class representing a basic attribute/relation
        attr -- a str object
    """
    allCopies = []

    def __init__(self, attr):

        if isinstance(attr, str):
            self.value = attr
        else:
            raise TypeError('\033[93m [E] : 1 paramètres nécessaire : 1 attributs/relation\033[97m')

    def __str__(self):
        return self.value

    def toSQL(self):

        return self.value

    def validate(self):

        with Bdd.Bdd() as bd:
            Attr.allCopies.append(bd.copyTable(self.value, f'temp{len(Attr.allCopies)+1}'))
            return [(i[1], i[2]) for i in bd.getSchema(Attr.allCopies[-1])]
        
class Condition:
    """
        Class representing a condition
        attr1, attr2 -- 2 attributes objects
        comparateur  -- a string comparator
    """

    comparators = ['=', '>', '<', '<>', '<=', '>=']

    def __init__(self, attr1, comparateur, attr2):

        if isinstance(attr1, Attr) and isinstance(attr2, Attr) and comparateur in Condition.comparators:
            self.attr1 = attr1
            self.attr2 = attr2
            self.comparateur = comparateur
        else:
            raise TypeError('\033[93m [E] : 3 paramètres nécessaires : 2 attributs et un comparateur\033[97m')

    def __str__(self):

        return f'{self.attr1} {self.comparateur} {self.attr2}'

    def toSQL(self):

        return self.__str__()