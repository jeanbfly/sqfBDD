from Tools import *
import SPJRUD, Stack
import String as s
import Excpt as e
import Bdd

import sqlite3

def findCondition(expr):

    currentChar = next(expr)
    res = ''
    if currentChar in s.String.conditionOpen:
        currentChar = next(expr)
        while currentChar not in s.String.conditionClose and currentChar != None:
            res += currentChar
            currentChar = next(expr)
        currentChar = next(expr)

        if res == '':
            raise e.ConditionError('d\'arguments')

        condi = None
        params = None
        for comp in Condition.comparators:
            if res.find(comp) != -1:
                params = res.split(comp)
                condi = Condition(Attr(params[0]), comp, Attr(params[1]))
        if params != None and params[0] != '' and params[1] != '':
            return condi
        else:
            raise e.ConditionError('nombre d\'attribut conforme')
    else:
        raise e.ConditionError('condition conforme')

def findSplit(expr):

    currentChar = next(expr)
    currentChar = next(expr)
    left = ''
    leftStc = Stack.Stack()
    right = ''
    rightStc = Stack.Stack()

    ignore = False
    while currentChar != ',' and currentChar != None:

        if currentChar in s.String.subOpen:
            leftStc.push(currentChar)
            ignore = True
        elif currentChar in s.String.subClose:
            if leftStc.is_empty():
                raise e.FormatError('un des caractères')
            leftStc.pop()
        elif leftStc.is_empty():
            ignore = False
        elif currentChar == ',' and not ignore:
            break
        left += currentChar
        currentChar = next(expr)

    if currentChar == None:
        raise e.FormatError('un des arguments')

    currentChar = next(expr)

    if left == '':
        raise e.FormatError('l\'expression gauche')

    while currentChar != None:
        right += currentChar
        currentChar = next(expr)

    if right == '' or right in s.String.subClose:
        raise e.FormatError('l\'expression droite')

    return (s.String(left), s.String(right[:-1]))

def findStrings(expr):

    currentChar = next(expr)
    old = ''
    new = ''
    while currentChar != None:
        if currentChar in s.String.conditionOpen:
            currentChar = next(expr)
            while currentChar != ':' and currentChar != None:
                old += currentChar
                currentChar = next(expr)
            if old == '':
                raise e.FormatError('l\'ancien nom')
            if currentChar == None:
                raise e.FormatError('le séparateur \':\'')
            currentChar = next(expr)
            while currentChar not in s.String.conditionClose and currentChar != None:
                new += currentChar
                currentChar = next(expr)
            if new == '':
                raise e.FormatError('le nouveau nom')
            if currentChar == None:
                raise e.FormatError('}')
            currentChar = next(expr)
            return (Attr(old), Attr(new))

def findAttributes(expr):
    
    currentChar = next(expr)
    res = ''
    while currentChar != None:
        if currentChar in s.String.conditionOpen:
            currentChar = next(expr)
            while currentChar not in s.String.conditionClose and currentChar != None:
                res += currentChar
                currentChar = next(expr)
            if currentChar == None:
                raise e.FormatError('}')
            currentChar = next(expr)
          
            res = [Attr(i) for i in res.split(',')]
            return res
        currentChar = next(expr)
    raise e.FormatError('la liste d\'attributs')

def findSubRequest(expr):

    currentChar = next(expr)
    res = ''

    while currentChar != None:
        if currentChar in s.String.subOpen:

            currentChar = next(expr)
            stc = Stack.Stack()
            stc.push(currentChar)

            while currentChar != None:

                if stc.is_empty():
                    break
                elif currentChar in s.String.subOpen:
                    stc.push(currentChar)
                elif currentChar in s.String.subClose:
                    stc.pop()
                res += currentChar
                currentChar = next(expr)
            if res[:-1] == '':
                raise e.FormatError('la relation')
            return s.String(res[:-1])
        else:
            currentChar = next(expr)
    raise e.FormatError('la relation')

def evalue(expr):

    currentChar = next(expr)
    res = ''
    while currentChar != None:

        if currentChar == '@':
            while currentChar not in s.String.specials and currentChar != None:

                res += currentChar
                currentChar = next(expr)

            match res:
                case '@select':
                    expression = SPJRUD.Select(findCondition(expr.toFinal()), evalue(findSubRequest(expr.toFinal())))
                case '@project':
                    expression = SPJRUD.Project(findAttributes(expr.toFinal()), evalue(findSubRequest(expr.toFinal())))
                case '@join':
                    left, right = findSplit(expr.toFinal())
                    expression = SPJRUD.Join(evalue(left), evalue(right))
                case '@rename':
                    old, new = findStrings(expr.toFinal())
                    expression = SPJRUD.Rename(old, new, evalue(findSubRequest(expr.toFinal())))
                case '@union':
                    left, right = findSplit(expr.toFinal())
                    expression = SPJRUD.Union(evalue(left), evalue(right))
                case '@diff':
                    left, right = findSplit(expr.toFinal())
                    expression = SPJRUD.Difference(evalue(left), evalue(right))
                case _:
                    raise e.CommandError(res)
            return expression
        else:
            res += currentChar
            currentChar = next(expr)
    return Attr(res)

if __name__ == '__main__':

    with Bdd.Bdd() as db:
        for i in db.getTables():
            if 'temp' in i:
                db.dropTable(i)
            if 'table3' in i:
                db.dropTable(i)

    indicator = 'sqf >> '
    entry = input(indicator)

    while entry != '@exit':
        if entry == '':
            pass
        elif entry == '@print':
            with Bdd.Bdd() as db:
                print(db)
        else:
            try:
                obj = evalue(s.String(entry))
                print('To SPJRUD :', obj)
                schema = obj.validate()

                with Bdd.Bdd() as bd:
                    a = obj.toSQL()
                    print('To sql :', a)
                    res = bd.execute(a)
                    print(res)
                    attributs = '('
                    values = ''
                    while True:
                        choice = input('Voulez-vous enregistrer ? Y-N : ').strip()
                        if choice.upper() == 'Y':
                            name = input('Quel nom voulez-vous donner à la table : ')
                            for index in range(len(schema)-1):
                                attributs += f'{schema[index][0]} {schema[index][1]}, '
                            attributs += f'{schema[-1][0]} {schema[-1][1]})'
                            print(attributs)
                            bd.createTable(name, attributs)
                            
                            for values in res:
                                insertion = '('
                                for column in range(len(values)-1):
                                    if schema[column][1] == 'TEXT':
                                        insertion += f'"{values[column]}", '
                                    else:
                                        insertion += f'{values[column]}, '
                                if schema[-1][1] == 'TEXT':
                                    insertion += f'"{values[-1]}")'
                                else:
                                    insertion += f'{values[-1]})'
                                print(insertion)
                                bd.insert(name, insertion)
                            for copieTable in Attr.allCopies:
                                bd.dropTable(copieTable)
                            break
                        elif choice.upper() == 'N':
                            for i in Attr.allCopies:
                                bd.dropTable(i)
                            break
                        else:
                            continue
            except Exception as o:
                print(o.with_traceback())
        entry = input(indicator)