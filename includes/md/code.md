
### Code inline :
Comme vu dans le [Corps de texte](./#corps-de-texte),
 on peut afficher dans le flux d'un paragraphe,
  du code en caractères [`monospaces`][2]
   en l'encadrant entre deux `` ` ``
    que l'on peut obtenir par la combinaison
     de touches ++"AltGr"+"7"++ ou ++"Alt"+"96"++.

!!! note ""
    Si le codage renferme déjà une apostrophe inversée
     ( backtick, [accent grave](https://fr.wikipedia.org/wiki/Accent_grave){ target=_blank}),
     on peut précéder et terminer la zone de code de deux fois ce caractère.  
    Dans ce cas, MarkDown n’interprétera pas cette apostrophe inversée comme une balise.

    === "MarkDown"
        ```markdown
        Exemple : ``Ceci est du `code`.``
        ```
    === "Rendu"
        Exemple : ``Ceci est du `code`.``

!!! tip ""    
    La coloration syntaxique s'applique aussi sur du code en ligne, par exemple, `#!py for lettre in "Bonjour" :`, s'obtient en écrivant en markdown  ``#!md `#!python3 for lettre in "Bonjour" :` `` dans le flux du texte.

    Après le premier `` ` ``, on place un [shebang](https://fr.wikipedia.org/wiki/Shebang){ target=_blank} `#!` (ou `:::`) suivi d'un [nom court](https://pygments.org/docs/lexers/#pygments.lexers.python.PythonLexer){ target=_blank} désignant le langage utilisé.  Aussi, ici on aurait pu se contenter du nom court `py` qui correspont à `python3` par défaut, ainsi le code ``:::md `:::py for lettre in "Bonjour" :` `` produit le même résultat : `:::py for lettre in "Bonjour" :`.

    ??? info
        Pour la coloration syntaxique du code en ligne, il faut activer dans le fichier `mkdocs.yml` les extensions : 
        
        ```yaml
        markdown_extensions:
          - pymdownx.highlight
          - pymdownx.inlinehilite         
        ```

### Bloc de texte brut :
=== "MarkDown"
    ```markdown
    Pour produire un bloc de texte brut,
     il suffit de faire
      un **saut de ligne**
       et de précéder le code
        d'une tabulation équivalente
         à au moins **quatre espaces** :

        Ceci est un bloc de texte brut ;

        A l'intérieur de ce dernier,
        tous les retours à la ligne,


        sont considérés ;

        Tous les  espaces   laissés    vides     sont      conservés ;
            L'indentation est donc respectée ;
        
        De plus :
            - aucun caractère de balisage **MarkDown**, <HTML> ou $LaTeX$ n'est interprété ;
            + ![image](url "info"){ heigt=300 align=left} ...
            # tout le texte s'affiche en caractère monospace ;
       On sort simplement de ce bloc de texte brut en revenant à une indentation inférieure à 4 espaces.
    ```
=== "Rendu"
    Pour produire un bloc de texte brut,
     il suffit de faire
      un **saut de ligne**
       et de précéder le code
        d'une tabulation équivalente
         à au moins **quatre espaces** :

        Ceci est un bloc de texte brut ;

        A l'intérieur de ce dernier,
        tous les retours à la ligne,


        sont considérés ;

        Tous les  espaces   laissés    vides     sont      conservés ;
            L'indentation est donc respectée ;
        
        De plus :
            - aucun caractère de balisage **MarkDown**, <HTML> ou $LaTeX$ n'est interprété ;
            + ![image](url "info"){ heigt=300 align=left} ...
            # tout le texte s'affiche en caractère monospace ;
       On sort simplement de ce bloc de texte brut en revenant à une indentation inférieure à 4 espaces. 

!!! attention "Si + de 4 espaces d'indentation après une ligne vide => c'est du texte brut !"
***
### Bloc de code :

#### Coloré :

Une autre pratique pour produire des blocs de texte brut
 consiste à encadrer les lignes de code
  entre deux triplets d'apostrophes inversées (backtick, accent grave) ;

Aussi, si on précise après le premier triplet le nom court
 du langage informatique correspondant au contenu des lignes de code,
  une coloration syntaxique idoine s'applique :

!!! example "Exemple :"

    === "MarkDown sans langage"
        ````
        ```
        def ma_fonction(paramètres):
            ''' docstring '''
            # bloc d'instructions (optionnel)            
            return valeur
        ```
        ````
    === "Rendu texte brut"
        ```
        def ma_fonction(paramètres):
            ''' docstring '''
            # bloc d'instructions (optionnel)            
            return valeur
        ```
    
    === "MarkDown avec langage"
        ````
        ``` python
        def ma_fonction(paramètres):
            ''' docstring '''
            # bloc d'instructions (optionnel)            
            return valeur
        ```
        ````
    === "Rendu avec coloration"
        ``` python
        def ma_fonction(paramètres):
            ''' docstring '''
            # bloc d'instructions (optionnel)            
            return valeur
        ```
!!! tip ""
    La [liste des langages supportés](https://pygments.org/languages/){ target=_blank} est plutôt exhaustive. Aussi il est pratique d'utiliser la barre de recherche pour trouver un nom court correspondant au langage souhaité...

#### Numéroté, surligné :

Franck CHAMBON présente parfaitement les [différentes options](https://ens-fr.gitlab.io/mkdocs/markdown-mkdocs/#options-sur-les-blocs-de-code){ target=_blank} pour faire cela. Il s'appuie sur l'exemple de code utilisé dans la [référence mkdocs-material](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#adding-line-numbers){ target=_blank} à ce sujet :

!!! tip "Numérotation des lignes et marquage"
    - Il suffit d'ajouter `linenums="1"` (ou un autre nombre) pour faire débuter la numérotation.
    - Pour marquer des lignes en particulier, on utilise `hl_lines="<tranches et numéros>"`


!!! example "Exemples"
    === "Sans numérotation"
        !!! note "Entrée"
            ````
            ```python
            --8<--- "includes/py/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python
            --8<--- "includes/py/exemple.py"
            ```

    === "Numérotation classique"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1"
            --8<--- "includes/py/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1"
            --8<--- "includes/py/exemple.py"
            ```

    === "Numérotation décalée"
        !!! note "Entrée"
            ````markdown
            ```python linenums="42"
            --8<--- "includes/py/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="42"
            --8<--- "includes/py/exemple.py"
            ```

    === "Marquage d'une ligne"
        !!! note "Entrée"
            ````markdown
            ```python hl_lines="2"
            --8<--- "includes/py/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python hl_lines="2"
            --8<--- "includes/py/exemple.py"
            ```

    === "Marquage d'une ligne, avec numérotation"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1" hl_lines="2"
            --8<--- "includes/py/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1" hl_lines="2"
            --8<--- "includes/py/exemple.py"
            ```

    === "Marquage de lignes éparses"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1" hl_lines="2 5"
            --8<--- "includes/py/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1" hl_lines="2 5"
            --8<--- "includes/py/exemple.py"
            ```

    === "Marquage d'une tranche"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1" hl_lines="2-4"
            --8<--- "includes/py/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1" hl_lines="2-4"
            --8<--- "includes/py/exemple.py"
            ```

    === "Marquage lignes et tranches"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1" hl_lines="1 2 3-3 5-5"
            --8<--- "includes/py/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1" hl_lines="1 2 3-3 5-5"
            --8<--- "includes/py/exemple.py"
            ```
??? faq "Annoté ? ..."
    Cette [fonctionnalité](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#code-annotations){ target=_blank} est pour l'instant exclusivement réservée aux [insiders](https://squidfunk.github.io/mkdocs-material/insiders/){ target=_blank}...

??? info
    Pour permettre les fonctionnalités des [lignes et blocs de code](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/){ target=_blank} décrites ci-dessus,
     il faut activer dans le fichier `mkdocs.yml` les extensions :

    ```yaml
    markdown_extensions:
      - pymdownx.highlight
      - pymdownx.inlinehilite
      - pymdownx.superfences
      - pymdownx.snippets    
    ```

#### Intégré :
!!! bug inline end "Ne pas copier/coller"
    le code ci-contre
    sans enlever l'espace laissé volontairement
    après le nom du fichier.
    
    C'est un caractère d'échappement
    qui évite l'intégration effective
     du code contenu dans le fichier
      `:::md mkdocs.yml` ici :wink:
Pour afficher dans un bloc de code
 le contenu du fichier `mkdocs.yml`
  qui est situé à la racine du dépôt on écrirait :   
````md
```yaml
--8<-- "mkdocs.yml" 
```
````


```console
├── docs/
│   └── images/
│   │   └── undraw_Polaroid.svg
│   └── MarkDown-Mkdocs_Material.md
│   └── index.md
├── includes/
│   └── py/
│       └── exemple.py
└─ mkdocs.yml
```

??? example "Exemple 1 : un fichier MarkDown ..."
    Pour le fichier `index.md` du dossier `docs/`
     situé à la racine du dépôt :
    === "MarkDown"
        ````md
        ```md
        --8<-- "docs/index.md" 
        ```
        ````
    === "Rendu"
        ```md
        --8<-- "docs/index.md"
        ```
??? example "Exemple 2 : un fichier Python ..."
    Pour le fichier `exemple.py` du dossier `py/`
     situé dans le dossier `includes` qui est aussi, 
      comme le dossier `docs/`, à la racine du dépôt :
    === "MarkDown"
        ````md
        ```py
        --8<-- "includes/py/exemple.py" 
        ```
        ````
    === "Rendu"
        ```py
        --8<-- "includes/py/exemple.py"
        ```
??? example "Exemple 3 : un fichier SVG ..."
    Pour le fichier `undraw_Polaroid.svg` du dossier `images`
     situé le dossier `docs/` :
    === "MarkDown"
        ````md
        ```svg
        --8<-- "docs/images/undraw_Polaroid.svg" 
        ```
        ````
    === "Rendu"
        ```svg
        --8<-- "docs/images/undraw_Polaroid.svg"
        ```

??? info
    Pour permettre cette fonctionnalité d'intégration
     [de contenu externe](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#embedding-external-files){ target=_blank}
      décrite ci-dessus,
       il faut activer dans le fichier `mkdocs.yml` l'extension :

    ```yaml
    markdown_extensions:
      - pymdownx.snippets    
    ```