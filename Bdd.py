import sqlite3, Excpt

class Bdd:

    def __init__(self, name='bdd.db'):

        self.name = name
        self.c = None

    def createTable(self, nameTable, listOfAttributes):

        try:
            self.c.execute(f'CREATE TABLE {nameTable} {listOfAttributes}')
        except sqlite3.OperationalError:
            raise Excpt.InitError('Table déjà crée')
        self.c.commit()

    def execute(sqlExpr):

        self.c.execute(sqlExpr)

    def __str__(self):

        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        e = self.c.fetchall()
        return str(e)

    def __enter__(self):

        conn = sqlite3.connect(self.name)
        self.c = conn.cursor()
        return self

    def __exit__(self, type, value, traceback):

        self.c.close()

if __name__ == '__main__':

    with Bdd() as db:

        #db.createTable('stocks', '(date text, trans text, symbol text, qty real, price real)')
        print(db)