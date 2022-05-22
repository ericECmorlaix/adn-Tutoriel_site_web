## Kezako ?

[iSH Shell](https://ish.app/) est un projet d'application qui permet de faire fonctionner un terminal Linux localement sur votre tablette iPad (ou votre iPhone) :

![Ecran d'iSH](https://ish.app/assets/front-ipad.webp)

![IHM d'iSH](https://ish.app/assets/iphone-keyboard.webp)

- il y a un dépot GitHub : [https://github.com/ish-app/ish](https://github.com/ish-app/ish) ;

- on trouve de l'aide sur le wiki : [https://github.com/ish-app/ish/wiki](https://github.com/ish-app/ish/wiki)


## Installation

1. Depuis l'application `Self Service`, installer **iSH Shell** sur votre iPad ;

2. Démarrer **iSH** et saisir la commande `uname -a` ;
> On vérifie qu'on est dans un émulateur d'OS Linux contrairement à l'application [a-Shell mini](https://apps.apple.com/fr/app/a-shell-mini/id1543537943?l=en#?platform=ipad) qui dialogue avec [Darwin](https://fr.wikipedia.org/wiki/Darwin_(informatique)) l'OS de votre iPad...

3. Ouvrir l'application `Fichiers` et ajouter **iSH** dans les emplacements visibles à coté de "iCloud Drive" et "Sur mon iPad" ;
> Les autres applications comme `Carnets` ont accès aux fichiers de votre émulateur Linux...

4. **iSH** utilise [Alpine Package Manager](https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management) :
    - saisir `apk update` pour mettre à jour ;
    - puis `apk search python` pour rechercher un paquet ;
    - enfin `apk add python3`, pour installer un paquet...

5. Saisir `python3` puis essayer quelques instructions comme `import this` ou `from __future__ import braces` pour verifier qu'on est bien en présence d'un interpréteur Python, enfin saisir `exit()` pour revenir au prompt du terminal.

6. Saisir `apk add py3-pip` pour installer pip afin de gérer l'installation d'autres modules pour Python ;

7. Saisir `apk add py3-regex` puis `pip install mkdocs-material` afin d'installer [Material pour MkDocs](https://squidfunk.github.io/mkdocs-material/) ce qui est assez long...

8. Saisir `apk add py3-pyzmq` puis `pip install mkdocs-jupyter` afin d'installer un plugin pour intégrer des [Jupyter Notebook à MkDocs](https://github.com/danielfrg/mkdocs-jupyter) ce qui est encore assez long...









