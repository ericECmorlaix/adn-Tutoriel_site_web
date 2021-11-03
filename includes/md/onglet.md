La syntaxe pour créer des onglets coulissants commence par trois signes d'égalité `:::md ===` suivi d'un espace et d'un titre écrit entre guillemets.

Puis, après un retour à la ligne et une indentation de 4 espaces, on peut écrire en MarkDown le code du contenu de cet onglet.

On quitte l'onglet en revenant à l'indentation de base. On peut alors en commencer un autre et ainsi de suite autant de fois que nécessaire.

On peut aussi imbriquer des onglets les uns dans les autres...


??? example "Exemple : ..."
    === "Rendu :"
        --8<-- "includes/md/ongletIn.md"
    === "Markdown :"
        ```md
        --8<-- "includes/md/ongletIn.md"
        ```
    ??? "Code MarkDown de cet exemple : ..."
        ````md
        === "Rendu :"
            --8<-- "includes/md/ongletIn.md"
        === "Markdown :"
            ```md
            --8<-- "includes/md/ongletIn.md"
            ```
        ````

??? cite "Une explication en vidéo par Fred LELEU :"
    <figure>    
        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/aPnQAzTAqNk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        <br>
        <figcaption markdown> [Les vidéos de Fred LELEU]{ target="_blank"}</figcaption>
    </figure>