??? example "Exemple version basique : ..."
    === "MarkDown"
        ```md
        Aligné à gauche | Aligné à droite | Texte centré | Défaut
        :---|---:|:---:|---
        abcdef | 1234 | xyz | etc
        ghi jkl mno pqr | 567890 | ........ | etc        
        ```
    === "Rendu"
        Aligné à gauche | Aligné à droite | Texte centré | Défaut
        :---|---:|:---:|---
        abcdef | 1234 | xyz | etc
        ghi jkl mno pqr | 567890 | ........ | etc

La syntaxe de ce type de tableau est très naturelle et légère.

Le type d’alignement dans chaque colonne (à gauche, à droite, centré) est défini dans la seconde ligne par la position du caractère double point `:` relativement aux tirets `-`.

Afin d'améliorer la lecture d'un tableau en mode éditon de code,
 on peut débuter et terminer chaque ligne par une barre verticale `|`,
  mais ce n’est pas obligatoire,
   et aussi ajouter des tirets et des espaces supplémentaires.  
Le nombre de tirets dans la seconde ligne n’est pas significatif.
??? example "Exemple version plus esthétique : ..."
    === "MarkDown"
        ```md
        | Aligné à gauche | Aligné à droite | Texte centré | Défaut |
        |:----------------|----------------:|:------------:|--------|
        | abcdef          |            1234 |      xyz     | etc    |
        | ghi jkl mno pqr |          567890 |   ........   | etc    |
        ```
    === "Rendu"
        | Aligné à gauche | Aligné à droite | Texte centré | Défaut |
        |:----------------|----------------:|:------------:|--------|
        | abcdef          |            1234 |      xyz     | etc    |
        | ghi jkl mno pqr |          567890 |   ........   | etc    |

??? tip "Astuces pour obtenir au clavier le caractère spécial `|` : ..." 
    - La [barre verticale](https://fr.wikipedia.org/wiki/Barre_verticale){ target=_blank}, également nommée tube ou pipe de l'Anglais, s'obtient avec la combinaison de touches ++"AltGr"+"6"++ ;    

??? tip "Solution pour centrer un tableau et lui ajouter une légende : ..."

    === "MarkDown"
        ```md
        <figure markdown>
            
          Aligné à gauche | Aligné à droite | Texte centré | Défaut
          :---|---:|:---:|---
          abcdef | 1234 | xyz | etc
          ghi jkl mno pqr | 567890 | ........ | etc
            
          <figcaption markdown>
            _Légende du **tableau**_
          </figcaption>
        </figure>
        ```
    === "Rendu"
        <figure markdown>
            
          Aligné à gauche | Aligné à droite | Texte centré | Défaut
          :---|---:|:---:|---
          abcdef | 1234 | xyz | etc
          ghi jkl mno pqr | 567890 | ........ | etc
            
          <figcaption markdown>
            _Légende du **tableau**_
          </figcaption>
        </figure>            

??? tip "Générer le code MarkDown d'un tableau : ..."

    On peut avantageusement utiliser :
    
    - un [générateur de tableau en ligne](https://www.tablesgenerator.com/markdown_tables){ target=_blank} ;

    - Ou un script Python personnel... ;

    !!! example "Exemple : "
        ```py
        from IPython.display import Markdown
        chaine = "| d | b | h |" + "\n"
        chaine += "|:-:" * 3 + "|" + "\n"
        for i in range(16) :
            chaine += f"| {i} | {bin(i)} | {hex(i)} |" + "\n"
        Markdown(chaine)
        ``` 

??? todo "A tester : ..."
     [Tri de tableau](https://squidfunk.github.io/mkdocs-material/reference/data-tables/#sortable-tables){target=_blank}