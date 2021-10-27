## Introduction :
=== "Rendu MarkDown"
    ![Logo]{ align=left }
    
    [**Markdown**][1]{target="_blank"} est un langage de description à balisage plus léger à coder que des balises HTML.  
    Son code est plus lisible dans l'éditeur,
     plus pratique et rapide pour rédiger et publier un document sur le Web.
    
    > Cliquer sur les onglets ci-dessus pour comparer les codes **MarkDown** et **HTML** qui produisent ce même **Rendu**

    Le principal défaut de MarkDown est son manque d'unification :
     il existe plusieurs versions de ce langage qui,
      à partir d'une syntaxe de base commune,
       possèdent d'autres éléments additionnels souvent très spécifiques...  
    
    Cependant il est de plus en plus utilisé :

    - incontournable sur [GitHub]{target="_blank"},
    - le site de partage d'informations [Reddit]{target="_blank"},
    - l'éditeur collaboratif en ligne [HedgeDoc]{target="_blank"},
    - les forums [Discourse]{target="_blank"},
     [Stack Overflow]{target="_blank"}...

    Mais c'est surtout le langage que nous utiliserons pour rédiger du texte enrichi
     dans nos [notebook jupyter][bn-md]{target="_blank"} 
     et nos pages web rédigées avec le MarkDown de Mkdocs tel que présenté ici.
    
    > **Remarque** :
    >
    > Vous avez toujours la possibilité de coder en HTML
     dans les `fichiers.md` de Mkdocs,
     comme dans les cellules MarkDown
      d'un [notebook jupyter][bn-html]{target="_blank"}...
    >
    > Par exemple, pour écrire des commentaires dans un code en MarkDown
    on utilise la syntaxe HTML : `<!-- mon commentaire -->`

    <!-- Ceci est un commentaire qui ne sera donc pas affiché
    Liste des liens pour l'introduction :
    -->
    [1]: https://fr.wikipedia.org/wiki/Markdown "Page Markdown sur Wikipedia" 
    [GitHub]: https://guides.github.com/features/mastering-markdown/ "Guide MarkDown de GitHub"
    [Reddit]: https://www.reddit.com/wiki/markdown "Guide MarkDown de Reddit"
    [HedgeDoc]: https://demo.hedgedoc.org/features?both "Page de demonstration du Markdown de HedgeDoc"
    [Discourse]: https://forum.digikey.com/t/an-unofficial-discourse-user-reference-guide/1125/4  "Référence MarkDown pour Discourse"
    [Stack Overflow]: https://stackoverflow.com/editing-help "Aide Markdown de Stack Overflow"
    [bn-md]: ../MarkDown-Le_BN_pour_rapporter "Notebook d'initiation au Markdown de Jupyter"
    [bn-html]: ../HTML-Le_BN_pour_multimedier "Notebook d'initiation au HTML de Jupyter"
    [Logo]: https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg "Logo du langage MarkDown"

=== "MarkDown"
    ```markdown
    ![Logo]{ align=left }
    
    [**Markdown**][1]{target="_blank"} est un langage de description à balisage plus léger à coder que des balises HTML.  
    Son code est plus lisible dans l'éditeur,
     plus pratique et rapide pour rédiger et publier un document sur le Web.
    
    > Cliquer sur les onglets ci-dessus pour comparer les codes **MarkDown** et **HTML** qui produisent ce même **Rendu**

    Le principal défaut de MarkDown est son manque d'unification :
     il existe plusieurs versions de ce langage qui,
      à partir d'une syntaxe de base commune,
       possèdent d'autres éléments additionnels souvent très spécifiques...  
    
    Cependant il est de plus en plus utilisé :

    - incontournable sur [GitHub]{target="_blank"},
    - le site de partage d'informations [Reddit]{target="_blank"},
    - l'éditeur collaboratif en ligne [HedgeDoc]{target="_blank"},
    - les forums [Discourse]{target="_blank"},
     [Stack Overflow]{target="_blank"}...

    Mais c'est surtout le langage que nous utiliserons pour rédiger du texte enrichi
     dans nos [notebook jupyter][bn-md]{target="_blank"} 
     et nos pages web rédigées avec le MarkDown de Mkdocs tel que présenté ici.
    
    > **Remarque** :
    >
    > Vous avez toujours la possibilité de coder en HTML
     dans les `fichiers.md` de Mkdocs,
     comme dans les cellules MarkDown
      d'un [notebook jupyter][bn-html]{target="_blank"}...
    >
    > Par exemple, pour écrire des commentaires dans un code en MarkDown
    on utilise la syntaxe HTML : `<!-- mon commentaire -->`

    <!-- Ceci est un commentaire qui ne sera donc pas affiché
    Liste des liens pour l'introduction :
    -->
    [1]: https://fr.wikipedia.org/wiki/Markdown "Page Markdown sur Wikipedia" 
    [GitHub]: https://guides.github.com/features/mastering-markdown/ "Guide MarkDown de GitHub"
    [Reddit]: https://www.reddit.com/wiki/markdown "Guide MarkDown de Reddit"
    [HedgeDoc]: https://demo.hedgedoc.org/features?both "Page de demonstration du Markdown de HedgeDoc"
    [Discourse]: https://forum.digikey.com/t/an-unofficial-discourse-user-reference-guide/1125/4  "Référence MarkDown pour Discourse"
    [Stack Overflow]: https://stackoverflow.com/editing-help "Aide Markdown de Stack Overflow"
    [bn-md]: ../MarkDown-Le_BN_pour_rapporter "Notebook d'initiation au Markdown de Jupyter"
    [bn-html]: ../HTML-Le_BN_pour_multimedier "Notebook d'initiation au HTML de Jupyter"
    [Logo]: https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg "Logo du langage MarkDown"
    ```
