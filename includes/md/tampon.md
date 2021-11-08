<!--
??? tip "Ajouter des métadonnées ou d'autres balises personnalisées : ..."

    Pour inclure des [balises customisées](https://squidfunk.github.io/mkdocs-material/reference/meta-tags/#customization) entre les balises `<head></head>` d'une ou de toutes les pages du site, il faut créer à la racine du projet dans un dossier nommé [`overrides`](https://squidfunk.github.io/mkdocs-material/customization/?h=overr#extending-the-theme) un fichier `main.html` et déclarer ce dossier en tant que `custom_dir:` dans le paramétrage de `theme:`.

    ??? example "Exemple pour ce site : ..."
        === "dans mkdocs.yml"
            ```yaml
            theme:
              name: material
              custom_dir: overrides
            ```
        === "dans overrides/main.html"
            ```html
            {% extends "base.html" %}
            
            {% block extrahead %}
                <base href="" target="_blank">
            {% endblock %}
          ```
-->