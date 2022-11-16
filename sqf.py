from Tools import *
import Expr, SPJRU, re

def evalue(expr):

    if re.search("^@select", expr) != None:
        match = re.search("{.*", expr[7:])
        condition = expr[7:][1:expr[7:].find('}')]
        
        condi = None
        if condition.find('=') != -1:
            params = condition.split('=')
            condi = Condition(Attr(params[0]), '=', Attr(params[1]))
        elif condition.find('<>') != -1:
            params = condition.split('<>')
            condi = Condition(Attr(params[0]), '<>', Attr(params[1]))
        elif condition.find('<') != -1:
            params = condition.split('<')
            condi = Condition(Attr(params[0]), '<', Attr(params[1]))
        elif condition.find('>') != -1:
            params = condition.split('>')
            condi = Condition(Attr(params[0]), '>', Attr(params[1]))
        else:
            pass

        suite = match.string[expr[7:].find('}')+1:]
        suite = suite[suite.find('(')+1:suite.rfind(')')]
        return SPJRU.Select(condi, evalue(suite))

    elif re.search("^@project", expr) != None:
        match = re.search("^{.*", expr[8:])
        listOfAttr = [Attr(i.replace("'", "")) for i in expr[8:][1:expr[8:].find("}")-1].split(",")]

        match = re.search("\(.*\)", expr)
        suite = expr[match.span()[0]+1:match.span()[1]-1]
        return SPJRU.Project(listOfAttr, evalue(suite))

    elif re.search("^@join", expr) != None:
        match = re.search("(.*", expr)
        left, right = match.split('&')
        return SPJRU.Join(evalue(left), evalue(right)) # @join(@project{'Personne', 'Age'} & expr2)

    elif re.search("^@union", expr) != None:
        pass
    elif re.search("^@rename", expr) != None:
        pass
    else:
        return Attr(expr)

if __name__ == '__main__':

    entry = input('sqf >> ')

    while entry != '@exit':

        print(evalue(entry))
        entry = input('sqf >> ')