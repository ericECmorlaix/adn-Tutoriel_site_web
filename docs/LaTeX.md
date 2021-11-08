
# $\LaTeX$ pour les sciences
## Principe
De même que dans les cellules MarkDown d'un [notebook Jupyter](../LaTeX-Le_BN_pour_formuler),
 il est possible d'écrire des expressions scientifiques en $\LaTeX$ dans un `fichier.md` de MkDocs.

!!! example ""
    === "Rendu"
        On peut inclure un code $\LaTeX$ en ligne $y = x^2$,
        ou en bloc :
        
        $$y = x^2$$
    === "MarkDown"
        ```md
        On peut inclure un code $\LaTeX$ en ligne $y = x^2$,
        ou en bloc :
        
        $$y = x^2$$
        ```

??? cite "Une explication en vidéo par Fred LELEU :"
    <figure>    
        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/QR4-eLTslAE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        <br>
        <figcaption markdown> [Les vidéos de Fred LELEU]{ target="_blank"}</figcaption>        
    </figure>
***
## Installation
Il est nécessaire d'ajouter l'extension [pymdownx.arithmatex](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#arithmatex){target=_blank} ainsi que quelques lignes de Javascript et aussi une retouche de CSS (merci [GiYoM](https://mooc-forums.inria.fr/moocnsi/t/mkdocs-une-solution-ideale/1758/17){ target="_blank"}).

Il faut donc créer dans le dossier `docs` :

- un dossier nommé [`stylesheets`](https://squidfunk.github.io/mkdocs-material/customization/?h=css#additional-css){target=_blank} contenant un fichier `extra.css` ;
- un dossier nommé [`javascripts`](https://squidfunk.github.io/mkdocs-material/customization/?h=css#additional-css){target=_blank} contenant un fichier `config.js`.

Puis coller dans ces fichiers les codes suivants et les déclarer dans le fichier `mkdocs.yml` :

=== "dans mkdocs.yml"
    ```yaml
    markdown_extensions:
      - pymdownx.arithmatex:
          generic: true
          smart_dollar: false    

    extra_javascript:
      - javascripts/config.js
      - https://polyfill.io/v3/polyfill.min.js?features=es6
      - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
    
    extra_css:
      - stylesheets/extra.css
    ```
=== "dans javascripts/config.js"
    ```js
    window.MathJax = {
      tex: {
        inlineMath: [["\\(", "\\)"]],
        displayMath: [["\\[", "\\]"]],
        processEscapes: true,
        processEnvironments: true
      },
      options: {
        ignoreHtmlClass: ".*|",
        processHtmlClass: "arithmatex"
      }
    };

    document$.subscribe(() => {
      MathJax.typesetPromise()
    })
    ```
=== "dans stylesheets/extra.css"
    ```css
    .md-typeset div.arithmatex  {
        overflow: initial;
    }
    ```
***
## Applications
### Opérations Arithmétiques
=== "MarkDown"
    ```md
    * Addition :
        * $x + y$
    * Soustraction :
        * $x - y$
    * Multiplication :
        * $x \times y$ 
    * Division :
        * $x \div y$
        * $x \over y$
    * Puissance :
        * $x^2$
        * $y^{(x-1)}$
    ```
=== "Rendu"
    * Addition :
        * $x + y$
    * Soustraction :
        * $x - y$
    * Multiplication :
        * $x \times y$ 
    * Division :
        * $x \div y$
        * $x \over y$
    * Puissance :
        * $x^2$
        * $y^{(x-1)}$

### Relations
=== "MarkDown"
    ```md
    * $\pi \approx 3.14159$
    * $1 \neq 2$
    * $0 < 1$
    * $2 > 1$
    * $x \leq 2$
    * $x \geq 1$
    ```
=== "Rendu"
    * $\pi \approx 3.14159$
    * $1 \neq 2$
    * $0 < 1$
    * $2 > 1$
    * $x \leq 2$
    * $x \geq 1$

### Indice
=== "MarkDown"
    ```md
    $$U_n = 3 \times U_{n-1}+2$$
    ```
=== "Rendu"
    $$U_n = 3 \times U_{n-1}+2$$

### Fractions
=== "MarkDown"
    ```md
    * $\frac{1}{2x}$
    * ${3 \over 4}$
    * $^1/_2$
    ```
=== "Rendu"
    * $\frac{1}{2x}$
    * ${3 \over 4}$
    * $^1/_2$

### Racine
=== "MarkDown"
    ```md
    $$f(x) = \sqrt[3]{2x} + \sqrt{x-2}$$
    ```
=== "Rendu"
    $$f(x) = \sqrt[3]{2x} + \sqrt{x-2}$$

### Algèbre de Boole
=== "MarkDown"
    ```md
    $$a\oplus b=\bar{a}\cdot b+a\cdot\bar{b}$$
    ```
=== "Rendu"
    $$a\oplus b=\bar{a}\cdot b+a\cdot\bar{b}$$

### Moments et Forces
=== "MarkDown"
    ```md
    $\sum\overrightarrow{M_G(\overrightarrow{F_{ext \to S}})}$
    ```
=== "Rendu"
    $\sum\overrightarrow{M_G(\overrightarrow{F_{ext \to S}})}$


### Alphabet Grec
=== "MarkDown"
    ```md
    |         | Small Letter          | Capical Letter       | Alervative                  |
    |---------| --------------------- | -------------------- | --------------------------- |
    | alpha   | $\alpha$              | $A$                  |                             |
    | beta    | $\beta$               | $B$                  |                             |
    | gamma   | $\gamma$              | $\Gamma$             |                             |
    | delta   | $\delta$              | $\Delta$             |                             |
    | epsilon | $\epsilon$            | $E$                  | $\varepsilon$               |
    | zeta    | $\zeta$               | $Z$                  |                             |
    | eta     | $\eta$                | $H$                  |                             |
    | theta   | $\theta$              | $\Theta$             | $\vartheta$                 |
    | iota    | $\iota$               | $I$                  |                             |
    | kappa   | $\kappa$              | $K$                  | $\varkappa$                 |
    | lambda  | $\lambda$             | $\Lambda$            |                             |
    | mu      | $\mu$                 | $M$                  |                             |
    | nu      | $\nu$                 | $N$                  |                             |
    | xi      | $\xi$                 | $Xi$                 |                             |
    | omicron | $\omicron$            | $O$                  |                             |
    | pi      | $\pi$                 | $\Pi$                | $\varpi$                    |
    | rho     | $\rho$                | $P$                  | $\varrho$                   |
    | sigma   | $\sigma$              | $\Sigma$             | $\varsigma$                 |
    | tau     | $\tau$                | $T$                  |                             |
    | upsilon | $\upsilon$            | $\Upsilon$           |                             |
    | phi     | $\phi$                | $\Phi$               | $\varphi$                   |
    | chi     | $\chi$                | $X$                  |                             |
    | psi     | $\psi$                | $\Psi$               |                             |
    | omega   | $\omega$              | $\Omega$             |                             |
    ```
=== "Rendu"
    |         | Small Letter          | Capical Letter       | Alervative                  |
    |---------| --------------------- | -------------------- | --------------------------- |
    | alpha   | $\alpha$              | $A$                  |                             |
    | beta    | $\beta$               | $B$                  |                             |
    | gamma   | $\gamma$              | $\Gamma$             |                             |
    | delta   | $\delta$              | $\Delta$             |                             |
    | epsilon | $\epsilon$            | $E$                  | $\varepsilon$               |
    | zeta    | $\zeta$               | $Z$                  |                             |
    | eta     | $\eta$                | $H$                  |                             |
    | theta   | $\theta$              | $\Theta$             | $\vartheta$                 |
    | iota    | $\iota$               | $I$                  |                             |
    | kappa   | $\kappa$              | $K$                  | $\varkappa$                 |
    | lambda  | $\lambda$             | $\Lambda$            |                             |
    | mu      | $\mu$                 | $M$                  |                             |
    | nu      | $\nu$                 | $N$                  |                             |
    | xi      | $\xi$                 | $Xi$                 |                             |
    | omicron | $\omicron$            | $O$                  |                             |
    | pi      | $\pi$                 | $\Pi$                | $\varpi$                    |
    | rho     | $\rho$                | $P$                  | $\varrho$                   |
    | sigma   | $\sigma$              | $\Sigma$             | $\varsigma$                 |
    | tau     | $\tau$                | $T$                  |                             |
    | upsilon | $\upsilon$            | $\Upsilon$           |                             |
    | phi     | $\phi$                | $\Phi$               | $\varphi$                   |
    | chi     | $\chi$                | $X$                  |                             |
    | psi     | $\psi$                | $\Psi$               |                             |
    | omega   | $\omega$              | $\Omega$             |                             |

## Ressources

- La très précieuse et précise [Aide pour écrire des mathématiques simples](https://ens-fr.gitlab.io/mkdocs/maths/){target=_blank} par Franck CHAMBON

- [Equation Sheet](http://www.equationsheet.com/){target=_blank}

- [Editeur d'équation en ligne](http://www.codecogs.com/eqnedit.php?latex=){target=_blank}

- L'ultime ressource : [LaTeX Wiki](http://en.wikibooks.org/wiki/LaTeX/Mathematics){target=_blank}

- Pour s'initier au vrai $\LaTeX$ :[Apprentissage LaTeX en ligne avec ShareLaTeX](http://tsi.si.lycee.ecmorlaix.fr/APprentissageLaTeX/){target=_blank}


--8<-- "includes/md/abr_ref.md"