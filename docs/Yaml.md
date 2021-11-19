
# YAML pour la configuration
## Introduction
Les fichiers de configuration du site `mkdocs.yml` et `ci.yml` sont écrits en [YAML]{target=_blank},
un langage avec une syntaxe la plus lisible possible par des humains pour représenter des données.

Aussi ce langage est largement utilisé par ailleurs comme par exemple en domotique pour la configuration
 du logiciel [Home Assistant](https://en.wikipedia.org/wiki/Home_Assistant){target="_blank"} :

<figure markdown>
  ![capture configuration.yaml](https://www.domotique123.fr/content/images/2021/05/xHome-Assistant-Yaml.jpg.pagespeed.ic.eiMdaVo9mc.webp){ width=70% .center }
  <figcaption markdown>
   exemple d’un fichier configuration.yaml pour [Home Assistant](https://www.domotique123.fr/presentation-dhome-assistant/){target="_blank"}
  </figcaption>
</figure>

***
## Notions de YAML utiles
- Les données sont sous la forme `:::yaml clé: valeur`, à raison d'un couple par ligne ;
```yaml
nom: toto
```
- Les commentaires sont signalés par le signe dièse `#` et se prolongent sur tout le reste de la ligne ;
```yaml
# Commentaire
salut: "Degemer mat" # Commentaire : bienvenue en Breton !
```
> Il est pratique de placer un `#` au début d'une ligne pour désactiver sa prise en compte ;
>
> Dans Visual Studio Code, la combinaison de touches ++ctrl+slash++ active/désactive une ligne de code...

- Les imbrications de la structure de données (tableau associatif, dictionnaire)
sont assurées par l'indentation :
```yaml
mon_dictionnaire:
    propriete_1: valeur  
    propriete_2: valeur
# ou
mon_dictionnaire_bis: {propriete_1: valeur, propriete_2: valeur }
# Comme en Python ? En fait, c'est au format JSON que YAML accepte.
```
- Les éléments d'une liste (tableau) sont dénotés par le tiret `-`, suivi d'une espace, à raison d'un élément par ligne :
```yaml
ma_liste:
- a
- b
- c
# ici l'indentation n'a pas d'importance
# ou
ma_liste_bis: [a,b,c]
# Comme en Python ? En fait, c'est au format JSON que YAML accepte.
```
- Toute valeur qui ne peut être convertie ni en entier,
ni en nombre à virgule flottante, ni en tout autre type reconnu par YAML
est interprétée comme une chaine de caractères.  
Pour éviter les situations ambiguës, les valeurs de type chaine de caractères (string)
peuvent être entourés de guillemets doubles `"`, ou simples `'` :
```yaml
key: "1234"
```
- Les valeurs booléennes sont `true` ou `false` (de préférence...) ;
- Un `~` représente une valeur `NULL` ;
- Un `>` permet d'écrire sur plusieurs lignes une valeur longue
 sans conserver les retours à la ligne :
```yaml
site_description: >
    Tutoriel pour créer et gérer un site web depuis un dépôt git 
    avec le framework material pour mkdocs et des notebook jupyter
```

??? cite "Ressources pour aller plus loin avec YAML : ..."
    - [Apprendre YAML en Y minutes](https://learnxinyminutes.com/docs/fr-fr/yaml-fr/){target="_blank"}
    - [Introduction à YAML](https://sweetohm.net/article/introduction-yaml.html){target="_blank"}
    - [Online YAML Parser](http://yaml-online-parser.appspot.com/){target="_blank"}
    - [YAML 1.2 Spec](https://yaml.org/spec/1.2.2/){target="_blank"}
    - [YAML Home Assistant](https://www.home-assistant.io/docs/configuration/yaml/){target="_blank"}

***
## Le fichier `ci.yml`

Le fichier `ci.yml` doit être placé dans une arborescence de répertoires nommés `.github/workflows/ci.yml`.

Les données qu'il contient sont destinées à configurer le bot de GitHub avec toutes les applications logicielles,
 les plugins MkDocs et les extensions MarkDown, nécessaires pour qu'il puisse créer et mettre à jour automatiquement[^ci]
la branche `gh-pages` à partir du contenu de la branche `main` à chaque changement (commit + push).

[^ci]:
    [GitHub Actions](https://fr.github.com/features/actions){target=_blank}
    gère le déploiement du site par intégration continue (CI = Continuous Intégration).

??? example "Exemple pour ce site : ..."
    ```yaml hl_lines="5 16"
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
          # C'est ici qu'il faut ajouter si besoin
          # les instructions pour installer avec pip
          # les autres plugins MkDocs ou extensions MarkDown
          # souhaités pour le déploiement du site...

          - run: mkdocs gh-deploy --force
    ```
    Ce code correspond à celui proposé dans la [documentation MkDocs-Material](
    https://squidfunk.github.io/mkdocs-material/publishing-your-site/#with-github-actions){target=_blank}
    si ce n'est :
    
    - la suppression de l'item `- master` car la branche par défaut du projet est ici la branche `main` ;
    - l'ajout de l'item `:::yaml - run: pip install mkdocs-jupyter`
    qui installe le plugin [mkdocs-jupyter](#mkdocs-jupyter)
    pour ajouter directement des fichiers `.ipynb` et `.py` comme nouvelles pages du site...

***
## Le fichier `mkdocs.yml`

Les données de ce fichier définissent la configuration du site web afin de personnaliser son style, son organisation, ses fonctionnalités et son comportement...

### Configuration minimale
Au minimum, ce fichier de [configuration pour MkDocs](https://www.mkdocs.org/user-guide/configuration/#configuration){target="_blank"} doit contenir les deux paramètres :

- [`site_name:`](https://www.mkdocs.org/user-guide/configuration/#site_name){target="_blank"}
une chaine de moins de 70 caractères définissant le titre du site qui s'affichera dans l'onglet du navigateur :
??? example "Exemple extrait du fichier `mkdocs.yml` de ce site : ..."
    === "Ce code YAML :"
        ```yaml
        site_name: ADN - Tutoriel site web
        ```
    === "génère le code HTML :"
        ```html
        <head>
            <title>ADN - Tutoriel site web</title>
        </head>
        ```  
- [`site_url:`](https://www.mkdocs.org/user-guide/configuration/#site_url){target="_blank"}
l'adresse web principale de publication du site : 
??? example "Exemple extrait du fichier `mkdocs.yml` de ce site : ..."
    === "Ce code YAML :"
        ```yaml
        site_url: https://ericecmorlaix.github.io/adn-Tutoriel_site_web/
        ```
    === "génère le code HTML :"
        ```html
        <head>
            <link rel="canonical" href="https://ericecmorlaix.github.io/adn-Tutoriel_site_web/">
        </head>
        ```  

??? cite "Une explication en vidéo par Fred LELEU :"
    <figure>    
        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/K6l-5TCORMg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        <br>
        <figcaption markdown> [Les vidéos de Fred LELEU]{ target="_blank"}</figcaption>        
    </figure>

Tous les autres paramètres sont facultatifs mais ils apportent des fonctionnalités intéressantes...

### Dépôt
- [repo_url:](https://www.mkdocs.org/user-guide/configuration/#repo_url){target="_blank"}
ajoute en haut à droite de chaque page du site, icône, nom et lien vers le dépôt GitHub du projet. 
- [repo_name:](https://www.mkdocs.org/user-guide/configuration/#repo_name){target="_blank"}
personnalise le nom générique "GitHub" donné par défaut au lien vers le dépôt GitHub du projet. 
- [edit_uri:](https://www.mkdocs.org/user-guide/configuration/#edit_uri){target="_blank"}
complément au chemin pour aller depuis la valeur de `repo_url:` jusqu'au répertoire `docs` ;  
Ce qui permet avec MkDocs-Material d'ajouter un bouton (crayon) d'édition du code `source.md` d'une page du site depuis le navigateur :
    - `edit/main/docs/` permet l'édition moyennant une connexion ;
    - `blob/main/docs/` comme `tree/main/docs/` donne un accès anonyme en lecture.

??? example "Exemple extrait du fichier `mkdocs.yml` de ce site : ..."
    ```yaml
    repo_url: https://github.com/ericECmorlaix/testMkDocsAdN/
    repo_name: adn-Tutoriel_site_web
    edit_uri: edit/main/docs/
    ```
### Métadonnées
On peut configurer l'ajout de [métadonnées](https://www.netoffensive.blog/referencement-naturel/bien-referencer-site/on-site/redaction-web/balises-metas/){target="_blank"} de description, moins de 300 caractères, et d'auteur pour toutes les pages du site :

- [site_description:](https://www.mkdocs.org/user-guide/configuration/#site_description){target="_blank"}
- [site_author:](https://www.mkdocs.org/user-guide/configuration/#site_author){target="_blank"}

??? example "Exemple extrait du fichier `mkdocs.yml` de ce site : ..."
    === "Ce code YAML :"
        ```yaml
        site_description: >
            Tutoriel pour créer et gérer un site web depuis un dépôt git
            avec le framework material pour mkdocs et des notebook jupyter
        site_author: "Eric MADEC"
        ```
    === "génère le code HTML :"
        ```html
        <head>
            <meta name="description" content="Tutoriel pour créer et gérer un site web depuis un dépôt git avec le framework material pour mkdocs et des notebook jupyter">      
            <meta name="author" content="Eric MADEC">
        </head>
        ```
??? tip "Spécifier des métadonnées pour une page en particulier : ..."
    
    Il faut activer dans le fichier `mkdocs.yml` l'extension
     [meta](https://squidfunk.github.io/mkdocs-material/reference/meta-tags){target=_blank} :

    ``` yaml
    markdown_extensions:
        - meta        
    ```

    On peut alors ajouter dans l'en tête d'un fichier `source.md` :

    - un [titre](https://squidfunk.github.io/mkdocs-material/reference/meta-tags/#setting-the-page-title){target=_blank}
    spécifique qui ne s'affichera dans l'onglet du navigateur que pour cette page ;

    - une [description](https://squidfunk.github.io/mkdocs-material/reference/meta-tags/#setting-the-page-description){target=_blank} différente de celle commune aux autres pages du site.

    ??? example "Exemple extrait du fichier source `MarkDown-Mkdocs_Material.md` de ce site : ..."
        === "Ce code YAML dans l'en tête du fichier MarkDown :"
            ```yaml
            ---
            description: Page en Français décrivant l'utilisation du MarkDown de MkDocs avec le thème Material pour produire une documentation web.
            title: Le MarkDown avec Mkdocs-Material
            ---
            ## Introduction
            ```
        === "génère le code HTML :"
            ```html
            <head>
                <meta name="description" content="Page en Français décrivant l'utilisation du MarkDown de MkDocs avec le thème Material pour produire une documentation web.">
                <title>Le MarkDown avec Mkdocs-Material - ADN - Tutoriel site web</title>
            </head>
            ```
        === "au lieu du code HTML :"
            ```html
            <head>
                <meta name="description" content="Tutoriel pour créer et gérer un site web depuis un dépôt git avec le framework material pour mkdocs et des notebook jupyter">
                <title>MarkDown Mkdocs-Material, le contenu - ADN - Tutoriel site web</title>
            </head>
            ```

    !!! note ""
        Par ailleurs l'activation de l'extension `:::yaml meta` permet aussi [d'activer/désactiver l'affichage du menu de navigation latéral et/ou de la table des matières][meta]{target=_blank}
        ??? example "C'est le cas de la page d'accueil de ce site : ..."
            ```md hl_lines="1-5"
            --8<-- "docs/index.md"
            ```

??? tip "Ajouter des métadonnées ou d'autres balises personnalisées : ..."

    Pour inclure des [balises customisées](https://squidfunk.github.io/mkdocs-material/reference/meta-tags/#customization){target=_blank} entre les balises `<head></head>` d'une ou de toutes les pages du site, il faut créer à la racine du projet dans un dossier nommé [`overrides`](https://squidfunk.github.io/mkdocs-material/customization/?h=overr#extending-the-theme){target=_blank} un fichier `main.html` et déclarer ce dossier en tant que `custom_dir:` dans le paramétrage de `theme:`...


### Stucture de navigation

L'organisation et le contenu du menu principal de navigation du site sont définis par la valeur associée au paramètre [`nav:`](https://www.mkdocs.org/user-guide/configuration/#nav){target=_blank}.

Tous les chemins menant aux fichiers à inclure dans cette navigation doivent être relatifs à la valeur de la clé [`docs_dir`](https://www.mkdocs.org/user-guide/configuration/#docs_dir){target=_blank} qui est le dossier `docs` par défaut.

On peut également inclure des liens absolus vers des sources externes.

??? example "Exemple extrait du fichier `mkdocs.yml` de ce site : ..."
    ```yaml
    # Dossier source, chemin relatif au fichier mkdocs.yml
    docs_dir: docs
    # Structure du menu principal de navigation, chemins relatifs au dossier source docs_dir
    nav: 
    - Accueil: index.md
    - Créer, déployer puis maintenir son site:
        Dans un navigateur: PremiersPas.md
        Sur PC avec Visual Studio Code: PCW10-VSC.md
        Sur iPad en ligne de commande: iPad.md
    - Coder pour générer ses pages web:
        MarkDown Mkdocs-Material, le contenu: MarkDown-Mkdocs_Material.md
        YAML, la configuration: Yaml.md
        LaTeX, les sciences: LaTeX.md
        Python, les macros: Python.md
    - Ressources : Ressources.md    
    ```

??? cite "Une explication en vidéo par Fred LELEU :"
    <figure>    
        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/4fdmO-n37Gg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        <br>
        <figcaption markdown> [Les vidéos de Fred LELEU]{ target="_blank"}</figcaption>        
    </figure>

!!! note "Remarque :"
    Toutes les `fichier.md` non répertoriés dans la configuration de navigation seront toujours convertis et inclus dans le site construit, cependant, les pages ainsi générées ne seront pas liées à partir de la navigation globale et ne seront pas incluses dans les liens de navigation en fin de page **_Précédent_** et **_Suivant_**. Ces pages resteront "cachées" à moins qu'elles ne soient directement associées à un lien hypertexte comme c'est le cas dans ce site pour la page [iSH Shell](../iSH_Shell){target="_blank"}. Néanmoins, on les trouve très facilement grace à la [barre de recherche](#recherche)

### Thème

Il suffit de changer la valeur de la clé [`name:`](https://www.mkdocs.org/user-guide/configuration/#name){target=_blank} pour changer radicalement l'allure d'un site de documentation.  
[MkDocs]{target=_blank} inclut deux [thèmes de base](https://www.mkdocs.org/user-guide/choosing-your-theme/){target=_blank} mais de nombreux [autres thèmes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes){target=_blank} existent qu'il suffit d'essayer...

Le choix du thème nommé `material` permet de préciser des paramètres imbriqués de configuration tels que :

- les [couleurs](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/){target=_blank} ;
- les [polices de caractères](https://squidfunk.github.io/mkdocs-material/setup/changing-the-fonts/){target=_blank} ;
- la [langue](https://squidfunk.github.io/mkdocs-material/setup/changing-the-language/){target=_blank} ;
- les [icônes](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/){target=_blank} ;
- la [navigation](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/){target=_blank} ;

??? example "Exemple extrait du fichier `mkdocs.yml` de ce site : ..."
    ```yaml
    --8<-- "includes/yml/theme.yml"
    ```
### Extensions MarkDown :

Il s'agit principalement des extensions à déclarer pour autoriser les fonctions de balisage présentées à la page [MarkDown Mkdocs-Material](./MarkDown-Mkdocs_Material.md).

??? example "Exemple extrait du fichier `mkdocs.yml` de ce site : ..."
    ```yaml
    --8<-- "includes/yml/extension.yml"
    ```
    
### Plugins
#### Recherche
On peut ajouter et configurer un plugin pour inclure
 une barre de [recherche](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-search/){target=_blank}.

#### MkDocs-Jupyter

En activant le plugin [mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter){target=_blank}
 dans le fichier de configuration `mkdocs.yml`,
  tous les fichiers `.ipynb` et `.py` placés dans le dossier `docs` seront convertis en page web
   de la même facon qu'un fichier `source.md`.  
Ces pages peuvent alors être déclarées dans la
 [configuration de la stucture de navigation](#configuration-de-la-stucture-de-navigation){target=_self}.

Différentes options existent autre que `:::yaml include_source: True` qui crée une copie du fichier
 `source.ipynb` (ou `.py`) dans le dossier de la page sur le site pour permettre son téléchargement.

Pour afficher un bouton de téléchargement du fichier `source.ipynb` (ou `.py`) et obtenir un style d'affichage proche de l'affichage classique d'un notebook, il faut créer à la racine du projet dans un dossier nommé [`overrides`](https://squidfunk.github.io/mkdocs-material/customization/?h=overr#extending-the-theme) un fichier `main.html` et déclarer ce dossier en tant que `custom_dir:` dans le paramétrage de `theme:`.

=== "dans mkdocs.yml"
    ```yaml
    nav:
    - Accueil: index.md
    - Notebook: notebook.ipynb
    - Python: python_script.py

    plugins:
    - mkdocs-jupyter:
        include_source: True
    ```
=== "dans overrides/main.html"
    ```html
    {% extends "base.html" %}    
    {% block content %}
    {% if page.nb_url %}
        <a href="{{ page.nb_url }}" title="Download" class="md-content__button md-icon">
            {% include ".icons/material/download.svg" %}
        </a>
    {% endif %}
    {{ super() }}
    <style>
        .jp-RenderedHTMLCommon p {
            font-size: 0.8rem;
            line-height: 1.6;
        }
        .jp-RenderedHTMLCommon li {
            font-size: .8rem;
            line-height: 1.6;
        }
        .jp-RenderedHTMLCommon h1 {
            margin: 0 0 1.25em;
            color: var(--md-default-fg-color--light);
            font-weight: 300;
            font-size: 2em;
            line-height: 1.3;
            letter-spacing: -0.01em;
        }
        .jp-RenderedHTMLCommon h2 {
            margin: 1.6em 0 .64em;
            font-weight: 300;
            font-size: 1.965em;
            line-height: 1.4;
            letter-spacing: -0.01em;
        }
        .jp-RenderedHTMLCommon h3 {
            margin: 1.6em 0 .8em;
            font-weight: 400;
            font-size: 1.57em;
            line-height: 1.5;
            letter-spacing: -0.01em;
        }
        .jp-RenderedHTMLCommon hr {
            border: none;
        }
    </style>
    {% endblock content %}
    ```
### Pied de page
#### Licence
- [copyright:](https://www.mkdocs.org/user-guide/configuration/#copyright){target="_blank"} information de droit d'auteur qui s'affiche dans le pied de page pour toutes les pages du site
??? example "Exemple extrait du fichier `mkdocs.yml` de ce site : ..."
    === "Ce code YAML :"
        ```yaml
        copyright: >
            Document partagé par <a href="https://github.com/ericECmorlaix" target="_blank">Eric MADEC</a>
            &copy; 2021 sous licence <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr" target="_blank">CC BY-NC-SA 4.0</a>
            <br> Illustrations par <a href="https://undraw.co/" target="_blank">UnDraw</a>
        ```
    === "génère le code HTML :"
        ```html
        <div class="md-footer-copyright__highlight">
            Document partagé par <a href="https://github.com/ericECmorlaix" target="_blank">Eric MADEC</a> &copy; 2021 sous licence <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr" target="_blank">CC BY-NC-SA 4.0</a> <br> Illustrations par <a href="https://undraw.co/" target="_blank">UnDraw</a>
        </div>
        ```
#### Liens sociaux
- [social:](https://squidfunk.github.io/mkdocs-material/setup/setting-up-the-footer/#social-links){target="_blank"} permet d'afficher dans le pied de page pour toutes les pages du site des icônes support de liens sociaux.

??? example "Exemple extrait du fichier `mkdocs.yml` de ce site : ..."
    === "Ce code YAML :"
        ```yaml
        extra:
        social: 
            - icon: fontawesome/solid/paper-plane
            link: "mailto:eric.madec@ecmorlaix.fr?subject=ADN - Tutoriel documentation web&body=Votre question : ..."
            name: Pour toute question, suggestion ou commentaire, écrire à l'auteur
            - icon: fontawesome/brands/github
            link: https://github.com/ericECmorlaix/adn-Tutoriel_site_web
            name: dépôt github
            - icon: fontawesome/solid/university
            link: https://www.ecmorlaix.fr/nos-etablissements/lycee-notre-dame-du-mur/
            name: Lycée Notre Dame du Mur
        ```
***
--8<-- "includes/md/chantier.md"
--8<-- "includes/md/abr_ref.md"