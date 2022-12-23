import sqlite3, Excpt

class Bdd:

    def __init__(self, name='bdd.db'):

        self.name = name
        self.conn = None
        self.c = None

    def createTable(self, nameTable, listOfAttributes):

        try:
            self.c.execute(f'CREATE TABLE {nameTable} {listOfAttributes}')
        except sqlite3.OperationalError:
            raise Excpt.InitError('Table déjà créée')
        self.conn.commit()

    def dropTable(self, nameTable):

        self.c.execute(f'DROP TABLE {nameTable}')
        self.conn.commit()

    def copyTable(self, nameTable, newNameTable):

        self.c.execute(f'CREATE TABLE {newNameTable} AS SELECT * FROM {nameTable}')
        self.conn.commit()
        return newNameTable

    def getSchema(self, nameTable):

        return self.execute(f'PRAGMA table_info(\'{nameTable}\')')

    def getTable(self, nameTable):

        return self.c.execute(f"SELECT * FROM {nameTable}").fetchall()

    def getTables(self):

        return [str(i)[str(i).find('\'')+1:str(i).rfind('\'')] for i in self.c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]

    def printTable(self, nameTable):

        maxi = [len(str(i)) for i in range(len(self.getSchema(nameTable)))]
        schema = self.getSchema(nameTable)
        table = self.getTable(nameTable)

        for i in table:
            for j in range(len(i)):
                if len(str(i[j])) > maxi[j]:
                    maxi[j] = len(str(i[j]))

        for i in range(len(schema)):
            first, name, *other = schema[i]
            if len(name) > maxi[i]:
                maxi[i] = len(name)

        res = f'{nameTable} | '
        for i in range(len(schema)):
            first, name, *other = schema[i]
            res += f'{name}'.center(maxi[i], ' ')
            res += ' | '
        res += '\n'
        row = len(res)

        for i in range(len(table)):
            res += '―'*row
            res += '\n'
            res += ' '*(len(nameTable)+1)
            res += '|'
            for j in range(len(table[i])):
                res += f' {str(table[i][j])}'.center(maxi[j]+1, ' ')
                res += ' |'
            res += '\n'

        return res

    def insert(self, nameTable, values):

        self.c.execute(f"INSERT INTO {nameTable} VALUES {values}")
        self.conn.commit()

    def execute(self, sqlExpr):

        self.c.execute(sqlExpr)
        self.conn.commit()
        return self.c.fetchall()

    def __str__(self):

        return "\n".join([f'{self.printTable(i)}' for i in self.getTables()])

    def __enter__(self):

        self.conn = sqlite3.connect(self.name)
        self.c = self.conn.cursor()
        return self

    def __exit__(self, type, value, traceback):

        self.c.close()

if __name__ == '__main__':

    with Bdd() as db:
        
        for i in db.getTables():
            db.dropTable(i)
        print(db.createTable('EMPLOYEE', '(MATRICULE INT, SALAIRE INT, NAME TEXT, DEPARTEMENT TEXT)'))
        print(db.createTable('LOCATION', '(STREET TEXT, NUMBER INT, CITY TEXT)'))
        print(db.insert('EMPLOYEE', '(1, 2500, "Antoine", "Informatique")'))
        print(db.insert('EMPLOYEE', '(2, 2700, "Jean", "Comptabilité")'))
        print(db.insert('EMPLOYEE', '(3, 2650, "Julien", "Informatique")'))
        print(db.insert('EMPLOYEE', '(4, 2350, "Axel", "Comptabilité")'))
        print(db.insert('EMPLOYEE', '(5, 2400, "Louis", "Informatique")'))
        print(db.insert('EMPLOYEE', '(6, 2450, "Jules", "RH")'))
        print(db.insert('LOCATION', '("Rue de la clef", 20, "Mons")'))
        print(db.insert('LOCATION', '("Rue du hautbois", 34, "Mons")'))
        print(db.insert('LOCATION', '("Chaussée de cuesmes", 12, "Cuesmes")'))
        print(db.insert('LOCATION', '("Avenue de Gaule", 89, "Mons")'))

        print(db.createTable('STUDENT', '(MATRICULE INT, AGE INT, NAME TEXT)'))
        print(db.insert('STUDENT', '(1, 18, "Patrick")'))
        print(db.insert('STUDENT', '(2, 18, "Hervé")'))
        print(db.insert('STUDENT', '(3, 18, "Stéphane")'))
        print(db.insert('STUDENT', '(4, 18, "Marcel")'))
        print(db.insert('STUDENT', '(5, 18, "André")'))
        print(db.insert('STUDENT', '(6, 18, "Adrien")'))

        print(db.createTable('COURSELIST', '(ID_ARTICLE INT, PRIX INT, ACHETEUR TEXT)'))
        print(db.insert('COURSELIST', '(1, 13, "Patrick")'))
        print(db.insert('COURSELIST', '(2, 15, "Hervé")'))
        print(db.insert('COURSELIST', '(3, 17, "Stéphane")'))
        print(db.insert('COURSELIST', '(3, 17, "Patrick")'))
        print(db.insert('COURSELIST', '(3, 17, "Hervé")'))
        print(db.insert('COURSELIST', '(2, 15, "Stéphane")'))