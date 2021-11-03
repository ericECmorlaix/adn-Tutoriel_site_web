Sur son site, Franck CHAMBON présente très complètement l'ajout de [boutons](https://ens-fr.gitlab.io/mkdocs/markdown-mkdocs/#les-boutons){target=_blank} ;

Il y a également la référence officielle [buttons](https://squidfunk.github.io/mkdocs-material/reference/buttons/#buttons){target=_blank} ;

??? example "Exemple : ..."
    === "Rendu"
        [![envelope]{align=left width=40%} <br>Poser une question à l'auteur...
         :fontawesome-solid-paper-plane: ](mailto:eric.madec@ecmorlaix.fr
         ?subject=Le MarkDown de Mkdocs-Material&body=Votre question : ...
         ){ .md-button }

    === "MarkDown"
        ```md
        [![envelope]{align=left width=40%} <br>Poser une question à l'auteur...
         :fontawesome-solid-paper-plane: ](mailto:eric.madec@ecmorlaix.fr
         ?subject=Le MarkDown de Mkdocs-Material&body=Votre question : ...
         ){ .md-button }
        ```
    === "MarkDown bouton plein"
        ```md
        [![envelope]{align=left width=40%} <br>Poser une question à l'auteur...
         :fontawesome-solid-paper-plane: ](mailto:eric.madec@ecmorlaix.fr
         ?subject=Le MarkDown de Mkdocs-Material&body=Votre question : ...
         ){ .md-button .md-button--primary }
        ``` 
    === "Rendu bouton plein"
        [![envelope]{align=left width=40%} <br>Poser une question à l'auteur...
         :fontawesome-solid-paper-plane: ](mailto:eric.madec@ecmorlaix.fr
         ?subject=Le MarkDown de Mkdocs-Material&body=Votre question : ...
         ){ .md-button .md-button--primary }