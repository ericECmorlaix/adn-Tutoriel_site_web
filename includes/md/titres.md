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

??? tip "<a id='toc'></a>Titres, titre de page et table des matières automatique : ..."    

    - En pratique, un fichier MarkDown `source.md` du dossier `docs`
    ne doit comporter, au plus, qu'un titre de niveau 1
    qui peut potentiellement devenir le titre de la page web.
    De même pour un Notebook Jupyter `source.ipynb` du dossier `docs`.

    - A partir des titres de niveau 2, MkDocs génère automatiquement une table des matières pour naviguer dans la page courante.  
    La profondeur des sous-titres souhaités est réglable. Une profondeur fixée à la valeur 0 désactive l'affichage de la table des matières.

    !!! example ""  
        Pour cela, il faut activer dans le fichier `mkdocs.yml` l'extension 
        [toc]{target=_blank}
        (table of contents) en précisant les options souhaitées : plus petit niveau de titre à intégrer, ajout de lien vers les [ancres](#ancre) des titres,...

        Par exemple pour ce site :

        ``` yaml
        markdown_extensions:
            - toc:                          # Table des matières générée automatiquement à partir des titres du niveau 2
                permalink: "&num;"          # Ajoute un symbole lien hypertexte vers l'ancre du titre #le-titre 
                toc_depth: 4                # Limite de la profondeur d'inclusion des titres dans la table des matières        
        ```
    
<!-- 
## test profondeur 2
### test profondeur 3
#### test profondeur 4
##### test profondeur 5
###### test profondeur 6
 -->


      