# Projet Base de données I
## 1) Tutoriel :

Au lancement de l'application, une interface de commande vous propose de rentrer une commande. Deux types de commandes sont disponibles : 

- Commande de type control
- Commande de type SPJRUD

### 1.1) Commande de type Control :

- `@exit` permet de quitter l'application
- `@use $tableName` permet de sélectionner la table `$tableName`

### 1.2) Commande de type SPJRUD :

- `@select{$condition}($expr)` commande select avec `$condition`la condition de type (Attribut1 comparateur Attribut2) et `$expr` la relation/la sous-requête sur laquelle s'applique le select.
- `@project{$listOfAttributes}($expr)` commande project avec `$listOfAttributes`une liste d'attributs de type (Attribut1, Attribut2, Attribut3, ...) et `$expr` la relation/la sous-requête sur laquelle s'applique le project.
- `@join($Rel1, $Rel2)` commande join avec `$Rel1, $Rel2` deux relations/ sous-requêtes à joindre.
- `@rename{$oldName:$newName}($expr)` commande rename avec `$oldName` l'attribut qui doit changer de nom, `$newName`le nouveau nom de l'attribut et `$expr` la relation/la sous-requête sur laquelle s'applique le rename.
- `@union($Rel1, $Rel2)` commande union avec `$Rel1, $Rel2` deux relations/ sous-requêtes à unir.
- `@diff($Rel1, $Rel2)` commande difference avec `$Rel1, $Rel2` deux relations/ sous-requêtes à soustraire.

### 1.3) Autres:

Un système d'erreurs est prévu pour vous prévenir d'une erreur de syntaxe. 
Un système de TraceBack est prévu pour les erreurs lors de l'éxécution de la requête.
Enfin, à la fin d'une commande, vous avez la possibilié de sauvegarder le résultat
dans une nouvelle table.

## 2) Structure :

Le programme utilise le paradigme de la programmation orientée objet pour faciliter son
implémentation. 

### 2.1) SPJRUD :

les différentes opérations sont représentée chacune par une classe dans le fichier __SPJRUD.py__. Elles implémentent
un __constructeur__ qui vérifie la congruence des arguments, une méthode spéciale __str__
pour formater l'opération en String et une méthode __toSQL__ permettant de traduire la
commande en requête SQL. Cette dernière appel récursivement la méthode toSQL pour toutes
sous-requêtes. Toutes les classes héritent de la classe __Expr__ pour que l'on puisse les passer en argument des autres.

### 2.2) L'interpréteur :

Dans le fichier __sqf.py__ se trouve l'interpréteur de commandes. Le programme demande à l'utilisateur de rentrer une commande. Il l'analyse ensuite dans une fonction récursive  __evalue__ qui crée un objet en fonction de la commande rentrée. Si une sous-requête se situe dans cette requête, on appel de nouveau la fonction __evalue__ avec la chaine de caractère
de cette sous-requête et ainsi de suite jusqu'à la fin de la chaine de caractère. Les fonctions __findCondition__, __findSplit__, __findStrings__, __findAttributes__ et __findSubRequest__ permettent de parser la chaine de caractère pour en extraire des éléments précis ou soulever une exception lorsqu'une erreur de syntaxe est introduite

### 2.3) Base de données :

La classe __Bdd__ dans le fichier __Bdd.py__ permet de gérer les accès et modification de la base de donnée. Elle utilise 
les méthodes spéciales __enter__ et __exit__ pour pouvoir utiliser un gestionnaire de contexte lors de l'implémentation. 
Comme la connexion avec la base de donnée avec __sqlite3__ se fait via un flux, un gestionanire de contexte fait beaucoup de sens 
et permet une gestion facile et efficace de la base de donnée.

### 2.4) Structures de données :

On utilise une classe __Stack__ particulièrement dans la fonction __findSplit__ afin de séparer correctement deux expressions séparées par une virgule
sans prendre en compte les virgules présentent dans les sous-expressions. 

On utilise une classe __String__ pour redéfinir un itérateur, utilisé sur la chaine de carcatère rentrée par l'utilisateur. 
Une méthode __toFinal__ est également implémentée pour récupérer la fin de la chaine à partir de l'index actuel de l'itérateur. 
Les attributs statiques permettent de garder en mémoire les différents caractères/chaines de caractères que le programme peut 
rencontrer lors du parsage de la commande rentrée par l'utilisateur. 

On utilise une classe __condition__ pour représenter une condition avec un comparateur et deux opérandes. 
On utilise une classe __Attr__ pour définir une String. Il peut représenter à la fois le nom de la relation, le nom 
d'un attribut ou un autre nom. Cette classe hérite de Expr pour pouvoir être passé dans les arguments de la fonction evalue.

La commande rentrée par l'utilisateur est donc enregistrée dans une structure de données sous la forme de commande chainées à d'autres commandes. 
Nous pouvons représenter cette structure de données sous la forme d'une arborescence __AST__. Des commandes contiennent d'autres commandes et ainsi de suite.
Les terminaisons sont les structures de base __Attr__.
