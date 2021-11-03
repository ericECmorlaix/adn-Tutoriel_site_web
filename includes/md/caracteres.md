
### Entités HTML :

Puisque MarkDown interprète quatre espaces laissés au début d'une ligne de texte
 comme une intention de généré l'affichage d'un bloc de code
 et supprime automatiquement les espaces supplémentaires laissés vide,
  une solution pour en introduire malgré tout est d'utiliser
  l'[entité HTML](https://developer.mozilla.org/fr/docs/Glossary/Entity){ target=_blank} `&nbsp;`
   correspondante à un espace insécable (`&NonBreakingSpace;`).

=== "MarkDown"
    ```md
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Une indentation de plus de quatre espaces,
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; et un vide laissé au milieu de cette ligne de texte.
    <!-- un vrai commentaire qui ne s'affichera pas contrairement au trois saut de lignes suivant-->
    &NewLine;&NewLine;&NewLine;
    &Tab;&Tab;&lt;&excl;&hyphen;&hyphen; Ceci est&mldr;&Tab;&Tab;&Tab;&Tab;&mldr;un faux commentaire &hyphen;&hyphen;&gt;
    ```
=== "Rendu"
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Une indentation de plus de quatre espaces,
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; et un vide laissé au milieu de cette ligne de texte.
    
    <!-- un vrai commentaire qui ne s'affichera pas-->
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;&excl;&hyphen;&hyphen; ceci est&mldr;
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&mldr;un faux commentaire &hyphen;&hyphen;&gt;

De la même façon tout autre [symbole ou entité HTML](https://dev.w3.org/html5/html-author/charref){ target=_blank} peut être introduit ainsi
au milieu du code MarkDown.

### Icônes - Emojis :

Il y a la référence officielle [icons-emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#icons-emojis){target=_blank} ;

Sur son site, Franck CHAMBON présente l'ajout d'[émojis et de caractères unicodes](https://ens-fr.gitlab.io/mkdocs/markdown-bases/#emojis-et-unicode){target=_blank} ;

### Touches :

Sur son site, Franck CHAMBON présente des exemples d'ajout de [touches](https://ens-fr.gitlab.io/mkdocs/markdown-mkdocs/#affichage-des-touches){target=_blank} ;

Il y a également la [documentation](https://facelessuser.github.io/pymdown-extensions/extensions/keys/){target=_blank} et la [référence](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#keys){target=_blank} officielles


### Echappement :

En dehors des structures de type code inline ou bloc de texte brut,
 il peut être nécessaire de mettre un caractère backslash `\` devant
  des caractères qui sinon sont interprétés en Markdown, HTML ou Latex.

??? example "Par exemple : ..."

    === "avec \"
        
        *Code :*

        ```markdown
        \##### Usage de l'antislash \\ :

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
    
        \##### Usage de l'antislash \\ :

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
        ##### Usage de l'antislash \ :

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

        ##### Usage de l'antislash \ :

        1. `code`  
        5. <@>  
        3. ![image](url "info"){ heigt=30 align=left}

        > ~~barré~~,
        ^^souligné^^,
        ==surligné==, ...

        - __MarkDown__  
        + <em>HTML<em>  
        * $\LaTeX$
