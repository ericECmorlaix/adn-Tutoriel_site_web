=== "MarkDown"
    ```md
    --8<-- "includes/md/lienIn.md"
    ```
=== "Rendu"
    --8<-- "includes/md/lienIn.md"

Parce que de longues adresses de liens dégradent la lisibilité du texte en mode édition de code,
MarkDown permet de définir des liens par référence.  
Dans ce cas, on définit tous les liens à un endroit du document,
en dehors du texte (généralement rassemblé),
avec la syntaxe :
```md
[référence]: adresse "info-bulle"
```
et au fil du texte on lie cette adresse par sa référence à un texte support
avec la syntaxe `:::md [texte][référence]` ou encore tout simplement `:::md  [référence]`.      
Cette solution offre aussi l'avantage de pouvoir partager la même adresse
par plusieurs liens en ne la définissant qu’une fois dans le document.

???+ example "Pour exemple :"
    
     Le code MarkDown du paragraphe d'[introduction](./#introduction)
     comporte de nombreux liens de ce type,
      tous listés à la fin du texte de cette partie :
    ```md  hl_lines="39-47"
    --8<-- "includes/md/introductionM.md"
    ```

??? tip "Astuce pour faire ouvrir la page liée dans un nouvel onglet :"
    Par défaut, et contrairement à jupyter notebook, MkDocs ouvre la page web liée dans le même onglet que le document consulté.  
    L'extension [attr_list](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#attribute-lists){target="_blank"}
    activée dans le fichier `:::md mkdocs.yml` permet de préciser des valeurs personnalisées aux attributs HTML et CSS.  
    Ainsi la syntaxe `:::md {target="_blank"}` après le code d'un lien MarkDown modifie la valeur par défaut de l'attribut
    [`target`](https://www.w3schools.com/tags/att_a_target.asp){target="_blank"} afin d'ouvrir la page liée dans un nouvel onglet.  
    !!! summary "En résumé, la syntaxe complète en markdown d'un lien avec ce comportement est donc :"
        - en ligne dans le texte :
        ```md
        [mon texte support](https://monlien.com "mon info-bulle"){target="_blank"}
        ```
        - par référence :
            - dans le texte :
            ```md
            [référence]{target="_blank"}
            ```
            - hors du texte
            ```md
            [référence]: https://monlien.com "mon info-bulle"         
            ```
