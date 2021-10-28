Pour créer un bloc de citation, il suffit d'ajouter un `>` devant un paragraphe.

Les blocs de citation peuvent s'imbriqués tels que par exemple :

=== "MarkDown"
    ```md
    > Cette première ligne est incluse dans un bloc de citation.
    >
    > Cette seconde ligne l'est également.
    >> Celle ci se situe dans un bloc de citation imbriqué...
    ```
=== "Rendu"
    > Cette première ligne est incluse dans un bloc de citation.
    >
    > Cette seconde ligne l'est également.
    >> Celle ci se situe dans un bloc de citation imbriqué...

On peut utiliser les blocs de citation pour souligner un point, comme par exemple :
=== "Rendu"
    > :warning: &nbsp; **ATTENTION !**
    >
    > **Toto** est dans la place...
    >
    > *Ceci est une mise en garde, 
    vous voilà prévenu !!*
=== "MarkDown"
    ```md
    > :warning: &nbsp; **ATTENTION !**
    >
    > **Toto** est dans la place...
    >
    > *Ceci est une mise en garde, 
    vous voilà prévenu !!*
    ```
Mais pour cela, MkDocs-Material offre bien mieux...