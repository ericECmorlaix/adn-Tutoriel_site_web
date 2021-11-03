Sur son site, Franck CHAMBON présente très complètement les [notes de bas de page](https://ens-fr.gitlab.io/mkdocs/markdown-mkdocs/#notes-de-bas-de-page){target=_blank} ;

Il y a également la référence officielle [footnotes](https://squidfunk.github.io/mkdocs-material/reference/footnotes/#footnotes){target=_blank} ;

??? example "Exemple : ..."
    === "MarkDown"
        ```md
        Note pour le marquage de révision[^critic]
        
        [^critic]:
            Le [marquage de révision](https://github.com/CriticMarkup/CriticMarkup-toolkit){target=_blank}
            s'applique aussi bien au rendu HTML qu'aux blocs de code et de texte brut.  
            Ceci est [une note de bas de page](#note-de-bas-de-page).
        ```
    === "Rendu"
        Note pour le marquage de révision[^critic]
        
        [^critic]:
            Le [marquage de révision](https://github.com/CriticMarkup/CriticMarkup-toolkit){target=_blank}
            s'applique aussi bien au rendu HTML qu'aux blocs de code et de texte brut.  
            Ceci est [une note de bas de page](#note-de-bas-de-page).
??? info 

    Il faut activer dans le fichier `mkdocs.yml` l'extension
     [footnotes](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#footnotes){ target=_blank}
      pour autoriser les notes de bas de page.

    ``` yaml
    markdown_extensions:
        - footnotes        
    ```