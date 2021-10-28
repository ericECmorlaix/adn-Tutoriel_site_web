
### Liste à puces :
On commence par sauter une ligne, puis on place devant chaque item
      un caractère `-`, `+` ou `*`, suivi d'au moins d'un espace :

=== "MarkDown"
    ```markdown
    * Un élement de ma liste ;
    Une précision concernant cet élément...
    - Un autre élément de ma liste ;
        * Un élément de ma sous-liste ;
        * Un autre élément de ma sous-liste ;
    + Encore un autre élément de ma liste.
    ```
=== "Rendu"
    * Un élement de ma liste ;  
    Une précision concernant cet élément...
    - Un autre élément de ma liste ;
        * Un élément de ma sous-liste ;
        * Un autre élément de ma sous-liste ;
    + Encore un autre élément de ma liste.

### Liste ordonnées :
On procède de même, mais en précédant chaque item d'un nombre suivi d'un `.`,
 la numérotation se fait alors automatiquement indépendamment du nombre indiqué :
=== "MarkDown"
    ```markdown
    1. Le premier élement de ma liste ;  
    Une précision concernant cet élément...
    1. Le second élément de ma liste ;
        1. Le premier élément de ma sous-liste ;
        72. Le second élément de ma sous-liste ;
    1024. Le troisième élément de ma liste.
    ```
=== "Rendu"
    1. Le premier élement de ma liste ;  
    Une précision concernant cet élément...
    1. Le second élément de ma liste ;
        1. Le premier élément de ma sous-liste ;
        72. Le second élément de ma sous-liste ;
    1024. Le troisième élément de ma liste.

### Liste de taches :
On insère `[ ]` ou `[x]` devant chaque item
 d'une liste non ordonnée pour ajouter des cases à cocher  :
=== "MarkDown"
    ```markdown
    - [ ] Une tâche de ma todo liste ;
    - [x] Une autre tâche de ma todo liste ;
        - [x] une sous tâche de ma todo liste ;
        - [ ] une autre sous tâche de ma todo liste ;
    - [ ] Encore une autre tâche de ma todo liste.
    ```
=== "Rendu"
    - [ ] Une tâche de ma todo liste ;
    - [x] Une autre tâche de ma todo liste ;
        - [x] une sous tâche de ma todo liste ;
        - [ ] une autre sous tâche de ma todo liste ;
    - [ ] Encore une autre tâche de ma todo liste.

??? info 

    Il faut activer dans le fichier `mkdocs.yml` l'extension
     [pymdownx.tasklist](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#tasklist){ target=_blank}
      pour générer des listes de tâches avec des cases à cocher.
    
    ``` yaml
    markdown_extensions:
        - pymdownx.tasklist        
    ```
    
    
### Liste de description :
Sous la ligne d'un terme, on précède sa définition par un `:` suivi d'au moins un espace :
=== "MarkDown"
    ```markdown
    **Premier terme** :
    : Voici la définition du premier terme...

    **Second terme** :
    : Voici une définition pour le second terme...
    : Voici une autre définition pour le second terme...    
    ```
=== "Rendu"
    **Premier terme** :
    : Voici la définition du premier terme...

    **Second terme** :
    : Voici une définition pour le second terme...
    : Voici une autre définition pour le second terme...


??? info 

    Il faut activer dans le fichier `mkdocs.yml` l'extension
     [def_list](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#definition-lists){ target=_blank}
      pour générer des listes de définitions.

    ``` yaml
    markdown_extensions:
        - def_list        
    ```
