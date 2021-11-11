


Pour qu'un lien hypertexte pointe vers un endroit précis de la page courante, ou d'une autre page afin de positionner correctement le navigateur, il est nécessaire de définir une ancre :

??? tip "Ancre sur les titres : ..."
    [A partir des titres](#toc), MkDocs crée automatiquement des ancres vers lesquelles pointent les liens de la table des matières.  
    Pour le nommage de ces ancres, par défaut, les masjuscules sont transformées en minuscules, les espaces sont remplacés par des `-` et les caractères accentués deviennent des caractères de la table ASCII.
    !!! example ""
        === "MarkDown"
            ```md
            [Lien vers le titre "Caratères spéciaux"](#caracteres-speciaux)
            ```
        === "Rendu"
            [Lien vers le titre "Caratères spéciaux"](#caracteres-speciaux)

??? tip "Ancre sur les notes de bas page : ..."
    [Une note de bas de page](#note-de-bas-de-page) qui aurait `bar` pour référence d'identification, génère deux ancres :

    - l'une pour aller au contenu de la note de bas de page, `#fn:bar` ;
    - et l'autre pour revenir dans le texte à une référence liée à cette note, `#reffn:bar`.
 
    !!! example ""
        === "MarkDown"
            ```md
            [Lien vers la note de bas de page "critic"](#fn:critic)
            ```
        === "Rendu"
            [Lien vers la note de bas de page "critic"](#fn:critic)
        === "MarkDown"
            ```md
            [Lien de retour vers une référence à la note de bas de page "critic"](#fnref:critic)
            ```
        === "Rendu"
            [Lien de retour vers une référence à la note de bas de page "critic"](#fnref:critic)
        === "MarkDown"
            ```md
            [Lien de retour vers une autre référence à la note de bas de page "critic"](#fnref2:critic)
            ```
        === "Rendu"
            [Lien de retour vers une autre référence à la note de bas de page "critic"](#fnref2:critic)

??? tip "Ancre à un endroit quelconque : ..."
    Pour créer une ancre à un endroit quelconque au beau milieu du MarkDown on peut y placer une balise HTML invisible en lui attribuant un identifiant : `:::html <a id="foo"></a>`.  
    Et puis, pour pointer vers cet endroit, on lui associe un lien débutant par le caractère dièse `#`, suivi du nom de cet identifiant : `:::md [lien vers l'ancre identifiée "foo"](#foo)`
    !!! example ""
        === "MarkDown"
            ```md
            [Lien vers l'ancre "toto"](#toto)
            ```
        === "Rendu"
            [Lien vers l'ancre "toto"](#toto)
