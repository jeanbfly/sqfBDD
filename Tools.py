class Attr:

    def __init__(attr):

        if isinstance(attr, str):
            self.value = attr
        else:
            raise TypeError

    def __str__(self):

        return f'\'{self.value}\''

class Rel:

    def __init__(tableName):

        if isinstance(tableName, str):
            self.value = tableName
        else:
            raise TypeError

class Condition:

    def __init__(attr1, comparateur, attr2):

        if isinstance(attr1, Attr) and isinstance(attr2, Attr) and comparateur in ['=', '>', '<', '<>']:
            pass
        else:
            raise TypeError