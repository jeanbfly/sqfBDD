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

class ValidationError(Exception):

    def __init__(self, msg):

        self.msg = msg

    def __str__(self):

        return f'\033[93m [E] : Validation Error : {self.msg} \033[97m'

class AttributeNameError(ValidationError):

    def __init__(self, msg):
        super().__init__(msg)
    
    def __str__(self):
        return super().__str__()

class AttributeTypeError(ValidationError):

    def __init__(self, msg):
        super().__init__(msg)
    
    def __str__(self):
        return super().__str__()