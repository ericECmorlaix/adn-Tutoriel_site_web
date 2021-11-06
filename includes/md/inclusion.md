??? faq "Quid : si on intègre le contenu d'un fichier en dehors d'un bloc de code ?"
    !!! attention ""
        === "MarkDown"
            ```md
            --8<-- "docs/index.md" 
            ```        
        === "Rendu"
            --8<-- "docs/index.md"
    !!! failure ""
        === "MarkDown"
            ```md
            --8<-- "includes/py/exemple.py" 
            ```        
        === "Rendu"
            --8<-- "includes/py/exemple.py"
    !!! success ""
        === "MarkDown"
            ```md
            --8<-- "docs/images/undraw_Polaroid.svg" 
            ```        
        === "Rendu"
            --8<-- "docs/images/undraw_Polaroid.svg"

### Fichier `.md` :
!!! attention ""
    On observe que le code MarkDown contenu dans le fichier `:::md index.md`
    s'affiche bien, hormis son [entête de métadonnées](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#hiding-the-sidebars)...

    On a là une solution pour inclure du contenu externe codé en MarkDown
    pour développer une longue page web en la décomposant en sous-parties.  

    ??? example "Exemple avec le début du code qui génère cette page : ..."
        ```` md hl_lines="3 6 25"
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
        ````
    Il est alors simple de répéter plusieurs fois un même bout de code
    dans une ou plusieurs pages différentes à partir d'une seule et même source.

    C'est le cas ici du contenu du fichier `:::md introductionM.md`
    qui est appelé deux fois dans la partie `:::md ## Introduction :`,
    et également dans le fichier `:::md lien.md`,
    qui est lui même intégré plus loin dans la partie `:::md ## Lien :`.

    Au total, on retrouve trois fois le contenu du paragraphe d'introduction MarkDown
    dans cette page et s'il faut y apporter une modification,
    il suffira d'agir dans son unique fichier source pour la répercuter partout...

    Ce  mécanisme d'inclusion d'extraits de code MarkDown est permis par l'extension [Snippets]{ target=_blank}.
    La syntaxe `--8<--` représente une paire de ciseaux en art ASCII.
    Il est aussi possible d'inclure plusieurs fichiers d'affilée
    en ajoutant selon le besoin des sauts de lignes et des indentations,
    un point virgule suivi d'une espace pour ignorer un fichier...
    ??? example "Comme par exemple ainsi : ..."
        === "MarkDown avec inclusions"
            ```md
            --8<-- 
            includes/md/loremIpsum.md
            includes/md/totoAlerte.md

                    includes/md/loremIpsum.md

            includes/md/loremIpsum.md
            ; includes/md/loremIpsum.md
            includes/md/loremIpsum.md

                includes/md/loremIpsum.md

            includes/md/loremIpsum.md
            --8<-- 
            ```

        === "Code MarkDown généré"
            ```md
            --8<--
            includes/md/loremIpsum.md
            includes/md/totoAlerte.md

                    includes/md/loremIpsum.md

            includes/md/loremIpsum.md
            ; includes/md/loremIpsum.md
            includes/md/loremIpsum.md

                includes/md/loremIpsum.md

            includes/md/loremIpsum.md
            --8<--
            ```
        === "Rendu"
            --8<--
            includes/md/loremIpsum.md
            includes/md/totoAlerte.md

                    includes/md/loremIpsum.md

            includes/md/loremIpsum.md
            ; includes/md/loremIpsum.md
            includes/md/loremIpsum.md

                includes/md/loremIpsum.md

            includes/md/loremIpsum.md
            --8<--
        !!! note "Remarque :"
            [Snippets]{ target=_blank} concatène (agrège)
             tout le code contenu dans les fichiers à inclure,
              il peut donc être nécessaire d'insérer des sauts de lignes
               et/ou des indentations entre les extraits inclus.
    ??? faq "Le fonctionnement de [Snippets]{ target=_blank} est-il récursif ? :thinking:" 
        
        Si comme moi vous êtes joueur, vous brulez d'envie de l'expérimenter
         pour le vérifier par vous même...  :wink:, sinon :
        === "divulgachage n°1 :"
            La réponse se trouve [là](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#overview)&mldr; :face_with_monocle: 
        === "divulgachage n°2 :"
            Oui, c'est récursif au sens ou un `fichier_a.md`
             peut inclure un `fichier_b.md` qui lui même
              inclut un autre `fichier_c.md` et ainsi de suite... :smirk:
        === "divulgachage n°3 :"
            Non, ce n'est pas vraiment récursif car le `fichier_b.md`
            ne peut pas s'inclure lui même, ni être inclus dans le `fichier_c` qu'il inclut déjà.  
            Dès que [Snippets] rencontre une nouvelle fois un même fichier
            dans la pile d'appels, le processus d'inclusion s'arrête par sécurité
             pour éviter une boucle infinie... :confused:


    
    ??? tip "Un fichier unique de références hypertextes et d'abréviations : ..."
        L'extension [Snippets]{ target=_blank} permet ainsi
        de créer facilement un fichier commun de références
        pour regrouper toutes les adresses de liens des différentes pages d'un site.

        De plus, en l'associant avec l'extension
        [`::: md abbr`](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
        qui sert à définir des abréviations et qu'il faut rajouter dans le fichier `mkdocs.yml` :

        ```yaml
        markdown_extensions:
        - abbr
        - pymdownx.snippets
        ```
        Il est possible de créer un glossaire d'acronymes :

        !!! example ""
        === "Fichier : includes/md/abr_ref-exemple.md"
            ```md
            --8<-- "includes/md/abr_ref-exemple.md"
            ```
        === "MarkDown"
            ```md
            La spécification HTML est maintenue par le [W3C]{target=_blank}.

            --8<-- "includes/md/abr_ref-exemple.md" 
            ```
        === "Rendu"
            La spécification HTML est maintenue par le [W3C]{target=_blank}.

            --8<-- "includes/md/abr_ref-exemple.md"

### Autres fichiers :
!!! failure ""
    On observe que le contenu du fichier `.py` n'est pas bien interprété
    car son indentation n'est pas respecté.

    Ce genre de contenu ne sera correctement affiché que dans un [bloc de code](#bloc-de-code)
     encadré entre des ```` ``` ```` et en précisant le langage
      si on souhaite la coloration syntaxique.

    Pour un affichage plus basique en texte brut,
     il suffit d'indenter de 4 espaces à gauche avant les ciseaux  `:::md --8<--` :

    === "MarkDown avec inclusion"
        ```md
            --8<-- "includes/py/exemple.py" 
        ```        
    === "Code MarkDown généré"
        ```md
            --8<-- "includes/py/exemple.py"
        ```
    === "Rendu"
            --8<-- "includes/py/exemple.py"
!!! success ""
    En revanche le code du fichier `.svg` est bien interprété.

    Voici donc une autre façon d'intégrer une image SVG
    mais sans la gestion ici de la taille d'affichage :

    === "MarkDown avec inclusion"
        ```md
        <figure markdown>
            --8<-- "docs/images/undraw_Polaroid.svg" 
        <figcaption markdown>
                Un Polaroïd selon [unDraw]{target="_blank"}
            </figcaption>
        </figure>
        ```

    === "Code MarkDown généré"
        ```md
        <figure markdown>
            --8<-- "docs/images/undraw_Polaroid.svg"
        <figcaption markdown>
                Un Polaroïd selon [unDraw]{target="_blank"}
            </figcaption>
        </figure>
        ```
    === "Rendu"
        <figure markdown>
            --8<-- "docs/images/undraw_Polaroid.svg"
        <figcaption markdown>
                Un Polaroïd selon [unDraw]{target="_blank"}
            </figcaption>
        </figure>

!!! summary ""
En conclusion, quelque soit l'extension du fichier inclu, MkDocs-Material avec l'extension [Snippets]{ target=_blank} va parser (analyser, chercher à interpréter) le code contenu comme s'il s'agissait d'un fichier `.md`.

S'il rencontre des caractères de balisage assimilable à **MarkDown**, <em>HTML</em> ou $\LaTeX$, il va les convertir pour générer le code HTML final destiné au navigateur.

Lors de la [construction du site, MkDocs convertit](https://www.mkdocs.org/user-guide/writing-your-docs/#file-layout){ target=_blank} chacun des fichiers `truc.md` qui se trouve dans le dossier `docs` en créant un dossier nommé `truc` contenant une copie du fichier `truc.md` et un fichier `index.html` généré à partir du code MarkDown de `truc.md` pour permettre son bon affichage dans un navigateur.  
De même avec l'extension [mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter){ target=_blank} pour les fichiers en `.py` et `.ipynb`.  
En conséquence, il est préférable de placer tous les fichiers d'extraits à inclure à l'extérieur du dossier `docs` par exemple dans un dossier nommé `includes`.
!!! note 
Une autre solution consiste à modifier l'extension du fichier `truc.md` à inclure en `truc.txt`, par exemple, et ainsi le conserver dans le dossier `docs` sans qu'il soit automatiquement converti.
