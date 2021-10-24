
# Introduction :

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
            Cliquer sur les onglets ci-dessus pour comparer les codes <strong>Markdown</strong>
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
            Cliquer sur les onglets ci-dessus pour comparer les codes <strong>Markdown</strong>
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

# Les titres :

=== "Rendu"

    # Titre de niveau 1
    ## Titre de niveau 2
    ### Titre de niveau 3
    #### Titre de niveau 4
    ##### Titre de niveau 5
    ###### Titre de niveau 6
    ####### Il n'y a pas de titre de niveau 7 

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

    === "Rendu"

        Souligner avec des `=` produit un titre de niveau 1
        ===================================================

        Souligner avec des `-` produit un titre de niveau 2
        ---------------------------------------------------

    !!! note "Remarque :"
    
        Un seul `=` ou `-` suffirait.  
        Leur répétition permet de souligner ces titres
         également dans le code en mode édition.
    
***
# Le corps de texte :

=== "Rendu"

    On peut obtenir du _texte_ avec *simple emphase* rendu en *italique*,
     du __texte__ avec **forte emphase** rendu en **Gras**,
      du **_Texte_** à la fois en **gras** et en *italique*,
       du `code source` rendu en caractères [`monospaces`][2],
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
       du `code source` rendu en caractères [`monospaces`][2],
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
    ```

??? info 

    Il faut activer dans le fichier `mkdocs.yml` les extensions :

    - [pymdownx.caret](https://facelessuser.github.io/pymdown-extensions/extensions/caret) pour `^^souligné^^` ou mettre en `^exposant^`;
    - [pymdownx.mark](https://facelessuser.github.io/pymdown-extensions/extensions/mark/) pour `==surligné==`;
    - [pymdownx.tilde](https://facelessuser.github.io/pymdown-extensions/extensions/tilde/) pour `~~barré~~` ou mettre en `~indice~`.

***

# Les liens :

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

# Les images :

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
     générée à partir du fichier `MarkDown-Mkdocs_Material.md`
      sera `../images/undraw_Polaroid.svg` car il faut sortir du dossier `MarkDown-Mkdocs_Material` pour pouvoir rentrer dans le dossier `images`.
    
    !!! note "Remarque :"
        Un chemin relatif vers cette même image depuis la page web `index.html`
         générée à partir du fichier `index.md` serait `./images/undraw_Polaroid.svg`...
    

???+ tip "Pour gérer l'alignement et la taille d'une image :"

    L'extension [attr_list](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#attribute-lists){target="_blank"}
     activée dans le fichier `mkdocs.yml` permet de préciser des valeurs personnalisées aux attributs HTML et CSS.

    === "Rendu"
        ![Illustration d'une photo](../images/undraw_Polaroid.svg){width=15% align=right}  
        Ainsi le code MarkDown suivant :
        ````markdown
        ![Illustration d'une photo](../images/undraw_Polaroid.svg){width=15% align=right}
        ````
        placé au début du texte de ce paragraphe, produit l'affichage de l'image tel que ci-contre.
    === "MarkDown"
        ```markdown
        ![Illustration d'une photo](../images/undraw_Polaroid.svg){width=15% align=right}  
        Ainsi le code MarkDown suivant :
        ````markdown
        ![Illustration d'une photo](../images/undraw_Polaroid.svg){width=15% align=right}
        ````
        placé au début du texte de ce paragraphe, produit l'affichage de l'image tel que ci-contre.
        ```

    
    
??? question "Quel format d'image pour le web ?"

    **JPEG**  (**J**oint **P**hotographic **E**xpert **G**roup)
    : Parfait pour les photos et visuels colorés, c’est le format compressé le plus utilisé sur le web.

    **PNG** (**P**ortable **N**etwork **G**raphics)
    : Idéal pour les images à fond transparent, graphique et logo.

    **SVG** (**G**raphics **I**nterchange **F**ormat)
    : Format adapté aux images vectorielles, permet de les déformer sans altérer la qualité.

    **GIF** (**G**raphics **I**nterchange **F**ormat)
    : Images animées idéale pour illustrer vos propos, fortement utilisé sur les réseaux sociaux.




# Les traits horizontaux :

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

# Les listes :

## Listes à puces :
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

## Listes ordonnées :
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

## Listes avec des cases à cocher :
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
    
    
## Listes de description :
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

***

# Ressources :

<https://www.jdbonjour.ch/cours/markdown-pandoc/>

<https://agea.github.io/tutorial.md/>

<https://learninglab.gitlabpages.inria.fr/mooc-rr/mooc-rr-ressources/module1/ressources/introduction_to_markdown_fr.html>

<https://www.markdownguide.org/>

<https://www.markdowntutorial.com/>

<https://www.ionos.fr/digitalguide/sites-internet/developpement-web/markdown/>

***

# Toujours en construction...

![Illustration par unDrawn de la construction d'un mur](../images/undraw_building_blocks_n0nc.svg "Toujours en construction..." )


<!-- Si votre codage renferme déjà l’apostrophe inversée, vous devez précéder la zone de code de deux fois ce caractère. Dans ce cas, Markdown n’interprétera pas l’apostrophe inversée comme une balise.

``C’est tout le `code`.``


***

# Les admonitions :

!!! warning inline end "Attention"
    
    **Toto** est dans la place !


*** -->


