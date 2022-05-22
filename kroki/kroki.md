# Des graphiques avec Kroki

Le plugin [mkdocs-kroki](https://github.com/AVATEAM-IT-SYSTEMHAUS/mkdocs-kroki-plugin){target=_blank}
permet d'intégrer des images de diagrammes générés à partir d'une description textuelle
grace au service open source, libre de gratuit de [Kroki](https://kroki.io/){target=_blank}...

## Installation

Dans Visual Studio Code (VSC), ouvrir un nouveau Terminal (menu `Terminal > New Terminal`) pour saisir :
```bash
pip install mkdocs-kroki-plugin
```
Dans le dossier du projet, modifier les fichiers suivants tels que :
=== "`mkdocs.yml`"
    ```yaml hl_lines="5"
    plugins:
      - search
      - mkdocs-jupyter:
          include_source: True
      - kroki
    ```
=== "`ci.yml`"
    ```yaml hl_lines="17"
    name: ci
    on:
      push:
        branches:
          - main
    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - uses: actions/setup-python@v2
            with:
              python-version: 3.x      
          - run: pip install --upgrade pip
          - run: pip install mkdocs-material
          - run: pip install mkdocs-jupyter
          - run: pip install mkdocs-kroki-plugin
          # C'est ici qu'il faut ajouter si besoin
          # les instructions pour installer avec pip
          # les autres plugins MkDocs ou extensions MarkDown
          # souhaités pour le déploiement du site...

          - run: mkdocs gh-deploy --force
    ```
Au prochain redémarrage avec la commande `mkdocs serve` en local
 et au prochain déploiement distant sur GitHub le plugin mkdocs-kroki sera actif.

## Hello world :

Dans n'importe quel fichier `source.md` on peut alors, par exemple,
 saisir un code [GraphViz](https://graphviz.org/){target=_blank}
 pour intégrer un diagramme tel que :

=== "MarkDown saisi :"
    <pre><code>
    &grave;&grave;&grave;kroki-graphviz
    digraph G {Demat ->"d'an holl"}
    &grave;&grave;&grave;
    </code></pre>

=== "MarkDown généré :"
    ````md
    ```kroki-graphviz
    digraph G {Demat ->"d'an holl"}
    ```
    ````
=== "Rendu :"
    ```kroki-graphviz
    digraph G {Demat ->"d'an holl"}
    ```
    
!!! note "Remarques :"
    - On peut obtenir l'URL de l'image à intégrer dans un code [Markdown](../MarkDown-Mkdocs_Material/#image)
     directement depuis le site de [Kroki](https://kroki.io/#try){target=_blank} :

    <figure>
      <iframe src="https://kroki.io/#try" width="800" height="900"></iframe>
    </figure>

    - ==Le plugin mkdocs-kroki offre l'avantage d'intégrer le code source pour facilement le retoucher
     par la suite et ainsi apporter d'éventuelles modifications à l'image générée...==

## Exemples

Plusieurs [types de diagramme](https://kroki.io/#support) sont supportés et de nombreux exemples sont présentés à cette adresse : [https://kroki.io/examples.html](https://kroki.io/examples.html){target=_blank}...

!!! example "Chronogramme avec [WaveDrom](https://wavedrom.com/tutorial.html){target=_blank} :"
    === "MarkDown saisi :"
        <pre><code>
        &grave;&grave;&grave;kroki-wavedrom
        { signal: [
          { name: "A", wave: "0.|1." },
          { name: "B", wave: "01|.0" },
          { name: "OU exclusif", wave: "01|01" },
        ]}
        &grave;&grave;&grave;
        </code></pre>

    === "MarkDown généré :"
        ````md
        ```kroki-wavedrom
        { signal: [
          { name: "A", wave: "0.|1." },
          { name: "B", wave: "01|.0" },
          { name: "OU exclusif", wave: "01|01" },
        ]}
        ```
        ````
    === "Rendu :"
        ```kroki-wavedrom
        { signal: [
          { name: "A", wave: "0.|1." },
          { name: "B", wave: "01|.0" },
          { name: "OU exclusif", wave: "01|01" },
        ]}
        ```

!!! example "Carte mentale avec [PlantUML](https://plantuml.com/fr/mindmap-diagram){target=_blank} :"
    === "MarkDown saisi :"
        <pre><code>
        &grave;&grave;&grave;kroki-plantuml
        @startmindmap
        skinparam monochrome true
        + ADN - Tutoriel site web
        -- Créer, déployer puis maintenir son site
        --- Dans un navigateur
        --- Sur PC avec Visual Studio Code
        --- Sur iPad en ligne de commande
        ++ Coder pour générer ses pages web
        +++ MarkDown Mkdocs-Material, le contenu
        +++ YAML, la configuration
        +++ LaTeX, les sciences
        +++ Python, les macros
        -- Ressources
        ++ Annexes
        @endmindmap
        &grave;&grave;&grave;
        </code></pre>

    === "MarkDown généré :"
        ````md
        ```kroki-plantuml
        @startmindmap
        skinparam monochrome true
        + ADN - Tutoriel site web
        -- Créer, déployer puis maintenir son site
        --- Dans un navigateur
        --- Sur PC avec Visual Studio Code
        --- Sur iPad en ligne de commande
        ++ Coder pour générer ses pages web
        +++ MarkDown Mkdocs-Material, le contenu
        +++ YAML, la configuration
        +++ LaTeX, les sciences
        +++ Python, les macros
        -- Ressources
        ++ Annexes
        @endmindmap
        ```
        ````
    === "Rendu"
        > Ne s'affiche pas dans un onglet ! ???

```kroki-plantuml
@startmindmap
skinparam monochrome true
+ ADN - Tutoriel site web
-- Créer, déployer puis maintenir son site
--- Dans un navigateur
--- Sur PC avec Visual Studio Code
--- Sur iPad en ligne de commande
++ Coder pour générer ses pages web
+++ MarkDown Mkdocs-Material, le contenu
+++ YAML, la configuration
+++ LaTeX, les sciences
+++ Python, les macros
-- Ressources
++ Annexes
@endmindmap
```






--8<-- "includes/md/chantier.md"