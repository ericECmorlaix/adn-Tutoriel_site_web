
Vous disposez maintenant d'un site web généré avec le framework MkDocs et le thème Material qui est publié sur un de vos dépots GitHub.

Ceci est un tutoriel complémentaire pour développer et maintenir votre site depuis votre PC Windows 10 avec l'éditeur Visual Studio Code.



## Préparation :

Il est nécessaire d'installer **Python**, un éditeur de code et tous les modules utiles au fonctionnement de **Git** et **MkDocs** :

- Télécharger et installer (cocher la case ajouter au PATH) la dernière version de Python disponible à l'adresse : [www.python.org](https://www.python.org/downloads/){target="_blank"} ;

- Télécharger et installer la dernière version de [Git for Windows](https://gitforwindows.org/){target="_blank"} ;

- Télécharger et installer la dernière version de [Visual Studio Code](https://code.visualstudio.com/download){target="_blank"} ;

Dans Visual Studio Code (VSC), ouvrir un nouveau Terminal (menu `Terminal > New Terminal`) pour saisir :
```bash
pip install mkdocs-material
```
```bash
pip install notebook
```
```bash
pip install mkdocs-jupyter
```

## La copie de travail = le clone local du dépôt distant :

- Dans Visual Studio Code (VSC), cliquer sur le bouton "Contrôle de code source" (1) (`Source Control` ++"Ctrl"+"Maj"+"G"++) ;

![VisualStudioCode.png](images/VisualStudioCodeGit00.png)

- Cliquer sur le bouton "Cloner le dépôt" (2), saisir l'URL du dépôt (3) puis valider (4) ;

- Choisir alors un dossier parent pour recevoir un clone local de votre dépôt distant ;

- Cliquer sur le bouton "Explorateur" (++"Ctrl"+"Maj"+"E"++) de VSC, puis cliquer sur un fichier pour l'ouvrir dans l'éditeur afin d'y apporter vos modifications... ;

## Développement du site en local :

- Ouvrir un nouveau Terminal pour saisir : `mkdocs serve` ;

- Votre site est visible dans un navigateur à l'URL : `http://127.0.0.1:8000`

- Editer et modifier les fichiers de votre site dans VSC ;

> Après chaque sauvegarde dans VSC avec la combinaison de touche ++"Ctrl"+"S"++ , l'affichage de votre site se met à jour dans le navigateur...

- Utiliser la combinaison de touches  ++"Ctrl"+"C"++ dans le terminal pour arrêter le serveur local...

??? tip "Afficher le rendu sur iPad tout en développant votre site local sur PC :"
    1. Connecter l'iPad et le PC sur un même réseau local ;
    2. Dans un terminal de VSC saisir `ipconfig` pour obtenir l'adresse IPv4 de votre PC ;
    3. Ouvrir un nouveau Terminal pour saisir : `mkdocs serve --dev-addr=0.0.0.0:8000` ;
    4. Dans un navigateur de l'iPad saisir l'adresse : `<IP_de_votre_PC>:8000` ;


## Mettre à jour votre site distant :

- Cliquer sur le bouton "Contrôle de code source" (`Source Control` ++"Ctrl"+"Maj"+"G"++) ;

??? caution "La première fois, il faut configurer git en ligne de commande dans un terminal :"
    
    > pour limiter la configuration à ce dossier uniquement, enlever le `--global`
    
    ```bash
    git config --global user.name "votrePseudoGitHub"
    ```
    
    ```bash
    git config --global user.email "prenom.nom@eleves.ecmorlaix.fr"
    ```

- Dans "Changements" (`Changes`) cliquer sur le `+` pour ajouter les fichiers modifiés à indexer dans cette phase (stage) de développement ;

- Ajouter un message sous "CONTROLE DE CODE SOURCE" (`SOURCE CONTROL`) pour définir cette phase de développement puis cliquer sur `✓` pour valider ce commit ;

- Enfin, cliquer sur les `...` et choisir `Push` ;

!!! caution "La première fois, il faut vous authentifier sur GitHub, choisir de le faire par une connexion via votre navigateur..."
    

> Votre site distant devrait se mettre à jour avec vos modifications après quelques temps...

!!! danger "Par la suite, commencer toujours par cliquer sur les `...` et choisir `Pull` avant de faire de nouveau changements..."

****

## ==Routine pour maintenir un site Git sur PC avec VSC== :

??? summary "1 - Ouvrir votre dossier local, le "clone" :"
    Démarrer Visual Studio Code, dans le menu `Fichier` choisir `Ouvrir le dossier...`  
    ou avec la comninaison de touches ++"Ctrl"+"K"+"O"++ ;

??? summary "2 - Tirer les modifications du dépôt distant :"
    Cliquer sur le bouton "Contrôle de code source" (`Source Control` ++"Ctrl"+"Maj"+"G"++), 
    puis cliquer sur les `...` en face de `CONTRÔLE DE CODE SOURCE` et choisir `Pull` ;

??? summary "3 - Modifier vos fichiers en local :"
    Depuis l'Explorateur (`Explorer` ++"Ctrl"+"Maj"+"E"++) de VSC ,
     cliquer sur un fichier pour l'ouvrir dans l'éditeur afin de le modifier ;

??? summary "4 - Indexer vos changements :"
    Depuis le "Contrôle de code source" (`Source Control` ++"Ctrl"+"Maj"+"G"++),
     dans "Changements" (`Changes`) cliquer sur le `+` pour ajouter les fichiers modifiés
      à mettre en attente (indexer) dans cette phase (stage) de développement ;

??? summary "5 - Committer, valider vos modifications :"
    Ajouter un message sous "CONTRÔLE DE CODE SOURCE" (`SOURCE CONTROL`)
     pour définir ces modifications à ce stade de votre développement,
      puis cliquer sur `✓` pour valider ce commit ;

??? summary "6 - Pousser les modifications vers votre dépôt distant :"
    Cliquer sur les `...` en face de `CONTRÔLE DE CODE SOURCE`
    et choisir `Push` ;

