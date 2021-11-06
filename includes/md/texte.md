=== "Rendu"
    --8<-- "includes/md/texteIn.md"
=== "MarkDown"
    ```md
    --8<-- "includes/md/texteIn.md"
    ```

??? tip "Complément pour ajouter des marquages et commentaires de révision : ..."

    === "Rendu Texte"
        --8<-- "includes/md/texteInIn.md"
    === "Rendu Code"
        ```
        --8<-- "includes/md/texteInIn.md"
        ```           
    === "MarkDown"
        ![Code markDown de marquage de Texte & Code](https://ericecmorlaix.github.io/adn-Tutoriel_site_web/images/MarkDownMarquageTexte&Code.png)


??? tip "Astuces pour obtenir au clavier les caractères spéciaux comme `~`, `` ` ``, `{`ou `}`: ..." 
    - Le [tilde](https://fr.wikipedia.org/wiki/Tilde){ target=_blank} s'obtient avec la combinaison de touches ++altgr+"é"++ ;
    - L'[accent grave](https://fr.wikipedia.org/wiki/Accent_grave){ target=_blank} s'obtient avec la combinaison de touches ++altgr+"è"++ ;
    - Les [accolades](https://fr.wikipedia.org/wiki/Accolade){ target=_blank} (braces) ouvrante et fermante s'obtiennent respectivement avec les combinaisons de touches ++altgr+"'"++ et ++altgr+"="++  

??? info 
    Il faut activer dans le fichier `mkdocs.yml` les extensions :

    ```yaml
    markdown_extensions:
        - pymdownx.caret
        - pymdownx.mark
        - pymdownx.tilde
        - pymdownx.critic
    ```

    - [pymdownx.caret](https://facelessuser.github.io/pymdown-extensions/extensions/caret){ target=_blank} pour `^^souligné^^` ou mettre en `^exposant^`;
    - [pymdownx.mark](https://facelessuser.github.io/pymdown-extensions/extensions/mark/){ target=_blank} pour `==surligné==`;
    - [pymdownx.tilde](https://facelessuser.github.io/pymdown-extensions/extensions/tilde/){ target=_blank} pour `~~barré~~` ou mettre en `~indice~` ;
    - [pymdownx.critic](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#critic){ target=_blank} pour du {++marquage++} et des {>> commentaires <<} de révision.