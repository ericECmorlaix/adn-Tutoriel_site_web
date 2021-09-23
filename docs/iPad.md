Ceci est un tutoriel pour déployer un site web avec le framework MkDocs et le thème Material sur votre iPad et GitHub.

## Prérequis :

Pour commencer,  il va vous falloir installer un OS Linux sur votre iPad et tous les paquets logiciels utiles au fonctionnement de **MkDocs**, pour ce faire suivez les instructions de la page [iSH Shell](./iSH_Shell) ;




## Votre premier site :

Puisque vous êtes maintenant en mesure de faire fonctionner MkDocs sur votre machine, il est temps de générer votre premier site afin de comprendre comment cela fonctionne...

### Générer les fichiers :
Dans un terminal d'[iSH Shell](iSH_Shell), saisir la commande :
```bash
mkdocs new monPremierSite
```
??? done "Vérification"
    Vous devez obtenir un message équivalent à :

    ```
    INFO    -  Creating project directory: monPremierSite
    INFO    -  Writing config file: monPremierSite/mkdocs.ym
    INFO    -  Writing initial docs: monPremierSite/docs/index.md
    ```

??? info "Observation"
    Utiliser les commandes `ls` et `cd` afin d'observer l'architecture suivante des fichiers dans le dossier :

    ```console
    .
    ├─ docs/
    │  └─ index.md
    └─ mkdocs.yml
    ```
### Construction du site :
Toujours dans un terminal d'[iSH Shell](iSH_Shell), ==depuis le dossier de votre site==, saisir la commande :
```bash
mkdocs build
```
??? done "Vérification"
    Vous devez obtenir un message équivalent à :

    ```
    INFO    -  Cleaning site directory
    INFO    -  Building documentation to directory: /root/monPremierSite/site
    INFO    -  Documentation built in 7.60 seconds
    ```

??? info "Observation"
    Installer puis utiliser la commande `tree` afin d'observer la nouvelle architecture des fichiers dans le dossier :

    ```
    └── monPremierSite
    ├── docs
    │   └── index.md
    ├── mkdocs.yml
    └── site
        ├── 404.html
        ├── css
        │   ├── base.css
        │   ├── bootstrap.min.css
        │   └── font-awesome.min.css
        ├── fonts
        │   ├── fontawesome-webfont.eot
        │   ├── fontawesome-webfont.svg
        │   ├── fontawesome-webfont.ttf
        │   ├── fontawesome-webfont.woff
        │   ├── fontawesome-webfont.woff2
        │   ├── glyphicons-halflings-regular.eot
        │   ├── glyphicons-halflings-regular.svg
        │   ├── glyphicons-halflings-regular.ttf
        │   ├── glyphicons-halflings-regular.woff
        │   └── glyphicons-halflings-regular.woff2
        ├── img
        │   ├── favicon.ico
        │   └── grid.png
        ├── index.html
        ├── js
        │   ├── base.js
        │   ├── bootstrap.min.js
        │   └── jquery-1.10.2.min.js
        ├── search
        │   ├── lunr.js
        │   ├── main.js
        │   ├── search_index.json
        │   └── worker.js
        ├── sitemap.xml
        └── sitemap.xml.gz
    ```

### Publication locale :

Maintenant que les fichiers de votre site web sont hébergés sur votre tablette, on peut très simplement publier ses pages localement et les visualiser depuis n'importe quelle autre machine connectée sur le même réseau que votre iPad.

Sur votre iPad, encore dans un terminal d'[iSH Shell](iSH_Shell), ==depuis le dossier `monPremierSite/site`== saisir la commande :

```bash
python3 -m http.server
```
Le mieux alors est d'afficher en partage d'écran la fenêtre du terminal et l'application `Safari`;

??? done "Vérification"
    Vous devez obtenir un message équivalent à :

    ```
    Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/)...
    ```

Puis, dans le navigateur de votre iPad saisir l'URL : `http://127.0.0.1:8000`.

Enfin depuis un navigateur d'une autre machine, saisir l'URL : `http://<IP_de_votre_iPad>:8000`

??? info "Observation"
    Observer les logs...

!!! warning "Interruption"
    Pour arrêter le serveur, appuyer sur les touches ++"^ Ctrl"+"C"++     


## Editer/Modifier le code :

Pour modifier les fichier de notre site, nous avons besoin d'un éditeur de code. Au moins deux solutions s'offrent à nous :

- l'application [Kodex](https://kodex.app/) disponible dans votre Self-Service ;

- ou installer dans un terminal d'[iSH Shell](iSH_Shell) le sympathique éditeur [micro-editor](https://micro-editor.github.io/) :wink: 

```bash
apk update
apk add bash
apk add curl
curl https://getmic.ro | bash
mv micro /usr/bin
```

Modifier ou remplacer le contenu du fichier `docs/index.md` et ajouter dans le fichier `mkdocs.yml` les lignes suivantes :

```yaml
theme:
    name: material
```
Pour vérifier l'effet de ces modifications à la volée, dans un terminal d'[iSH Shell](iSH_Shell), ==depuis le dossier de votre site==, saisir la commande :

```bash
mkdocs serve
``` 
Cela à pour effet de démarrer un serveur local pour visualiser le résultat dans un navigateur à l'adresse `http://127.0.0.1:8000`.


## Votre second site :

Pour cette seconde expérience, vous allez créer un portfolio de cours en adaptant le site visible à cette adresse : [https://ericecmorlaix.github.io/mkdocs_boilerplate/](https://ericecmorlaix.github.io/mkdocs_boilerplate/) ;

[Cliquer ici pour télécharger une archive de ce projet](https://github.com/ericECmorlaix/mkdocs_boilerplate/archive/refs/heads/main.zip){ .md-button }   

Extraire le dossier de cette archive, le copier et le renommer `monClasseurNSI` dans le dossier `/root` d'iSH ;

Analyser l'architecture des fichiers ;

Copier vos notebooks de Carnets Jupyter dans le dossier `docs` ;

Modifier le contenu du fichier `docs/index.md` et personaliser le fichier `mkdocs.yml` notamment en indiquant les références de vos notebooks dans le menu de navigation ;

Vérifier progressivement l'effet de vos modifications dans votre navigateur en démarrant un serveur local avec la commande `mkdocs serve` ;


## Publier votre portfolio sur GitHub :

Créer sur GitHub un dépot au nom de votre dossier `monClasseurNSI` sans créer de fichier `Readme.md` ;

En ligne de commande dans un terminal d'[iSH Shell](iSH_Shell) :

- installer et configurer git, si ce n'est pas déjà fait :

```bash
apk update # On met à jour le gestionnaire de paquets
apk add git # On installe le paquet git pour pouvoir piloter un dossier depuis GitHub
git config --global user.name "votrePseudoGitHub"
git config --global user.email "prenom.nom@eleves.ecmorlaix.fr" 
git config --list # vérifier la configuration globale
```

- piloter votre dépot GitHub :

```bash
cd monClasseurNSI # ce placer dans le dossier à piloter 
git init
git status
git add *
git commit -m "premier commit"
git remote add origin https://github.com/votrePseudoGitHub/monClasseurNSI.git
git branch -M main
git push -u origin main
```

Rendez-vous sur GitHub pour voir la mise à jour de votre dépot ;  
Après quelques minutes une seconde branche devrait être automatiquement créée...  
Allez alors dans le menu `Settings` puis `Pages` et sélectionner la branche `gh-pages` et le dossier `/(root)` pour construire votre site ;
Il sera alors visible à l'adresse `https://votrePseudoGitHub.github.io/monClasseurNSI.git`

