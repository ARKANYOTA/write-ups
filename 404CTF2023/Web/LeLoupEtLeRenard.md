# Le Loup et le renard


## Description

```
Dans un coin du café, un homme est assis. Une tasse de café ainsi qu'un manuscrit sont posés devant lui. Il observe la salle : les allées-venues des clients, les conversations. Il semble à l'affût de la moindre action, du moindre écart de la part de son sujet d'observation.
 
Alors que son regard parcourt la salle, il s'étonne de voir que vous l'observiez déjà. D'un geste accompagné d'un sourire il vous invite à le rejoindre.
 
« Bienvenue ! Prenez place. Il est rare de voir quelqu'un d'attentif à autre chose que sa propre personne ici. C'est dommage, c'est justement ce qu'il y a de plus intéréssant dans ce genre de rassemblement : les autres. Je me présente : Jean de La Fontaine. Votre regard me plait, vous me semblez capable de m'aider sur mon prochain manuscrit. J'écris, voyez-vous ? Des fables, je m'inspire de ce que je vois et j'observe. Pouvez-vous m'aider à écrire la suite de celle-ci ? »
 
 
Ouvrez l'œil et trouvez la fin de cette fable.
Artamis#7513 et V0odOo#3248
```


Partie 1:

```js
<script>
  // Système d'authentification
  function auth() {
    if (
      document.getElementById("username").value === "admin" &&
      document.getElementById("password").value === "h5cf8gf2s5q7d"
    ) {
      window.location.href = "/fable/partie-2-cookie";
    }
  }
</script>
```
dans inspecter l'elemeent

Partie 2:
On vas dans cookie: on passe isAdmin de false a true

Partie 3:
On vas dans Timeline:
--> Partie4...-->Script evalued

On tombe sur:
```js
<div>Flag : 404CTF{N0_frOn1_3nD_auTh3nt1ficAti0n}</div>
<script>
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  if (urlParams.has("username") && urlParams.has("password")) {
    const username = urlParams.get("username");
    const password = urlParams.get("password");
    if (!(username === "admin" && password === "Fbqh96BthQ")) {
      document.location = "/fable/partie-3-redirect";
    }
  } else {
    document.location = "/fable/partie-3-redirect";
  }
</script>
```






404CTF{N0_frOn1_3nD_auTh3nt1ficAti0n}