=== "HTML"
    ```HTML
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg" align="left" title="Logo du langage MarkDown" alt="Logo du langage MarkDown">
    
    <p>
        <a href="https://fr.wikipedia.org/wiki/Markdown" target="_blank" title="Page Markdown sur Wikipedia"><strong>Markdown</strong></a>
        est un langage de description à balisage plus léger à coder que des balises HTML.
        <br>
        Son code est plus lisible dans l'éditeur,
        plus pratique et rapide pour rédiger et publier un document sur le Web.
    </p>

    <blockquote>
        <p>
            Cliquer sur les onglets ci-dessus pour comparer les codes <strong>MarkDown</strong>
            et <strong>HTML</strong> qui produisent ce même <strong>Rendu</strong>
        </p>
    </blockquote>
    <p>
        Le principal défaut de MarkDown est son manque d'unification : 
        il existe plusieurs versions de ce langage qui,
        à partir d'une syntaxe de base commune,
        possèdent d'autres éléments additionnels souvent très spécifiques...  
    </p>
    <p>
        Cependant il est de plus en plus utilisé :
        <ul>
            <li>
                incontournable sur <a href="https://guides.github.com/features/mastering-markdown/" target="_blank" title="Guide MarkDown de GitHub">GitHub</a>,
            </li>
            <li>
                le site de partage d'informations <a href="https://www.reddit.com/wiki/markdown" target="_blank" title="Guide MarkDown de Reddit">Reddit</a>,
            </li>
            <li>
                l'éditeur collaboratif en ligne <a href="https://demo.hedgedoc.org/features?both" target="_blank" title="Page de demonstration du Markdown de HedgeDoc">HedgeDoc</a>,
            </li>
            <li>
                les forums <a href="https://forum.digikey.com/t/an-unofficial-discourse-user-reference-guide/1125/4" target="_blank" title="Référence MarkDown pour Discourse">Discourse</a>,
                <a href="https://stackoverflow.com/editing-help" target="_blank" title="Aide Markdown de Stack Overflow">Stack Overflow</a>...
            </li>
        </ul>
        Mais c'est surtout le langage que nous utiliserons pour rédiger du texte enrichi
        dans nos <a href="../MarkDown-Le_BN_pour_rapporter" target="_blank" title="Notebook d'initiation au Markdown de Jupyter">notebook jupyter</a> 
        et nos pages web rédigées avec le MarkDown de Mkdocs tel que présenté ici.
    </p>
    <blockquote>
        <p>
            <strong>Remarque</strong> :<br>
            Vous avez toujours la possibilité de coder en HTML
            dans les <code>fichiers.md</code> de Mkdocs,
            comme dans les cellules MarkDown d'un 
            <a href="../HTML-Le_BN_pour_multimedier" target="_blank" title="Notebook d'initiation au HTML de Jupyter">notebook jupyter</a>...
        </p>
        <p>
            Par exemple, pour écrire des commentaires dans un code en MarkDown
            on utilise la syntaxe HTML : <code>&lt;!-- mon commentaire --&gt;</code>
        </p>  
    </blockquote>
    <!-- Ceci est un commentaire qui ne sera donc pas affiché
    Liste des liens pour l'introduction :
    -->
    ```

=== " Rendu HTML :"
      <img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg" align="left" title="Logo du langage MarkDown" alt="Logo du langage MarkDown">
    
    <p>
        <a href="https://fr.wikipedia.org/wiki/Markdown" target="_blank" title="Page Markdown sur Wikipedia"><strong>Markdown</strong></a>
        est un langage de description à balisage plus léger à coder que des balises HTML.
        <br>
        Son code est plus lisible dans l'éditeur,
        plus pratique et rapide pour rédiger et publier un document sur le Web.
    </p>

    <blockquote>
        <p>
            Cliquer sur les onglets ci-dessus pour comparer les codes <strong>MarkDown</strong>
            et <strong>HTML</strong> qui produisent ce même <strong>Rendu</strong>
        </p>
    </blockquote>
    <p>
        Le principal défaut de MarkDown est son manque d'unification : 
        il existe plusieurs versions de ce langage qui,
        à partir d'une syntaxe de base commune,
        possèdent d'autres éléments additionnels souvent très spécifiques...  
    </p>
    <p>
        Cependant il est de plus en plus utilisé :
        <ul>
            <li>
                incontournable sur <a href="https://guides.github.com/features/mastering-markdown/" target="_blank" title="Guide MarkDown de GitHub">GitHub</a>,
            </li>
            <li>
                le site de partage d'informations <a href="https://www.reddit.com/wiki/markdown" target="_blank" title="Guide MarkDown de Reddit">Reddit</a>,
            </li>
            <li>
                l'éditeur collaboratif en ligne <a href="https://demo.hedgedoc.org/features?both" target="_blank" title="Page de demonstration du Markdown de HedgeDoc">HedgeDoc</a>,
            </li>
            <li>
                les forums <a href="https://forum.digikey.com/t/an-unofficial-discourse-user-reference-guide/1125/4" target="_blank" title="Référence MarkDown pour Discourse">Discourse</a>,
                <a href="https://stackoverflow.com/editing-help" target="_blank" title="Aide Markdown de Stack Overflow">Stack Overflow</a>...
            </li>
        </ul>
        Mais c'est surtout le langage que nous utiliserons pour rédiger du texte enrichi
        dans nos <a href="../MarkDown-Le_BN_pour_rapporter" target="_blank" title="Notebook d'initiation au Markdown de Jupyter">notebook jupyter</a> 
        et nos pages web rédigées avec le MarkDown de Mkdocs tel que présenté ici.
    </p>
    <blockquote>
        <p>
            <strong>Remarque</strong> :
        </p>
        <p>
            Vous avez toujours la possibilité de coder en HTML
            dans les <code>fichiers.md</code> de Mkdocs,
            comme dans les cellules MarkDown d'un 
            <a href="../HTML-Le_BN_pour_multimedier" target="_blank" title="Notebook d'initiation au HTML de Jupyter">notebook jupyter</a>...
        </p>
        <p>
            Par exemple, pour écrire des commentaires dans un code en MarkDown
            on utilise la syntaxe HTML : <code>&lt;!-- mon commentaire --&gt;</code>
        </p>  
    </blockquote>
    <!-- Ceci est un commentaire qui ne sera donc pas affiché
    Liste des liens pour l'introduction :
    -->
