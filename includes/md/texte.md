=== "Rendu"
    --8<-- "includes/md/texteIn.md"
=== "MarkDown"
    ```md
    --8<-- "includes/md/texteIn.md"
    ```

??? tip "Astuces pour obtenir au clavier les caractères spéciaux comme `~` ou `` ` ``: ..." 
    - Le [tilde](https://fr.wikipedia.org/wiki/Tilde){ target=_blank} s'obtient avec la combinaison de touches ++"AltGr"+"é"++ ;
    - L'[accent grave](https://fr.wikipedia.org/wiki/Accent_grave){ target=_blank} s'obtient avec la combinaison de touches ++"AltGr"+"è"++ ; 

??? info 
    Il faut activer dans le fichier `mkdocs.yml` les extensions :

    ```yaml
    markdown_extensions:
        - pymdownx.caret
        - pymdownx.mark
        - pymdownx.tilde
    ```

    - [pymdownx.caret](https://facelessuser.github.io/pymdown-extensions/extensions/caret){ target=_blank} pour `^^souligné^^` ou mettre en `^exposant^`;
    - [pymdownx.mark](https://facelessuser.github.io/pymdown-extensions/extensions/mark/){ target=_blank} pour `==surligné==`;
    - [pymdownx.tilde](https://facelessuser.github.io/pymdown-extensions/extensions/tilde/){ target=_blank} pour `~~barré~~` ou mettre en `~indice~`.