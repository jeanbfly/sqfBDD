from Tools import *
import Expr, SPJRUD, Stack
import String as s
import Excpt as e

def findCondition(expr):

    currentChar = next(expr)
    res = ''
    if currentChar in s.String.conditionOpen:
        currentChar = next(expr)
        while currentChar not in s.String.conditionClose and currentChar != None:
            res += currentChar
            currentChar = next(expr)
        currentChar = next(expr)

        condi = None
        if res.find('=') != -1:
            params = res.split('=')
            condi = Condition(Attr(params[0]), '=', Attr(params[1]))
        elif res.find('<>') != -1:
            params = res.split('<>')
            condi = Condition(Attr(params[0]), '<>', Attr(params[1]))
        elif res.find('<') != -1:
            params = res.split('<')
            condi = Condition(Attr(params[0]), '<', Attr(params[1]))
        elif res.find('>') != -1:
            params = res.split('>')
            condi = Condition(Attr(params[0]), '>', Attr(params[1]))
        else:
            raise e.ConditionError('comparateur')

        if params[0] != '' or param[1] != '':
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
            leftStc.pop()
        elif leftStc.is_empty():
            ignore = False
        elif currentChar == ',' and not ignore:
            break
        left += currentChar
        currentChar = next(expr)

    currentChar = next(expr)

    while currentChar != None:
        right += currentChar
        currentChar = next(expr)

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
            currentChar = next(expr)
            while currentChar not in s.String.conditionClose and currentChar != None:
                new += currentChar
                currentChar = next(expr)
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
            currentChar = next(expr)

            return [Attr(i) for i in res.split(',')]

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
            return s.String(res[:-1])
        else:
            currentChar = next(expr)

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
                    return SPJRUD.Select(findCondition(expr.toFinal()), evalue(findSubRequest(expr.toFinal())))
                case '@project':
                    return SPJRUD.Project(findAttributes(expr.toFinal()), evalue(findSubRequest(expr.toFinal())))
                case '@join':
                    left, right = findSplit(expr.toFinal())
                    return SPJRUD.Join(evalue(left), evalue(right))
                case '@rename':
                    old, new = findStrings(expr.toFinal())
                    return SPJRUD.Rename(old, new, evalue(findSubRequest(expr.toFinal())))
                case '@union':
                    left, right = findSplit(expr.toFinal())
                    return SPJRUD.Union(evalue(left), evalue(right))
                case '@diff':
                    left, right = findSplit(expr.toFinal())
                    return SPJRUD.Difference(evalue(left), evalue(right))
                case _:
                    raise e.CommandError(res)
        else:
            res += currentChar
            currentChar = next(expr)
    return Attr(res)

if __name__ == '__main__':

    entry = input('sqf >> ')

    while entry != '@exit':

        print(evalue(s.String(entry)))
        entry = input('sqf >> ')