***
## Titres :

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
***
## Corps de texte :

=== "Rendu"

    On peut obtenir du _texte_ avec *simple emphase* rendu en *italique*,
     du __texte__ avec **forte emphase** rendu en **Gras**,
      du **_Texte_** à la fois en **gras** et en *italique*,
       du `code source` rendu en caractères [`monospaces`][2]{target="_blank"},
        du ~~texte barré~~  rendu avec une ligne en travers du texte,
         du ^^texte souligné^^  rendu avec une ligne en dessous du texte.
          On peut aussi mettre en ~indice~ ou en ^exposant^ et même ==surligné==.



    En regardant le code
    qui produit cette phrase,
    vous remarquerez que
    même
    si
    on
    fait 
    des
    retours
    à
    la
    ligne
    dans
    le
    code,
    le texte                s'affiche              sans rupture
    dans un seul            et                  même paragraphe
    et les espaces      laissés en trop         sont supprimés...

    Pour former des paragraphes séparés, il faut laisser une ligne vide entre eux.

    Pour forcer le retour à la ligne dans un paragraphe,  
    il faut ajouter deux espaces à la fin d'une ligne  
    avant de faire un retour à la ligne...


    [2]: https://fr.wikipedia.org/wiki/Police_d%27%C3%A9criture_%C3%A0_chasse_fixe "Police d'écriture à chasse fixe"

=== "MarkDown"
    ```markdown
    On peut obtenir du _texte_ avec *simple emphase* rendu en *italique*,
     du __texte__ avec **forte emphase** rendu en **Gras**,
      du **_Texte_** à la fois en **gras** et en *italique*,
       du `code source` rendu en caractères `monospaces`,
        du ~~texte barré~~  rendu avec une ligne en travers du texte,
         du ^^texte souligné^^  rendu avec une ligne en dessous du texte.
          On peut aussi mettre en ~indice~ ou en ^exposant^ et même ==surligné==.


    En regardant le code
    qui produit cette phrase,
    vous remarquerez que
    même
    si
    on
    fait 
    des
    retours
    à
    la
    ligne
    dans
    le
    code,
    le texte                s'affiche              sans rupture
    dans un seul            et                  même paragraphe
    et les espaces      laissés en trop         sont supprimés...

    Pour former des paragraphes séparés, il faut laisser une ligne vide entre eux.

    Pour forcer le retour à la ligne dans un paragraphe,  
    il faut ajouter deux espaces à la fin d'une ligne  
    avant de faire un retour à la ligne...
    ```

