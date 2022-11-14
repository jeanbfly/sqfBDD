from Tools import *
import Expr

def evalue(expr):
    
    if isinstance(expr, Attr):
        return str(expr)

if __name__ == '__main__':

    entry = input('sqf >> ')

    while entry != '@exit':

        print(evalue(entry))
        entry = input('sqf >> ')