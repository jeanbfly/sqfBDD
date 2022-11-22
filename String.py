
class String:
    """
        Class representing a String iterator
        string -- the string needed to be iterate
    """

    subOpen           =     ['(']
    subClose          =     [')']
    conditionOpen     =     ['{']
    conditionClose    =     ['}']
    specialsSub       =     subClose + subOpen
    specialsCondition =     conditionClose + conditionOpen
    specials          =     specialsCondition + specialsSub
    specialsOthers    =     ['=', '<', '>', '\'', '\"']
    commands          =     ['@SELECT', '@PROJECT'   , 
                             '@JOIN'  , '@UNION'     , 
                             '@RENAME', '@DIFFERENCE' ]

    def __init__(self, string):

        if isinstance(string, str):
            self.string = string
            self.index = -1
        else:
            raise TypeError('\033[93m [E] : 1 paramètre nécessaire : 1 string\033[97m')

    def __str__(self):

        return self.string

    def __next__(self):

        self.index += 1
        if self.index < len(self.string):
            if self.string[self.index] != ' ':
                return self.string[self.index]
            else:
                return self.__next__()
        else:
            return None

    def toFinal(self):

        return String(self.string[self.index:])