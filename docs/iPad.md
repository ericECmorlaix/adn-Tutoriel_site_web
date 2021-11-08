Vous disposez maintenant d'un site web généré avec le framework MkDocs et le thème Material qui est publié sur un de vos dépots GitHub.

Ceci est un tutoriel complémentaire pour développer et maintenir votre site depuis votre votre iPad grâce aux supers pouvoirs de la ligne de commande.

## Prérequis

Pour commencer,  il va vous falloir installer un OS Linux sur votre iPad et tous les paquets logiciels utiles au fonctionnement de **MkDocs**, pour ce faire suivez les instructions de la page [iSH Shell](../iSH_Shell){target="_blank"} ;


## Votre premier site

Puisque vous êtes maintenant en mesure de faire fonctionner MkDocs sur votre machine, il est temps de générer un site *"from scratch"*, de zéro, afin de comprendre comment cela fonctionne...

### Générer les fichiers
Dans un terminal d'[iSH Shell](../iSH_Shell){target="_blank"}, saisir la commande :
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
### Construction du site
Toujours dans un terminal d'[iSH Shell](../iSH_Shell){target="_blank"}, ==depuis le dossier de votre site==, saisir la commande :
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

### Publication locale

Maintenant que les fichiers de votre site web sont hébergés sur votre tablette, on peut très simplement publier ses pages localement et les visualiser depuis n'importe quelle autre machine connectée sur le même réseau que votre iPad.

Sur votre iPad, encore dans un terminal d'[iSH Shell](../iSH_Shell){target="_blank"}, ==depuis le dossier `monPremierSite/site`== saisir la commande :

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


### Editer/Modifier le code

Pour modifier les fichier de notre site, nous avons besoin d'un éditeur de code. Au moins deux solutions s'offrent à nous :

- l'application [Kodex](https://kodex.app/) disponible dans votre Self-Service ;

- ou installer dans un terminal d'[iSH Shell](../iSH_Shell){target="_blank"} le sympathique éditeur [micro-editor](https://micro-editor.github.io/) :wink: 

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
Pour vérifier l'effet de ces modifications à la volée, dans un terminal d'[iSH Shell](../iSH_Shell){target="_blank"}, ==depuis le dossier de votre site==, saisir la commande :

```bash
mkdocs serve
``` 
Cela à pour effet de démarrer un serveur local pour visualiser le résultat dans un navigateur à l'adresse `http://127.0.0.1:8000`.


## Maintenir sur l'iPad une copie de travail de votre site déployé sur GitHub :

En ligne de commande dans un terminal d'[iSH Shell](../iSH_Shell){target="_blank"} :

> Pour la gestion en ligne de commande, depuis le 13 août 2021, l'identification par simple mot de passe n'est plus supportée, il vous faudra définir une [clef personnelle d'identification](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).

### Installer git

```bash
apk update # On met à jour le gestionnaire de paquets
apk add git # On installe le paquet git pour pouvoir piloter un dossier depuis GitHub
```

### Cloner votre dépot GitHub

Sans préciser de nom de dossier ni d'identification :
```bash
git clone https://github.com/votrePseudoGitHub/monPremierSite.git
```

Avec nom de dossier et identification :
```bash
git clone https://github.com/votrePseudoGitHub/monPremierSite.git nom_du_dossier_clone
Username: your_username
Password: your_token
```

> Si on ne précise pas le nom du dossier à la fin de l'instruction, alors c'est le nom du dépôt GitHub cloné qui est attribué par défaut au dossier auquel il sera lié.

### Changer de répertoire de travail

```bash
cd monPremierSite # ce placer dans le dossier cloné
```

### Configurer le dossier

```bash
git config --global user.name "votrePseudoGitHub" # pour limiter la configuration à ce dossier uniquement, enlever le --global
git config --global user.email "prenom.nom@eleves.ecmorlaix.fr" # pour limiter la configuration à ce dossier uniquement, enlever le --global
git config --list # vérifier la configuration du dossier
```

### Développer en local à partir de la copie de travail

- Modifier le contenu du fichier `docs/index.md` et créer de nouveaux fichiers `docs/ma_nouvelle_page.md` ;

- Copier vos notebooks Jupyter `.ipynb` de Carnets et vos scripts Python `.py` dans le dossier `docs` ;

- Personaliser le fichier `mkdocs.yml` notamment en indiquant les références de vos nouveaux fichiers `.md` et vos notebooks `.ipynb` dans la configuration du menu de navigation ;

- Vérifier progressivement l'effet de vos modifications dans votre navigateur en démarrant un serveur local avec la commande `mkdocs serve` ;


### Récupérer les données actualisées du dépôt GitHub vers votre dossier clone = "Tirer"

```bash
git pull
```

### Vérifier l'état de votre copie de travail

```bash
git status
```

### Visualiser tous les changements réalisés à ce stade

```bash
git diff
```
> Les suppresions apparaissent en rouge précédées d'un signe **`-`**, et les ajouts apparaissent en vert prédédés d'un signe **`+`**.

> Utiliser avec la commande `git diff nomDuFichier` pour ne voir que les modifications effectuées sur un fichier 

### Ajouter les changements à mettre à jour à ce stade

```bash
git add nom_du_fichier
```
> La commande `git add *` permet d'ajouter tous les fichiers modifiés en une fois.
> 
> La commande `git add dossier/`permet d'ajouter un dossier et tout sont contenu.
>
> La commande `git reset HEAD -- nomDuFichier` permet d'enlever un fichier ajouté par erreur.
>
> La commande `git checkout nomDuFichier` permet d'annuler les modifications faites sur un fichier depuis l'état précédent.


### Valider et consigner vos modifications = "Commiter"
```bash
git commit -m "message du commit"
```
> La commande `git commit -a -m "mon message"` permet de directement valider et consigner les modifications qui concernent tous les fichiers déjà suivis sans avoir à passer préalablement par une commande `add`.
> 
> La commande `git commit` sans argument ouvre l'éditeur définit par défaut pour permettre d'écrire le message de `commit`...

### Mettre à jour votre dépôt GitHub avec votre copie de travail = "Pousser"

```bash
git push origin main
```
> Rendez-vous sur GitHub pour voir la mise à jour de votre dépot ;
> 
> Votre site distant devrait se mettre à jour avec vos modifications après quelques temps... 