??? tip "Astuces pour obtenir au clavier les caractères spéciaux comme `~` ou `` ` ``: ..." 

    - Le [tilde](https://fr.wikipedia.org/wiki/Tilde) s'obtient avec la combinaison de touches ++"AltGr"+"2"++ ou ++"Alt"+"126"++ ;
    - L'[accent grave](https://fr.wikipedia.org/wiki/Accent_grave)) s'obtient avec la combinaison de touches ++"AltGr"+"7"++ ou ++"Alt"+"96"++ 



??? info 

    Il faut activer dans le fichier `mkdocs.yml` les extensions :

    ```yaml
    markdown_extensions:
        - pymdownx.caret
        - pymdownx.mark
        - pymdownx.tilde
    ```

    - [pymdownx.caret](https://facelessuser.github.io/pymdown-extensions/extensions/caret) pour `^^souligné^^` ou mettre en `^exposant^`;
    - [pymdownx.mark](https://facelessuser.github.io/pymdown-extensions/extensions/mark/) pour `==surligné==`;
    - [pymdownx.tilde](https://facelessuser.github.io/pymdown-extensions/extensions/tilde/) pour `~~barré~~` ou mettre en `~indice~`.


***
## Liens :
=== "Rendu"
    Le plus simple pour intégrer un lien hypertexte est de coller son adresse
     directement entre deux chevrons `<URL>` comme par exemple : <https://www.mkdocs.org/> ;
     De cette façon on peut aussi indiquer une adresse `<mail>` : <prenom.nom@ecmorlaix.fr>.

    La syntaxe `[texte](adresse "info-bulle")` lie une adresse à un texte support
     avec l'affichage optionnel d'une info-bulle au survol du lien :
      par exemple, voici [un lien relatif](./#introduction "Introduction au MarkDown de Mkdocs avec Material")
       vers l'introduction de cette page, et
        [un lien absolu]( https://ericecmorlaix.github.io/adn-Tutoriel_site_web/MarkDown-Mkdocs_Material/#introduction
         "Introduction au MarkDown de Mkdocs avec Material") qui renvoie au même titre.
    
    Parce que de longues adresses de liens dégradent la lisibilité du texte en mode édition de code,
     MarkDown permet de définir des liens par référence.  
      Dans ce cas, on définit tous les liens à un endroit du document,
       en dehors du texte (généralement rassemblé),
       avec la syntaxe `[référence]: adresse "info-bulle"`
       et au fil du texte on lie cette adresse par sa référence à un texte support
       avec la syntaxe `[texte][référence]` ou encore tout simplement `[référence]`.      
    Cette solution offre aussi l'avantage de pouvoir partager la même adresse
     par plusieurs liens en ne la définissant qu’une fois dans le document.

=== "MarkDown"
    ```markdown
    Le plus simple pour intégrer un lien hypertexte est de coller son adresse
     directement entre deux chevrons `<URL>` comme par exemple : <https://www.mkdocs.org/> ;
     De cette façon on peut aussi indiquer une adresse `<mail>` : <prenom.nom@ecmorlaix.fr>.

    La syntaxe `[texte](adresse "info-bulle")` lie une adresse à un texte support
     avec l'affichage optionnel d'une info-bulle au survol du lien :
      par exemple, voici [un lien relatif](./#introduction "Introduction au MarkDown de Mkdocs avec Material")
       vers l'introduction de cette page, et
        [un lien absolu]( https://ericecmorlaix.github.io/adn-Tutoriel_site_web/MarkDown-Mkdocs_Material/#introduction
         "Introduction au MarkDown de Mkdocs avec Material") qui renvoie au même titre.
    
    Parce que de longues adresses de liens dégradent la lisibilité du texte en mode édition de code,
     MarkDown permet de définir des liens par référence.  
      Dans ce cas, on définit tous les liens à un endroit du document,
       en dehors du texte (généralement rassemblé),
       avec la syntaxe `[référence]: adresse "info-bulle"`
       et au fil du texte on lie cette adresse par sa référence à un texte support
        avec la syntaxe `[texte][référence]` ou encore tout simplement `[référence]`.      
    Cette solution offre aussi l'avantage de pouvoir partager la même adresse
     par plusieurs liens en ne la définissant qu’une fois dans le document.    
    ```

!!! example "Pour exemple :"
    
     Le code MarkDown du paragraphe d'[introduction](./#introduction)
     comporte de nombreux liens de ce type,
      tous listés à la fin du texte de ce paragraphe... 


??? tip "Astuce pour faire ouvrir la page liée dans un nouvel onglet :"
    Par défaut, et contrairement à jupyter notebook, Mkdocs ouvre la page web liée dans le même onglet que le document consulté.  
    L'extension [attr_list](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#attribute-lists){target="_blank"}
    activée dans le fichier `mkdocs.yml` permet de préciser des valeurs personnalisées aux attributs HTML et CSS.  
    Ainsi la syntaxe `{target="_blank"}` après le code d'un lien MarkDown modifie la valeur par défaut de l'attribut
    [`target`](https://www.w3schools.com/tags/att_a_target.asp){target="_blank"} afin d'ouvrir la page liée dans un nouvel onglet.  
    !!! summary "En résumé, la syntaxe complète en markdown d'un lien avec ce comportement est donc :"
        ```markdown
        [mon texte support](https://monlien.com "mon info-bulle"){target="_blank"}
        ```
***
## Images :

La syntaxe pour les images est la même que pour les liens hypertextes,
 mais avec un `!` devant :
```markdown
![texte alternatif](adresse "info-bulle")
```
L'info-bulle optionnelle s'affichera au survol de l'image.

Il est important de bien choisir le [texte alternatif](http://www.pompage.net/traduction/Bien-utiliser-le-texte-alternatif){target="_blank"}
 qui s'affichera lorsque l'image n'est pas disponible,
 car il permet aussi l'accessibilité pour les non-voyants
  et apporte de la sémantique pour les moteurs de recherche...

L'adresse est l'URL relative ou absolue qui permet d'atteindre le fichier lié en cheminant dans l'arborescence du site web...

???+ example "Exemple :"

    === "Chemin relatif"
        ```markdown
        ![Illustration d'une photo](../images/undraw_Polaroid.svg "image via URL relative")
        ```
        ![Illustration d'une photo](../images/undraw_Polaroid.svg "image via URL relative")

    === "Chemin absolu"
        ```markdown
        ![Illustration d'une photo](https://ericecmorlaix.github.io/adn-Tutoriel_site_web/images/undraw_Polaroid.svg "image via URL absolue")
        ```
        ![Illustration d'une photo](https://ericecmorlaix.github.io/adn-Tutoriel_site_web/images/undraw_Polaroid.svg "image via URL absolue")

    Ici le fichier de l'image est placé dans un dossier nommé `images` lui même situé dans le dossier `docs` :
    ```
    ├── docs/
    │   └── images
    │   │   └── undraw_Polaroid.svg
    │   └── MarkDown-Mkdocs_Material.md
    │   └── index.md
    └─ mkdocs.yml
    ```
    Une fois déployé ce dossier `images` sera à la racine du site :
    ```  
    └── site
        ├── images
        │   └── undraw_Polaroid.svg
        ├── MarkDown-Mkdocs_Material
        │   ├── MarkDown-Mkdocs_Material.md
        │   ├── index.html
        ├── index.md
        ├── index.html
        ├── 404.html    
    ```     
    Alors, le chemin relatif vers cette image depuis la page web `index.html`
     située dans le dossier `MarkDown-Mkdocs_Material` et
      générée à partir du fichier `MarkDown-Mkdocs_Material.md`
       sera `../images/undraw_Polaroid.svg`
        car il faut sortir du dossier `MarkDown-Mkdocs_Material`
         pour pouvoir rentrer dans le dossier `images`.
    
    !!! note "Remarque :"
        Un chemin relatif vers cette même image depuis la page web `index.html`
        située à la racine du site et
         générée à partir du fichier `index.md`
          serait `./images/undraw_Polaroid.svg`...
    



??? tip "Pour gérer l'alignement et la taille d'une image :"

    L'extension [attr_list](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#attribute-lists){target="_blank"} 
        qui permet de préciser des valeurs personnalisées aux attributs HTML et CSS doit être activée dans le fichier `mkdocs.yml` :

    ```yaml
        markdown_extensions:
            - attr_list
    ```
    
  
    === "Rendu"
        ![Illustration d'une photo](../images/undraw_Polaroid.svg){width=20% align=right}  
        Ainsi le code MarkDown suivant :
        ````markdown
        ![Illustration d'une photo](../images/undraw_Polaroid.svg){width=20% align=right}
        ````
        placé au début du texte de ce paragraphe, produit l'affichage de l'image tel que ci-contre.
    === "MarkDown"
        ```markdown
        ![Illustration d'une photo](../images/undraw_Polaroid.svg){width=20% align=right}  
        Ainsi le code MarkDown suivant :
        ````markdown
        ![Illustration d'une photo](../images/undraw_Polaroid.svg){width=20% align=right}
        ````
        placé au début du texte de ce paragraphe, produit l'affichage de l'image tel que ci-contre.
        ```
??? tip "Une image cliquable, support d'un lien  :"

    Il suffit de remplacer le texte support d'un lien hypertexte par le code MarDown d'une image tel que :
    
    ```markdown
    [![texte alternatif](adresse)](adresse "info-bulle")
    ```
    === "Rendu"
        [![Illustration d'une photo](../images/undraw_Polaroid.svg){width=20%}](https://undraw.co/illustrations "Vers le site de unDraw"){target="_blank"}
    === "MarkDown"
        ```markdown
        [![Illustration d'une photo](../images/undraw_Polaroid.svg){width=20%}](https://undraw.co/illustrations "Vers le site de unDraw"){target="_blank"}
        ```





??? tip "Des solutions pour centrer une image :"

    ??? example "Solution 1 : un code HTML..."

        === "Code"
            ```html
            <figure>
                <img src="../images/undraw_Polaroid.svg" alt ="Illustration d'une photo" width="300" >
                <figcaption>
                    Un Polaroïd selon <a href="https://undraw.co/illustrations">unDraw</a>
                </figcaption>
            </figure>
            ```

        === "Rendu"
            <figure>
                <img src="../images/undraw_Polaroid.svg" alt ="Illustration d'une photo" width="300" >
                <figcaption>
                    Un Polaroïd selon <a href="https://undraw.co/illustrations" target="_blank">unDraw</a>
                </figcaption>
            </figure>

        ??? note "Pour une largeur en %, l'image est décalée par rapport à sa légende..."
            
            === "Code"
                ```html
                <figure>
                    <img src="../images/undraw_Polaroid.svg" alt ="Illustration d'une photo" width="50%" >
                    <figcaption>
                        Un Polaroïd selon <a href="https://undraw.co/illustrations">unDraw</a>
                    </figcaption>
                </figure>
                ```

            === "Rendu"
                <figure>
                    <img src="../images/undraw_Polaroid.svg" alt ="Illustration d'une photo" width="50%" >
                    <figcaption>
                        Un Polaroïd selon <a href="https://undraw.co/illustrations" target="_blank">unDraw</a>
                    </figcaption>
                </figure>
                                
            Ce décalage n'apparait pas pour une largeur indiquée [en *px* ou en *em*](https://www.codeur.com/tuto/css/unite-de-mesure-taille-px-em-rem/){target="_blank"}.

    ??? example "Solution 2 : un code MarkDown..."
        L'extension [attr_list](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#attribute-lists){target="_blank"} 
        qui permet de préciser des valeurs personnalisées aux attributs HTML et CSS doit être activée dans le fichier `mkdocs.yml` :

        ```yaml
        markdown_extensions:
            - attr_list
        ```
        Il faut ajouter la spécification CSS supplémentaire dans le fichier `docs/stylesheet/extra.css`
         (Merci à [Gilles](https://mooc-forums.inria.fr/moocnsi/t/mkdocs-astuce-pour-centrer-une-image-en-markdown-pur/2831)) :

        ```css
        .center {
            display: block;
            margin: 0 auto;
        }
        ```

        L’insertion d’une image peut se faire maintenant avec la syntaxe :
        ```markdown
        ![texte alternatif](adresse "info-bulle"){ .center }
        ```
        === "Rendu"
            ![Illustration d'une photo](../images/undraw_Polaroid.svg){ width="30%" .center }

        === "Code"
            ```markdown
            ![Illustration d'une photo](../images/undraw_Polaroid.svg){ width="30%" .center }  
            ```
        
        !!! note "Même avec une largeur en %, l'image est centrée mais il n'y a pas de légende centrée possible."
             

    ??? example "Solution 3 : un code hybride..."

        En plus de l'extension [attr_list](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#attribute-lists){target="_blank"} 
        qui permet de préciser des valeurs personnalisées aux attributs HTML et CSS, il faut également activer dans le fichier `mkdocs.yml` l'extension [md_in_html](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#markdown-in-html) qui permet d'écrire du code MarkDown à l'intérieur de balises HTML :

        ```yaml
        markdown_extensions:
            - attr_list
            - md_in_html
        ```
        
        Comme pour la solution précédente, il faut ajouter la spécification CSS supplémentaire dans le fichier `docs/stylesheet/extra.css`
         (Merci à [Gilles](https://mooc-forums.inria.fr/moocnsi/t/mkdocs-astuce-pour-centrer-une-image-en-markdown-pur/2831)) :

        ```css
        .center {
            display: block;
            margin: 0 auto;
        }
        ```

        Pour notre exemple, une synthaxe possible serait,
         sans oublier d'inscrire `markdown` dans les balises HTML qui contiendront du MarkDown :

        === "Code"
            ```html
            <figure markdown>
                ![Illustration d'une photo](../images/undraw_Polaroid.svg){ width="50%" .center }
                <figcaption markdown>
                    Un Polaroïd selon [unDraw](https://undraw.co/illustrations){target="_blank"}
                </figcaption>
            </figure>            
            ```

        === "Rendu"
            <figure markdown>
                ![Illustration d'une photo](../images/undraw_Polaroid.svg){ width="50%" .center }
                <figcaption markdown>
                    Un Polaroïd selon [unDraw](https://undraw.co/illustrations){target="_blank"}
                </figcaption>
            </figure>


    
??? question "Quel format d'image pour le web ?"

    **JPEG**  (**J**oint **P**hotographic **E**xpert **G**roup)
    : Parfait pour les photos et visuels colorés, c’est le format compressé le plus utilisé sur le web.

    **PNG** (**P**ortable **N**etwork **G**raphics)
    : Idéal pour les images à fond transparent, graphique et logo.

    **SVG** (**G**raphics **I**nterchange **F**ormat)
    : Format adapté aux images vectorielles, permet de les déformer sans altérer la qualité.

    **GIF** (**G**raphics **I**nterchange **F**ormat)
    : Images animées idéale pour illustrer vos propos, fortement utilisé sur les réseaux sociaux.

***
## Traits horizontaux :

=== "Rendu"
    Une série d'au moins trois `*`,
    ***
    ou trois `_`,
    ___
    ou trois `-` après un saut de ligne,

    ---
    trace une ligne de séparation.

=== "MarkDown"
    ```markdown
    Une série d'au moins trois `*`,
    ***
    ou trois `_`,
    ___
    ou trois `-` après un saut de ligne,

    ---
    trace une ligne de séparation.
    ```

***
## Listes :

### Listes à puces :
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

### Listes ordonnées :
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

### Listes avec des cases à cocher :
On insère `[ ]` ou `[x]` devant chaque item
 d'une liste non ordonnée :
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
     [pymdownx.tasklist](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#tasklist)
      pour générer des listes de tâches avec des cases à cocher.
    
    ``` yaml
    markdown_extensions:
        - pymdownx.tasklist        
    ```
    
    
### Listes de description :
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
     [def_list](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#definition-lists)
      pour générer des listes de définitions.

    ``` yaml
    markdown_extensions:
        - def_list        
    ```

***
## Codes :

### Code inline :
Comme vu dans le [Corps de texte](./#corps-de-texte),
 on peut afficher dans le flux d'un paragraphe,
  du code en caractères [`monospaces`][2]
   en l'encadrant entre deux `` ` ``
    que l'on peut obtenir par la combinaison
     de touches ++"AltGr"+"7"++ ou ++"Alt"+"96"++.

!!! note "Remarque :"
    Si le codage renferme déjà une apostrophe inversée
     ( = un caractère d'[accent grave](https://fr.wikipedia.org/wiki/Accent_grave)),
     on peut précéder et terminer la zone de code de deux fois ce caractère.  
    Dans ce cas, Markdown n’interprétera pas cette apostrophe inversée comme une balise.

    === "MarkDown"
        ```markdown
        Exemple : ``Ceci est du `code`.``
        ```
    === "Rendu"
        Exemple : ``Ceci est du `code`.``

Ecrire du code en ligne avec coloration syntaxique `#!python [ for i in range(toto) if truc]` test 

### Bloc de texte brut :
=== "MarkDown"
    ```markdown
    Pour produire un bloc de texte brut,
     il suffit de faire un saut de ligne vide et
      de précéder le code d'une tabulation      
       équivalente à au moins quatre espaces :

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
     il suffit de faire un saut de ligne vide et
      de précéder le code d'une tabulation      
       équivalente à au moins quatre espaces :

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
### Coloration syntaxique :

On peut également produire des blocs de texte brut
 en encadrant les lignes de code
  entre deux triplets d'apostrophes inversées (d'accent grave) ;

Aussi, si on précise après le premier triplet le langage
 de programmation correspondant au contenu des lignes de code,
 la coloration syntaxique idoine s'applique :

!!! example "Exemple :"

    === "MarkDown basique"
        ````
        ```
        def ma_fonction(paramètres):
            # bloc d'instructions (optionnel)
            return valeur
        ```
        ````
    === "Rendu basique"
        ```
        def ma_fonction(paramètres):
            # bloc d'instructions (optionnel)
            return valeur
        ```
    
    === "MarkDown avec langage"
        ````
        ``` python
        def ma_fonction(paramètres):
            # bloc d'instructions (optionnel)
            return valeur
        ```
        ````
    === "Rendu avec coloration"
        ``` python
        def ma_fonction(paramètres):
            # bloc d'instructions (optionnel)
            return valeur
        ```

***
## Admonitions :
???+ warning inline end "Attention !"
    
    **Toto** est dans la place...

    Ceci est une mise en garde,
     vous voilà prévenu !!
Une des grandes caractéristiques de MkDocs avec Material sont ces admonitions : ce sont des boites colorées d'avertissements, pour des alertes, mises en garde et autres appartés, qui viennent compléter le flux normal de l'information sur une page web pour illustrer ou souligner un point particulier, une difficulté...

De base, il existe [12 styles de boites](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types) différentes définies par des noms de types. Si aucun de ces mots clés types n'est précisé, ou si le mot clé n'est pas reconnu, c'est le type `note` qui sera utilisé par défaut.
=== "note"
    === "Rendu"
        !!! note
            Un avertissement de type `note`.
    === "Mardown"
        ```markdown
        !!! note
            Un avertissement de type `note`.
        ```
=== "abstract"
    === "Rendu"
        !!! abstract
            Un avertissement de type `abstract` (résumé), `summary` (sommaire) ou `tdlr` (too long ; didn't read).
    === "Mardown"
        ```markdown
        !!! abstract
            Un avertissement de type `abstract` (résumé), `summary` (sommaire) ou `tdlr` (too long ; didn't read).
        ```
=== "info"
    === "Rendu"
        !!! info
            Un avertissement de type `info` ou `todo` (à faire).
    === "Mardown"
        ```markdown
        !!! info
            Un avertissement de type `info` ou `todo` (à faire).
        ```
=== "tip"
    === "Rendu"
        !!! tip
            Un avertissement de type `tip` (astuce), `hint` (indice), `important`.
    === "Mardown"
        ```markdown
        !!! tip
            Un avertissement de type `tip` (astuce), `hint` (indice), `important`.
        ```
=== "success"
    === "Rendu"
        !!! success
            Un avertissement de type `success`, `check` (vérifié) ou `done` (terminé).
    === "Mardown"
        ```markdown
        !!! success
            Un avertissement de type `success`, `check` (vérifié) ou `done` (terminé).
        ```
=== "question"
    === "Rendu"
        !!! question
            Un avertissement de type `question`, `help` (aide) ou `faq` (Frequently Asked Questions)
    === "Mardown"
        ```markdown
        !!! question
            Un avertissement de type `question`, `help` (aide) ou `faq` (Frequently Asked Questions)
        ```
=== "attention"
    === "Rendu"
        !!! attention
            Un avertissement de type `attention`, `warning`, `caution` (avertir).
    === "Mardown"
        ```markdown
        !!! attention
            Un avertissement de type `attention`, `warning`, `caution` (avertir).
        ```
=== "failure"
    === "Rendu"
        !!! failure
            Un avertissement de type `failure` (échec), `missing` (manquant), `fail` (échouer).
    === "Mardown"
        ```markdown
        !!! failure
            Un avertissement de type `failure` (échec), `missing` (manquant), `fail` (échouer).
        ```
=== "danger"
    === "Rendu"
        !!! danger
            Un avertissement de type `danger` ou `error`.
    === "Mardown"
        ```markdown
        !!! danger
            Un avertissement de type `danger` ou `error`.
        ```
=== "bug"
    === "Rendu"
        !!! bug
            Un avertissement de type `bug`.
    === "Mardown"
        ```markdown
        !!! bug
            Un avertissement de type `bug`.
        ```
=== "example"
    === "Rendu"
        !!! example
            Un avertissement de type `example`.
    === "Mardown"
        ```markdown
        !!! example
            Un avertissement de type `example`.
        ```
=== "quote"
    === "Rendu"
        !!! quote
            Un avertissement de type `quote` (citation) ou `cite` (citer).
    === "Mardown"
        ```markdown
        !!! quote
            Un avertissement de type `quote` (citation) ou `cite` (citer).
        ```
Pour la syntaxe, on commmence par trois points d'exclamation `!!!`
 suivi d'un espace et du mot clé type de l'admonition qui s'affichera en titre par défaut.

Puis, après un retour à la ligne et une indentation de 4 espaces,
 on peut écrire en MarkDown le code du contenu de la boite d'avertissement.

??? tip "Des titres personnalisés : ..."
    Après le type, il est possible d'ajouter un titre personnalisé entre guillemets
     ce qui va nous permettre au moins de franciser les titres de nos boites :     
    === "Rendu"
        !!! example "Exemple :"
            Un exemple de boite
             avec un titre
              personnalisé.
    === "Mardown"
        ```markdown
        !!! example "Exemple :"
            Un exemple de boite
             avec un titre
              personnalisé.
        ```    
    !!! tip ""
        Un titre personalisé vide `""` permet de produire une boite d'avertissement sans barre de titre :
        === "Mardown"
            ```markdown
            !!! example ""
                Un exemple de boite sans titre.
            ```
        === "Rendu"
            !!! example ""
                Un exemple de boite sans titre.

??? tip "Des boites déroulantes : ..."
    En remplaçant les trois points d'exclamation `!!!`
    par trois points d'interrogation `???`
    on obtient une boite déroulante enroulée par défaut.  
    === "Rendu"
        ??? example "Exemple NF : ..."
            Un exemple de boite déroulante
             enroulée par défaut.
    === "Mardown"
        ```markdown
        ??? example "Exemple NF : ..."
            Un exemple de boite déroulante
             enroulée par défaut.
        ```
    Pour qu'elle soit déroulée par défaut, il suffit d'ajouter un `+`
    après les trois points d'interrogation `???`.
    === "Mardown"
        ```markdown
        ???+ example "Exemple NO : ..."
            Un exemple de boite déroulante
             déroulée par défaut.
        ```
    === "Rendu"
        ???+ example "Exemple NO : ..."
            Un exemple de boite déroulante
             déroulée par défaut.
    
    !!! attention ""
        Une boite d'avertissement déroulante
        possède toujours une barre de titre
         même avec un titre personnalisé vide !
        === "Rendu"
            ???+ example ""
                Un exemple de boite déroulante
                 sans titre mais avec une barre.
        === "Mardown"
            ```markdown
            ???+ example ""
                Un exemple de boite déroulante
                sans titre mais avec une barre.
            ```

    
??? tip "Des boites "inline" : ..."
    === "Rendu à gauche"
        !!! example inline "Exemple :"
            Un exemple de boite
            s'alignant à gauche.
        En indiquant `inline` entre
         le mot clé du type et le titre personnalisé,
          cela modifie le comportement d'affichage de la boite
           d'avertissement.
        
        Elle s'aligne à **gauche** en parallèle
            du bloc de paragraphes qu'elle précède.
    === "Mardown à gauche"
        ```markdown
        !!! example inline "Exemple :"
            Un exemple de boite
            s'alignant à gauche.
        En indiquant `inline` entre
         le mot clé du type et le titre personnalisé,
          cela modifie le comportement d'affichage de la boite
           d'avertissement.
        
        Elle s'aligne à **gauche** en parallèle
            du bloc de paragraphes qu'elle précède.
        ```    
    === "Rendu à droite"
        !!! note inline end "Exemple :"
            Un exemple de boite
            s'alignant à droite.
        En indiquant `inline end` entre
         le mot clé du type et le titre personnalisé,
          cela modifie le comportement d'affichage de la boite
           d'avertissement.

        Elle s'aligne à **droite** en parallèle
            du bloc de paragraphes qu'elle précède.  
    === "Mardown à droite"
        ```markdown
        !!! example inline end "Exemple :"
            Un exemple de boite
            s'alignant à droite.
        En indiquant `inline end` entre
         le mot clé du type et le titre personnalisé,
          cela modifie le comportement d'affichage de la boite
           d'avertissement.

        Elle s'aligne à **droite** en parallèle
            du bloc de paragraphes qu'elle précède.
        ```

??? info 

    Pour permettre les fonctionnalités des [boites d'avertissement](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) décrites ci-dessus,
     il faut activer dans le fichier `mkdocs.yml` les extensions :

    ```yaml
    markdown_extensions:
      - admonition              
      - pymdownx.details        
      - pymdownx.superfences    
    ```
???+ tip "Des boites très personnalisées : ..."

    Il est possible de choisir des [icones](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#admonition-icons)
     personnalisés pour chaque type de boite d'avertissement.

    On peut même [customiser](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#customization)
     ses propres types de boites d'avertissement comme par exemple :
    === "Rendu"
        !!! adn
            La boite très spéciale pour l'Atelier du numérique.
    === "Mardown"
        ```markdown
        !!! adn
            La boite très spéciale pour l'Atelier du numérique.
        ```
    === "docs/stylesheets/extra.css"
        ``` css
        /*Ajout pour admonition spéciale adn */
        :root {
            --md-admonition-icon--adn: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="m290.2,256c51.2-33.4 164.8-119.4 164.8-224.6 0-11.3-9.1-20.4-20.4-20.4-11.3,0-20.4,9.1-20.4,20.4 0,93.3-122.2,175.6-158.2,197.9-36.1-22.2-158.2-104.4-158.2-197.9-1.42109e-14-11.3-9.1-20.4-20.4-20.4-11.3,0-20.4,9.1-20.4,20.4 0,105.2 113.6,191.2 164.8,224.6-51.3,33.4-164.9,119.4-164.9,224.6-7.10543e-15,11.3 9.1,20.4 20.4,20.4 11.3,0 20.4-9.1 20.4-20.4 0-93.3 122.2-175.6 158.2-197.9 36.1,22.2 158.2,104.4 158.2,197.9 0,11.3 9.1,20.4 20.4,20.4 11.3,0 20.4-9.1 20.4-20.4 0.2-105.2-113.4-191.2-164.7-224.6z"/><path d="m177,51.8h158c11.3,0 20.4-9.1 20.4-20.4 0-11.3-9.1-20.4-20.4-20.4h-158c-11.3,0-20.4,9.1-20.4,20.4 0,11.3 9.1,20.4 20.4,20.4z"/><path d="m211.7,113.3c-11.3,0-20.4,9.1-20.4,20.4 0,11.3 9.1,20.4 20.4,20.4h88.6c11.3,0 20.4-9.1 20.4-20.4 0-11.3-9.1-20.4-20.4-20.4h-88.6v1.42109e-14z"/><path d="m335,460.2h-158c-11.3,0-20.4,9.1-20.4,20.4 0,11.3 9.1,20.4 20.4,20.4h158c11.3,0 20.4-9.1 20.4-20.4 0-11.3-9.1-20.4-20.4-20.4z"/><path d="m300.3,398.7c11.3,0 20.4-9.1 20.4-20.4 0-11.3-9.1-20.4-20.4-20.4h-88.6c-11.3,0-20.4,9.1-20.4,20.4 0,11.3 9.1,20.4 20.4,20.4h88.6z"/></svg>')
        }
        .md-typeset .admonition.adn,
        .md-typeset details.adn {
            border-color: rgb(233, 32, 99);
        }
        .md-typeset .adn > .admonition-title,
        .md-typeset .adn > summary {
            background-color: rgba(233, 32, 99, 0.1);
            border-color: rgb(233, 32, 99);
        }
        .md-typeset .adn > .admonition-title::before,
        .md-typeset .adn > summary::before {
            background-color: rgb(233, 32, 99);
            -webkit-mask-image: var(--md-admonition-icon--adn);
                    mask-image: var(--md-admonition-icon--adn);
        }
        ```
    === "mkdocs.yml"
        ```yaml
        extra_css:
          - stylesheets/extra.css
        ```

***
## Toujours en construction...

![Illustration par unDrawn de la construction d'un mur](../images/undraw_building_blocks_n0nc.svg "Toujours en construction..." )

***
## Volets :


*** 
## Citations et 

> :warning: **If you are using mobile browser**: Be very careful here!

| WARNING: be careful to baz the quux before initializing the retro encabulator! |
| --- |


> **⚠ WARNING: Aliens are coming.**  
> A description of the colour, smell and dangerous behaviour of the aliens.



A simple highlighted warning can be achieved like this:

>[!WARNING]
>This is a warning




    

    
    
     



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
## Tableaux :

***
## 
***
## Ressources :

<https://www.jdbonjour.ch/cours/markdown-pandoc/>

<https://agea.github.io/tutorial.md/>

<https://learninglab.gitlabpages.inria.fr/mooc-rr/mooc-rr-ressources/module1/ressources/introduction_to_markdown_fr.html>

<https://www.markdownguide.org/>

<https://www.markdowntutorial.com/>

<https://www.ionos.fr/digitalguide/sites-internet/developpement-web/markdown/>

<https://docs.microsoft.com/en-us/contribute/markdown-reference>

<https://jupyterbook.org/content/myst.html> Markedly Structured Text
***

