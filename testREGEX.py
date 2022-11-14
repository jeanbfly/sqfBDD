import re

txt = "@project{\'Personne', 'Age\'}(\'DATA\')"
x = re.search("^@project", txt)

attributs = txt[x.span()[1]:]
x1 = re.search("^{.*\}", attributs)

attributs = [i.replace("'", "") for i in attributs[1:x1.span()[1]-1].split(",")]
print(attributs)

x = re.search("\(.*\)", txt)
seq = txt[x.span()[0]+1:x.span()[1]-1]
print(seq)