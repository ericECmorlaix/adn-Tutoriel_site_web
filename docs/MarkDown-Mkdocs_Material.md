## Introduction :
=== "Rendu MarkDown"
    --8<-- "includes/md/introductionM.md"
=== "MarkDown"
    ```md
    --8<-- "includes/md/introductionM.md"
    ```
=== "HTML"
    ```html
    --8<-- "includes/md/introductionH.md"
    ```
=== "Rendu HTML :"
    --8<-- "includes/md/introductionH.md"

***
## Titres :
--8<-- "includes/md/titres.md"

***
## Corps de texte :
--8<-- "includes/md/texte.md"

***
## Lien :
--8<-- "includes/md/lien.md"

***
## Image :
--8<-- "includes/md/image.md"

***
## Trait horizontal :
--8<-- "includes/md/trait.md"

***
## Listes :
--8<-- "includes/md/liste.md"

***
## Citation :
--8<-- "includes/md/citation.md"

***
## Admonition :
--8<-- "includes/md/admonition.md"

***
## Codes :
--8<-- "includes/md/code.md"

***
## Toujours en construction...

![Illustration par unDrawn de la construction d'un mur](../images/undraw_building_blocks_n0nc.svg "Toujours en construction..." )

***
## Inclusion :

!!! faq "Quid : si on intègre le contenu d'un fichier MarkDown
     comme `index.md` en dehors d'un bloc de code ?"
    
    === "MarkDown"
        ```md
        --8<-- "docs/index.md" 
        ```        
    === "Rendu"
        --8<-- "docs/index.md"

***
## Volets :


     



***
## Caractères spéciaux :
### Echappement :

En dehors des structures de type code inline ou bloc de texte brut,
 il peut être nécessaire de mettre un caractère backslash `\` devant
  des caractères qui sinon sont interprétés en Markdown, HTML ou Latex.

??? example "Par exemple : ..."

    === "avec \"
        
        *Code :*

        ```markdown
        \#### Usage de l'antislash \\ :

        1\. \`code`  
        5\. <@\>  
        3\. !\[image](url "info"){ heigt=30 align=left}  
            
        \> \~\~barré~~, 
        \^\^souligné^^,
        \==surligné==, ...

        \- \__MarkDown__ ;  
        \+ <em\>HTML<em\> ;  
        \* \$\LaTeX$ ;
        ```
        
        *Rendu :*
    
        \#### Usage de l'antislash \\ :

        1\. \`code`  
        5\. <@\>  
        3\. !\[image](url "info"){ heigt=30 align=left}  
            
        \> \~\~barré~~, 
        \^\^souligné^^,
        \==surligné==, ...

        \- \__MarkDown__ ;  
        \+ <em\>HTML<em\> ;  
        \* \$\LaTeX$ ;

    === "sans \"

        *Code :*

        ```markdown
        #### Usage de l'antislash \ :

        1. `code`  
        5. <@>  
        3. ![image](url "info"){ heigt=30 align=left}

        > ~~barré~~,
        ^^souligné^^,
        ==surligné==, ...

        - __MarkDown__  
        + <em>HTML<em>  
        * $\LaTeX$  
        ```

        *Rendu :*

        #### Usage de l'antislash \ :

        1. `code`  
        5. <@>  
        3. ![image](url "info"){ heigt=30 align=left}

        > ~~barré~~,
        ^^souligné^^,
        ==surligné==, ...

        - __MarkDown__  
        + <em>HTML<em>  
        * $\LaTeX$  


    







### Icônes - Emojis :

<https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#icons-emojis>

### Touches :

***
## Tableau :

| WARNING: be careful to baz the quux before initializing the retro encabulator! |
| --- |

***
## 
***
## Ressources :

<https://www.jdbonjour.ch/cours/markdown-pandoc/>

<http://pageperso.lif.univ-mrs.fr/~edouard.thiel/mkdocs-et/>

<https://agea.github.io/tutorial.md/>

<https://learninglab.gitlabpages.inria.fr/mooc-rr/mooc-rr-ressources/module1/ressources/introduction_to_markdown_fr.html>

<https://www.markdownguide.org/>

<https://www.markdowntutorial.com/>

<https://www.ionos.fr/digitalguide/sites-internet/developpement-web/markdown/>

<https://docs.microsoft.com/en-us/contribute/markdown-reference>

<https://jupyterbook.org/content/myst.html> Markedly Structured Text


***




[2]: https://fr.wikipedia.org/wiki/Police_d%27%C3%A9criture_%C3%A0_chasse_fixe "Police d'écriture à chasse fixe"