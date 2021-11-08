<!-- === "Rendu"

    # Titre de niveau 1
    ## Titre de niveau 2
    ### Titre de niveau 3
    #### Titre de niveau 4
    ##### Titre de niveau 5
    ###### Titre de niveau 6
    ####### Il n'y a pas de titre de niveau 7  
-->
=== "MarkDown"

    ```markdown
    # Titre de niveau 1
    ## Titre de niveau 2
    ### Titre de niveau 3
    #### Titre de niveau 4
    ##### Titre de niveau 5
    ###### Titre de niveau 6
    ####### Il n'y a pas de titre de niveau 7
    ```

??? info "Autres solutions pour obtenir des titres de niveau 1 et 2 :"

    === "MarkDown"

        ```markdown
        Souligner avec des `=` produit un titre de niveau 1
        ===================================================

        Souligner avec des `-` produit un titre de niveau 2
        ---------------------------------------------------
        ```

    !!! note "Remarque :"
    
        Un seul `=` ou `-` suffirait.  
        Leur répétition permet de souligner ces titres
         également dans le code en mode édition.

??? tip "Titres, titre de page et table des matières automatique : ..."
    
    - En pratique, un fichier MarkDown `source.md` du dossier `docs`
    ne doit comporter, au plus, qu'un titre de niveau 1
    qui peut potentiellement devenir le titre de la page web.

    - A partir des titres de niveau 2 et jusqu'au niveau de sous-titres souhaités,
     on peut activer la création automatique d'une table des matières
      par page qui s'ajoute à la navigation principale.

    !!! example ""  
        Pour cela, il faut activer dans le fichier `mkdocs.yml` l'extension 
        [toc](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/?h=tit#table-of-contents){target=_blank}
        (table of contents) en précisant les options souhaitées...

        Par exemple pour ce site :

        ``` yaml
        markdown_extensions:
            - toc:                          # Table des matières générée automatiquement à partir des titres du niveau 2
                permalink: "&num;"          # Ajoute une ancre pour de potentiels liens hypertextes vers #le-titre 
                toc_depth: 4                # inclusion des titres jusqu'au niveau toc_depth        
        ```
    




      