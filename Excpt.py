
class CommandError(Exception):
    
    def __init__(self, msg):

        if isinstance(msg, str):
            self.msg = msg

        else:
            raise TypeError('\033[93m [E] : le message d\'erreur n\'est pas un string')

    def __str__(self):

        return f'\033[93m [E] : CommandError : la commande {self.msg} n\'existe pas'

class ConditionError(Exception):

    def __init__(self, msg):

        if isinstance(msg, str):
            self.msg = msg
        else:
            raise TypeError('\033[93m [E] : le message d\'erreur n\'est pas un string')

    def __str__(self):

        return f'\033[93m [E] : CommandError : la condition ne possède pas de {self.msg}'