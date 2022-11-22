# SQF command line
## Projet Base de données I

Au lancement de l'application, une interface de commande vous propose de rentrer une commande. Deux types de commandes sont disponibles : 

- Commande de type control
- Commande de type SPJRUD

## Commande de type Control :

- `@exit` permet de quitter l'application
- `@use $tableName` permet de sélectionner la table `$tableName`

## Commande de type SPJRUD :

- `@select{$condition}($expr)` commande select avec `$condition`la condition de type (Attribut1 comparateur Attribut2) et `$expr` la relation/la sous-requête sur laquelle s'applique le select.
- `@project{$listOfAttributes}($expr)` commande project avec `$listOfAttributes`une liste d'attributs de type (Attribut1, Attribut2, Attribut3, ...) et `$expr` la relation/la sous-requête sur laquelle s'applique le project.
- `@join($Rel1, $Rel2)` commande join avec `$Rel1, $Rel2` deux relations/ sous-requêtes à joindre.
- `@rename{$oldName:$newName}($expr)` commande rename avec `$oldName` l'attribut qui doit changer de nom, `$newName`le nouveau nom de l'attribut et `$expr` la relation/la sous-requête sur laquelle s'applique le rename.
- `@union($Rel1, $Rel2)` commande union avec `$Rel1, $Rel2` deux relations/ sous-requêtes à unir.
- `@diff($Rel1, $Rel2)` commande difference avec `$Rel1, $Rel2` deux relations/ sous-requêtes à soustraire.

## Autres:

Un système d'erreurs est prévu pour vous prévenir d'une erreur de syntaxe
