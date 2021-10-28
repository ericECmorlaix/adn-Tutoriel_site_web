???+ warning inline end "ATTENTION !"
    
    **Toto** est dans la place...

    *Ceci est une mise en garde,
     vous voilà prévenu !!*
Une caractéristique remarquable de MkDocs avec Material sont ces admonitions : ce sont des boites colorées d'avertissements, pour des alertes, mises en garde et autres appartés, qui viennent compléter le flux normal de l'information sur une page web de documentation pour illustrer ou souligner un point particulier, une difficulté...

De base, il existe [12 styles de boites](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types){ target=_blank} différentes définies par des noms de types. Si aucun de ces mots clés types n'est précisé, ou si le mot clé n'est pas reconnu, c'est le type `note` qui sera utilisé par défaut.
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

    Pour permettre les fonctionnalités des [boites d'avertissement](https://squidfunk.github.io/mkdocs-material/reference/admonitions/){ target=_blank} décrites ci-dessus,
     il faut activer dans le fichier `mkdocs.yml` les extensions :

    ```yaml
    markdown_extensions:
      - admonition              
      - pymdownx.details        
      - pymdownx.superfences    
    ```
???+ tip "Des boites très personnalisées : ..."

    En attendant qu'il soit possible de choisir
     des [icones](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#admonition-icons){ target=_blank}
     personnalisés pour chaque type de boite d'avertissement,
      on peut déjà [customiser](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#customization){ target=_blank}
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
