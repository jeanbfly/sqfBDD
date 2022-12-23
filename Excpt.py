class CommandError(Exception):
    """ 
        Class for command format Errors 
        msg -- The specified command
    """
    def __init__(self, msg):

        if isinstance(msg, str):
            self.msg = msg

        else:
            raise TypeError('\033[93m [E] : le message d\'erreur n\'est pas un string\033[97m')

    def __str__(self):

        return f'\033[93m [E] : CommandError : la commande {self.msg} n\'existe pas\033[97m'

class ConditionError(Exception):
    """ 
        Class for condition format Errors 
        msg -- The specified part of condition
    """
    def __init__(self, msg):

        if isinstance(msg, str):
            self.msg = msg
        else:
            raise TypeError('\033[93m [E] : le message d\'erreur n\'est pas un string\033[97m')

    def __str__(self):

        return f'\033[93m [E] : ConditionError : la condition ne possède pas de {self.msg}\033[97m'

class FormatError(Exception):
    """ 
        Class for format Errors 
        msg -- The specified part
    """
    def __init__(self, msg):

        if isinstance(msg, str):
            self.msg = msg
        else:
            raise TypeError('\033[93m [E] : le message d\'erreur n\'est pas un string\033[97m')

    def __str__(self):
        
        return f'\033[93m [E] : FormatError : {self.msg} est manquant\033[97m'

class InitError(Exception):
    """
        class
        msg
    """
    def __init__(self, msg):

        self.msg = msg

    def __str__(self):

        return f'\033[93m [E] : InitError : {self.msg} \033[97m'

class InvalidExpressionError(Exception):

    def __init__(self, totalExpr, expr1, schema1, expr2, schema2):

        self.totalExpr = totalExpr
        self.expr1 = expr1
        self.schema1 = schema1
        self.expr2 = expr2
        self.schema2 = schema2

    def __str__(self):

        return f'\033[93m [E] : Invalid expression, the expression :\n       {self.totalExpr}\n       is invalid because the schema of\n       {self.expr1} which is {self.schema1}\n       is not the same as the one from : {self.expr2}\n       which is {self.schema2} \033[97m'

class AttributeNameError(Exception):

    def __init__(self, totalExpr, attr, schema):
        self.totalExpr = totalExpr
        self.attr = attr
        self.schema = schema
    
    def __str__(self):
        return f'\033[93m [E] : Invalid expression, the expression :\n       {self.totalExpr}\n       is invalid because the attribute {self.attr}\n       is not in the schema : {self.schema}'