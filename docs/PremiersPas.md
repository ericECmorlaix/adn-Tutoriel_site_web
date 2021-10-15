# Premiers pas depuis un navigateur web :

## Créer un dépot GitHub :
Créer un compte sur GitHub (Sign up) depuis un navigateur à l'adresse [https://github.com/](https://github.com/){target="_blank"}, ou identifier vous (Sign in) si vous avez déjà un compte.

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub00.png" alt="inscription GitHub">
</figure>

A l'adresse [https://github.com/new](https://github.com/new){target="_blank"} créer un nouveau répertoire de dépot nommé, par exemple `mon_premier_site` :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub01bis.png" alt="nouveau repository GitHub">
</figure>

Cocher la case **"Initialize this repository with a README"** puis cliquer sur le bouton **"Create repository"**.

> Voilà, vous faites maintenant parti d'un autre [réseau social mondial celui des développeurs de code](https://medium.com/coding-days/focus-sur-github-le-r%C3%A9seau-social-des-d%C3%A9veloppeurs-165a2978ea9e){target="_blank"}...


## Modifier le fichier `README.md` :

Le fichier `README` à pour extension `.md` pour [**MarkDown**](https://fr.wikipedia.org/wiki/Markdown){target="_blank"}, c'est ce langage de description rudimentaire que nous utiliserons principalement pour rédiger nos futures pages web.

> Il existe plusieurs versions de ce langage qui, à partir d'une syntaxe de base commune, possèdent d'autres éléments additionnels spécifiques...

**Cliquer** sur le crayon pour ouvrir le fichier `README.md`dans l'éditeur en ligne :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub02bis.png" alt="editer README">
</figure>

**Modifier** son contenu en utilisant la syntaxe [MarkDown à la sauce GitHub](https://guides.github.com/features/mastering-markdown/){target="_blank"} :


<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub03bis.png" alt="modifier README">
</figure>

> l'onglet `Preview` permet de visualiser le résultat avant sa publication...

**Publier** la nouvelle version du fichier `README.md` en décrivant vos modifications dans un message et puis en cliquant sur le bouton `Commit changes` :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub04bis.png" alt="publier README">
</figure>

> **Waouh !** vous venez de faire votre premier [**Commit**](https://fr.wikipedia.org/wiki/Commit){target="_blank"} **!**

## Récupérer un modèle de site :

Vous allez recopier dans votre dépot GitHub les fichiers nécessaires pour produire un site tel que celui visible à cette adresse : [https://ericecmorlaix.github.io/base_mkdocs_material/](https://ericecmorlaix.github.io/base_mkdocs_material/){target="_blank"} ;

[Cliquer ici pour télécharger une archive de ce projet](https://github.com/ericECmorlaix/base_mkdocs_material/archive/refs/heads/main.zip){ .md-button }   

**Extraire** le dossier de cette archive en local sur PC ou iPad ;

**Cliquer** sur le bouton `Add file` depuis l'interface de votre dépot GitHub et choisir `Upload files` :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub06bis.png" alt="Glisser/Déposer">
</figure>

**Glisser/Déposer** ou **Sélectionner** les fichiers de l'archive à copier vers le dépot GitHub :

- ne pas prendre le `README.md`;

- le fichier `ci.yml` doit être placé dans une arborescence de répertoires nommés `.github/workflows/ci.yml` ;

> Pour créer une telle arborescence de dossier dans GitHub, il faut éditer le ficher `ci.yml`, comme fait précédemment pour le fichier `README.md`, afin de le renommer en ajoutant devant son nom le chemin des dossiers `.github/workflows/` ainsi que le montre la vidéo suivante :

<figure>
    <video width=80% controls autoplay>
        <source src="../video/GitHub-Editer_une_arborescence_de_dossiers.mov" type="video/mp4">  
        <source src="../video/GitHub-Editer_une_arborescence_de_dossiers.mp4" type="video/mp4">  
        Your browser does not support the video tag.
    </video>
    
    <figcaption>
        Comment éditer une arborescence de dossiers sur GitHub ? <br>
        <a href="https://www.youtube-nocookie.com/embed/0uEdPOhpNLE" target="blank">
            Voir la vidéo sur Youtube
        </a>
    </figcaption>
</figure>


<!-- 
<figure>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0uEdPOhpNLE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>
 -->



**Committer** !

> Au bout d'un moment, si tout se passe bien, le "bot" de GitHub devrait générer à partir de votre branche `main`, une seconde branche nommée `gh-pages` :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub07bis.png" alt="branche">
</figure>

## Déployer votre site :

**Cliquer** sur les onglets `Settings` (1) puis `Pages` (2), **sélectionner** la branche `gh-pages` (3) enfin **cliquer** sur le bouton `Save` (4) :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub08bis.png" alt="Déploiement">
</figure>

> Au bout d'un moment, si tout se passe bien, votre site devrait être visible sur le web...

## Personnaliser votre site :

**Analyser** l'architecture des fichiers...

**Modifier** le fichier `index.md` pour faire évoluer votre page d'accueil...

**Modifier** le fichier `mkdocs.yml` pour personnaliser votre site...


