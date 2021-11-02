La syntaxe pour les images est la même que pour les liens hypertextes,
 mais avec un `!` devant :
```md
![texte alternatif](adresse "info-bulle")
```
L'info-bulle optionnelle s'affichera au survol de l'image.

Il est important de bien choisir le [texte alternatif](http://www.pompage.net/traduction/Bien-utiliser-le-texte-alternatif){target="_blank"}
 qui s'affichera lorsque l'image n'est pas disponible,
 car il permet aussi l'accessibilité pour les non-voyants
  et apporte de la sémantique pour les moteurs de recherche...

L'adresse est l'URL relative ou absolue qui permet d'atteindre le fichier lié en cheminant dans l'arborescence du site web, sachant que le dossier `docs` du projet MkDocs (cf. [branche `main` du dépot GitHub](https://github.com/ericECmorlaix/adn-Tutoriel_site_web/tree/main){target="_blank"}) devient la racine du `site` une fois déployé (cf. [branche `gh-pages`du dépot GitHub](https://github.com/ericECmorlaix/adn-Tutoriel_site_web/tree/gh-pages){target="_blank"}) :

??? example "Exemple :"

    === "chemin relatif à la page"
        ```md
        ![Illustration d'une photo instantané](../images/undraw_Polaroid.svg "image via URL relative")
        ```
        ![Illustration d'une photo instantané](../images/undraw_Polaroid.svg "image via URL relative")

    === "chemin relatif à la racine"
        ```md
        ![Illustration d'une photo instantané](/images/undraw_Polaroid.svg "image via URL relative")
        ```
        ![Illustration d'une photo instantané](/images/undraw_Polaroid.svg "image via URL relative")

    === "chemin absolu"
        ```md
        ![Illustration d'une photo instantané](https://ericecmorlaix.github.io/adn-Tutoriel_site_web/images/undraw_Polaroid.svg "image via URL absolue")
        ```
        ![Illustration d'une photo instantané](https://ericecmorlaix.github.io/adn-Tutoriel_site_web/images/undraw_Polaroid.svg "image via URL absolue")

    === "par référence"
        ```md
        Ce qui permet d'ajouter facilement un [lien pour ouvrir cette image][polaroïd]{ target="_blank"} dans un nouvel onglet...
        
        ![polaroïd]

        <!-- Une seule et même référence pour le lien et l'image, une référence plusieurs fois réutilisable dans ce document... -->
        [polaroïd]: /images/undraw_Polaroid.svg "Illustration d'une photo instantané"
        ```
        Ce qui permet d'ajouter facilement un [lien pour ouvrir cette image][polaroïd]{ target="_blank"} dans un nouvel onglet...
        
        ![polaroïd]
        
        <!-- Une seule et même référence pour le lien et l'image, une référence plusieurs fois réutilisable dans ce document... -->
        [polaroïd]: /images/undraw_Polaroid.svg "Illustration d'une photo instantané"

    Ici le fichier de l'image est placé dans un dossier nommé `images` lui même situé dans le dossier `docs` :
    ```console
    ├── docs/
    │   └── images/
    │   │   └── undraw_Polaroid.svg
    │   └── MarkDown-Mkdocs_Material.md
    │   └── index.md
    └─ mkdocs.yml
    ```
    Une fois déployé ce dossier `images` sera à la racine du site :
    ```console  
    └── site/
        ├── images/
        │   └── undraw_Polaroid.svg
        ├── MarkDown-Mkdocs_Material/
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
        
    !!! note "Remarque 1 :"
        Un chemin relatif vers cette même image depuis la page web `index.html`
        située à la racine du site et
         générée à partir du fichier `index.md`
          serait `./images/undraw_Polaroid.svg`.
    
    !!! note "Remarque 2 :"
        Un chemin relatif depuis la racine du site web 
        vers cette même image serait `/images/undraw_Polaroid.svg`.
        
        **Un tel chemin est très pratique** :
        il fonctionne aussi bien depuis la page web `index.html`
        située à la racine du site que depuis la page web `index.html`
        située dans le dossier `MarkDown-Mkdocs_Material`
         car, définit à partir de la racine,
        il est commun à toutes les pages du site.

        ??? cite "Une vidéo simple, claire et calme, à ce sujet : ..."

            &ldquo;Remember that, as far as mkdocs in concerned, the docs folder is considered to be the root folder&rdquo;

            [https://calmcode.io/mkdocs/hosting-images.html](https://calmcode.io/mkdocs/hosting-images.html){ target=_blank}
    
??? tip "Pour gérer l'alignement et la taille d'une image :"

    L'extension [attr_list](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#attribute-lists){target="_blank"} 
        qui permet de préciser des valeurs personnalisées aux attributs HTML et CSS doit être activée dans le fichier `mkdocs.yml` :

    ```yaml
        markdown_extensions:
            - attr_list
    ```
    
  
    === "Rendu"
        ![polaroïd]{width=20% align=right}  
        Ainsi le code MarkDown suivant :
        ```markdown
        ![polaroïd]{width=20% align=right}
        ```
        placé au début du texte de ce paragraphe, produit l'affichage de l'image tel que ci-contre.
    === "MarkDown"
        ````md
        ![polaroïd]{width=20% align=right}  
        Ainsi le code MarkDown suivant :
        ```markdown
        ![polaroïd](../images/undraw_Polaroid.svg){width=20% align=right}
        ```
        placé au début du texte de ce paragraphe, produit l'affichage de l'image tel que ci-contre.        
        ````
    ??? cite "Une explication en vidéo par Fred LELEU :"
        <figure>    
            <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/L5S8qjyG6xM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            <br>
            <figcaption markdown> [Les vidéos de Fred LELEU]{ target="_blank"}</figcaption>
            <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/oHN-qfeS7bk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </figure>
??? tip "Une image cliquable, support d'un lien  :"

    Il suffit de remplacer le texte support d'un lien hypertexte par le code MarDown d'une image tel que :
    
    ```md
    [![texte alternatif](adresse)](adresse "info-bulle")
    ```
    === "Rendu"
        [![polaroïd]{width=20%}](https://undraw.co/illustrations "Vers le site de unDraw"){target="_blank"}
    === "MarkDown"
        ```md
        [![polaroïd]{width=20%}](https://undraw.co/illustrations "Vers le site de unDraw"){target="_blank"}
        ```





??? tip "Des solutions pour centrer une image :"

    ??? example "Solution 1 : un code HTML..."

        === "Code"
            ```html
            <figure>
                <img src="../images/undraw_Polaroid.svg"  alt="Illustration d'une photo instantané" width="300" >
                <figcaption>
                    Un Polaroïd selon <a href="https://undraw.co/illustrations">unDraw</a>
                </figcaption>
            </figure>
            ```

        === "Rendu"
            <figure>
                <img src="../images/undraw_Polaroid.svg" alt ="Illustration d'une photo instantané" width="300" >
                <figcaption>
                    Un Polaroïd selon <a href="https://undraw.co/illustrations" target="_blank">unDraw</a>
                </figcaption>
            </figure>

        ??? note "Pour une largeur en %, l'image est décalée par rapport à sa légende..."
            
            === "Code"
                ```html
                <figure>
                    <img src="../images/undraw_Polaroid.svg" alt ="Illustration d'une photo instantané" width="50%" >
                    <figcaption>
                        Un Polaroïd selon <a href="https://undraw.co/illustrations">unDraw</a>
                    </figcaption>
                </figure>
                ```

            === "Rendu"
                <figure>
                    <img src="../images/undraw_Polaroid.svg" alt ="Illustration d'une photo instantané" width="50%" >
                    <figcaption>
                        Un Polaroïd selon <a href="https://undraw.co/illustrations" target="_blank">unDraw</a>
                    </figcaption>
                </figure>
                                
            Ce décalage n'apparait pas pour une largeur indiquée [en *px* ou en *em*](https://www.codeur.com/tuto/css/unite-de-mesure-taille-px-em-rem/){target="_blank"}.

        ??? cite "Une explication en vidéo par Fred LELEU :"
            <figure>    
                <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/rcAelt5wcUU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                <br>
                <figcaption markdown> [Les vidéos de Fred LELEU]{ target="_blank"}</figcaption>
            </figure>                

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
        ```md
        ![texte alternatif](adresse "info-bulle"){ .center }
        ```
        === "Rendu"
            ![polaroïd]{ width="30%" .center }

        === "Code"
            ```md
            ![polaroïd]{ width="30%" .center }  
            ```
        
        !!! note "Même avec une largeur en %, l'image est centrée mais il n'y a pas de légende centrée possible."
             

    ??? example "Solution 3 : un code hybride..."

        En plus de l'extension [attr_list](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#attribute-lists){target="_blank"} 
        qui permet de préciser des valeurs personnalisées aux attributs HTML et CSS, il faut également activer dans le fichier `mkdocs.yml` l'extension [md_in_html](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#markdown-in-html){ target=_blank} qui permet d'écrire du code MarkDown à l'intérieur de balises HTML :

        ```yaml
        markdown_extensions:
            - attr_list
            - md_in_html
        ```
        
        Comme pour la solution précédente, il faut ajouter la spécification CSS supplémentaire dans le fichier `docs/stylesheet/extra.css`
         (Merci à [Gilles](https://mooc-forums.inria.fr/moocnsi/t/mkdocs-astuce-pour-centrer-une-image-en-markdown-pur/2831){ target=_blank}) :

        ```css
        .center {
            display: block;
            margin: 0 auto;
        }
        ```

        Pour notre exemple, une syntaxe possible serait,
         sans oublier d'inscrire `markdown` dans les balises HTML qui contiendront du MarkDown :

        === "Code"
            ```html
            <figure markdown>
                ![polaroïd]{ width="50%" .center }
                <figcaption markdown>
                    Un Polaroïd selon [unDraw](https://undraw.co/illustrations){target="_blank"}
                </figcaption>
            </figure>            
            ```

        === "Rendu"
            <figure markdown>
                ![polaroïd]{ width="50%" .center }
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
