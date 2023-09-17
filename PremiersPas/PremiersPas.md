# Premiers pas depuis un navigateur web

## Se connecter à GitHub

**Créer** un compte sur GitHub (Sign up) depuis un navigateur à l'adresse [https://github.com/](https://github.com/) :

    <img class="center" src="https://ericecmorlaix.github.io/img/GitHub00a.png" width=55% alt="inscription GitHub">
 
Ou **identifier** vous (Sign in) si vous avez déjà un compte :

   <img class="center" src="https://ericecmorlaix.github.io/img/GitHub00b.png" width=45% alt="identification GitHub" >

## Créer un nouveau dépôt à partir d'un template

**Créer** un nouveau dépôt GitHub à partir du modèle [base_mkdocs_material](https://ericecmorlaix.github.io/base_mkdocs_material/){target=_blank} en cliquant sur le bouton "==Use this template==" ou tout simplement en cliquant sur [ce lien](https://github.com/ericECmorlaix/base_mkdocs_material/generate) ;

<img class="center" src="https://ericecmorlaix.github.io/adn-Tutoriel_Obsidian/assets/Use_this_template.png" width=90% alt="Use_this_template GitHub" >


- **Donner** un nom à votre dépôt public sachant que par défaut votre site sera publié à une adresse au format <https://votre-pseudo-github.github.io/nom-depot/> ;
- **ajouter** une description ;
-  **ne copier que** la branche `main` du dépôt template ;
- enfin **cliquer** sur le bouton "==Create repository from template==".

 
!!! success "Voilà !"
    Vous faites maintenant parti d'un autre [réseau social mondial celui des développeurs de code](https://medium.com/coding-days/focus-sur-github-le-r%C3%A9seau-social-des-d%C3%A9veloppeurs-165a2978ea9e)...  

## Modifier le fichier `README.md`  

> Le fichier `README` est la vitrine de votre dépôt GitHub, il a pour extension `.md` pour [**MarkDown**](https://fr.wikipedia.org/wiki/Markdown){target=_blank}, un langage de balisage léger qui est ici, à quelques spécificités près, le même que celui que vous utilisez pour rédiger vos fichiers `notebook.md` de [Jupyter](https://ericecmorlaix.github.io/adn-Tutoriel_lab_si/notebook/){target=_blank} et `note.md` d'[Obsidian](https://ericecmorlaix.github.io/adn-Tutoriel_Obsidian/){target=_blank}.  
> C'est ce langage de description rudimentaire que nous utiliserons principalement pour rédiger nos futures pages web.  
> Il existe plusieurs versions de ce langage qui, à partir d'une syntaxe de base commune, possèdent d'autres éléments additionnels spécifiques...
 
- **Cliquer** sur le crayon pour ouvrir le fichier `README.md`dans l'éditeur en ligne :
 <img class="center" src="https://ericecmorlaix.github.io/img/GitHub02bis.png" alt="editer README" width=75%>
  
- **Modifier** son contenu en utilisant la syntaxe [MarkDown à la sauce GitHub](https://guides.github.com/features/mastering-markdown/){target=_blank} :
<img class="center" src="https://ericecmorlaix.github.io/img/GitHub03bis.png" alt="modifier README" width=75%>

> l'onglet `Preview` permet de visualiser le résultat avant sa publication...

- **Publier** la nouvelle version du fichier `README.md` en décrivant vos modifications dans un message et puis en cliquant sur le bouton `Commit changes` :
<img class="center" src="https://ericecmorlaix.github.io/img/GitHub04bis.png" alt="publier README" width=75%>

!!! success "**Waouh !**"
    Vous venez de faire votre premier [**Commit**](https://fr.wikipedia.org/wiki/Commit){target=_blank} **!**

!!! note "Remarque"
    Nous allons bientôt voir qu'il est également possible d'éditer ce fichier `README.md` facilement dans [Visual Studio Code pour le web](https://vscode.dev/){target=_blank}...

## Déployer votre site

!!! success ""
    Normalement, le "bot" de GitHub doit avoir généré à partir de votre branche `main`, une seconde branche nommée `gh-pages` :
    <img class="center" src="https://ericecmorlaix.github.io/img/GitHub07bis.png" alt="branche" width=40%>

- **Cliquer** sur les onglets `Settings` (1) puis `Pages` (2), **sélectionner** la branche `gh-pages` (3) enfin **cliquer** sur le bouton `Save` (4) :
 <img class="center" src="https://ericecmorlaix.github.io/img/GitHub08bis.png" alt="Déploiement" width=90%>

!!! success ""
    Au bout d'un moment, si tout se passe bien, votre site devrait être visible sur le web à une adresse au format <https://votre-pseudo-github.github.io/nom-depot/>...

## Maintenir votre site avec Visual Studio Code en ligne

Vous disposez maintenant d'un site web généré avec le framework MkDocs et le thème Material qui est publié sur un de vos dépots GitHub.

Pour éditer facilement vos fichiers avec l'[IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement){target=_blank} Visual Studio Code dans un navigateur et ainsi développer et maintenir des dépôts GitHub depuis n’importe quelle machine sans installation locale plusieures solutions s'offrent à nous :

??? tip "Une version allégée de VS Code s'exécutant entièrement dans votre navigateur"
    > Une fois toutes les fonctionnalités de sa page web chargée, l'outil de développement peut fonctionner entièrement sans serveur dans le navigateur mais le terminal et le débogueur ne seront pas disponibles. Donc, par exemple :
    >
    >- Pour exécuter le code d'une cellule python d'un notebook il faut recourir à l'extension [vscode-pyodide](https://marketplace.visualstudio.com/items?itemName=joyceerhl.vscode-pyodide){target=_blank}...  
    >- Il n'est pas possible de prévisualiser en local le rendu d'un site avec la commande `mkdocs serve`...
    

    === "vscode.dev"

        - Depuis l’affichage d’un dépôt GitHub dans un navigateur, il suffit d’insérer `vscode.dev/` devant l’URL pour ouvrir ce dépôt dans l’interface VSCode pour le web...
        - OU depuis l'adresse [https://vscode.dev/](https://vscode.dev/){target=_blank} cliquer sur le bouton `Ouvrir un référentiel distant` et suivre les instructions...
        
    === "github.dev"

        - Depuis l’affichage d’un dépôt GitHub dans un navigateur, il suffit :
            - d’enfoncer les touches d'un clavier ++"Maj"+"."++ ;
            - ou de changer le `github.com` en `github.dev` dans l’URL pour ouvrir ce dépôt dans l’interface VSCode pour le web...

        ![github dev](https://user-images.githubusercontent.com/856858/130119109-4769f2d7-9027-4bc4-a38c-10f297499e8f.gif){.center width=60%}

        - OU depuis l'adresse [https://github.dev/](https://github.dev/){target=_blank} cliquer sur le bouton `GitHub` en bas à gauche et choisir `Ouvrir le dépôt/référentiel distant` et suivre les instructions...


??? tip "Piloter un serveur distant depuis votre navigateur pour y exécuter VS Code"

    Solution plus énergivore car fonctionnant dans le cloud mais plus puissante et complète...

    ===  "[Codespaces](https://github.com/features/codespaces){target=_blank}"
        
        - A la racine de votre dépot GitHub **cliquer** sur le bouton vert `<> Code` puis choisir l'onglet `Codespaces` et enfin **cliquer** sur le bouton vert `Create codespace on main` 

        <figure>
        <img src="https://ericecmorlaix.github.io/img/Codespaces00.png" alt="Codespaces">
        </figure> 

    === "[Gitpod](https://www.gitpod.io/){target=_blank}"

        - Sur le site [Gitpod](https://www.gitpod.io/){target=_blank}, **signer** avec votre compte GitHub ;
        - **Choisir** VS Code BROWSER ;
        - **Cliquer** sur `New Workspace` ;
        - **Rechercher** puis choisir votre dépot dans la liste...


<!-- Lire la page vscode.dev Visual Studio Code pour le Web ou regarder la vidéo https://www.youtube.com/live/sy3TUb_iVJM?feature=shared 

-	Extensions pour VSCode récemment découverte :
o	VSCode Pyodide https://marketplace.visualstudio.com/items?itemName=joyceerhl.vscode-pyodide
o	MPE https://shd101wyy.github.io/markdown-preview-enhanced/#/vscode-installation
o	Wikilens WikiLens - Visual Studio Marketplace
o	CodeSwing https://marketplace.visualstudio.com/items?itemName=codespaces-Contrib.codeswing
o	Luna Paint Luna Paint — Image Editor - Visual Studio Marketplace
o	Code Tour CodeTour - Visual Studio Marketplace
-->

Tous les dossiers et fichiers de votre dépot sont alors éditables dans l'environnement de développement intégré Visual Studio Code en ligne.

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitPod01.png" alt="GitPod VSC Explorer">
</figure>

### ==La routine pour maintenir votre site GitHub avec un éditeur VSC en ligne se résume à :==

??? summary "I - Modifier vos fichiers :"
    Depuis l'Explorateur (`Explorer` ++"Ctrl"+"Maj"+"E"++) de VSC (_bleu_) :

    - cliquer sur un dossier pour afficher la liste de son contenu ;
    - cliquer sur les icônes (_jaunes_) pour créer un nouveau fichier et/ou un nouveau dossier ;
    - maintenir le clic sur un fichier (ou un dossier) pour le déplacer dans l'arborescence ;
    - cliquer sur un fichier pour l'ouvrir dans l'éditeur afin de le modifier ;
    - cliquer droit sur un fichier `.md` et choisir `Open preview` pour le prévisualiser ;

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitPod02.png" alt="GitPod VSC Explorer">
</figure>


??? summary "II - Indexer vos changements :"
    Depuis le "Contrôle de code source" (_vert_) (`Source Control` ++"Ctrl"+"Maj"+"G"++),
     dans "Changements" (`Changes`) cliquer sur le `+` (_orange_) pour ajouter les fichiers modifiés
      à mettre en attente (indexer) dans cette phase (stage) de développement ;

??? summary "III - Committer, valider vos modifications :"
    Ajouter un message sous "CONTRÔLE DE CODE SOURCE" (`SOURCE CONTROL`) (_rose_)
     pour définir ces modifications à ce stade de votre développement,
      puis cliquer sur `✓` (_violet_) pour valider ce commit ;

??? summary "IV - Pousser les modifications vers votre dépôt distant :"
    Cliquer sur les `...` en face de `CONTRÔLE DE CODE SOURCE`
    et choisir `Push` ;


## Configurer votre site

Les fichiers de configuration du site `mkdocs.yml` et `ci.yml` sont écrits en [YAML](https://fr.wikipedia.org/wiki/YAML), un langage avec une syntaxe la plus lisible possible par des humains pour représenter des données. 

**Modifier** ces fichiers de configuration pour les personnaliser :

- Sauf à vouloir ajouter de nouvelles fonctionnalités, le fichier [`CI.yml`](https://ericecmorlaix.github.io/adn-Tutoriel_site_web/Yaml/#le-fichier-ciyml) peut rester inchangé ;
- En revanche, il sera nécessaire de modifier le fichier `mkdocs.yml` en s'aidant des explications laissées en commentaires ou encore de celles ce [tutoriel de configuration d'un site web avec MkDocs](https://ericecmorlaix.github.io/adn-Tutoriel_site_web/Yaml/#le-fichier-mkdocsyml)


## Développer votre site

**Analyser** l'architecture des fichiers dans chacune des branches `main` et `gh-pages`...

Le texte en MarkDown de la page `index.md` du dossier `/docs` devient la page  d'accueil en HTML de votre site : `index.html`.

**Modifier** le fichier `index.md` à l'aide du langage [MarkDown de Mkdocks avec Material](../MarkDown-Mkdocs_Material/) pour faire évoluer votre page d'accueil...

Les dossiers présents dans `/docs` apparaissent comme sections principales de la barre de navigation. De même pour le titre de niveau 1 `# Accueil` écrit au début du fichier `index.md`.

Chaque note, `fichier.md` écrit en MarkDown, devient une nouvelle page du site dans leur section respective. Les noms de ces fichiers sont visibles dans la barre d'URL. Les titres et sous-titres de la table des matières apparaissent dans des sous-sections d'un menu secondaire.

> En l'absence de titre de niveau 1 au début d'une note, c'est le nom du fichier qui apparaitra en tête de la sous-section.

Il est donc préférable d'attribuer aux dossiers et fichiers des noms significatifs, sans caractère accentué ni espace et, de même que pour les titres et sous-titres, le mieux est de les choisir courts. 

> Ce nommage automatique peut-être modifié en définissant manuellement la rubrique `nav` dans le fichier `mkdocs.yml`, ce qui devient cependant vite fastidieux...

!!! note

    Toutes ces fichiers en MarkDown, futures page de votre site, sont éditables soit directement dans GitHub ou dans VS Code ou dans Obsidian...






