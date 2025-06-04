## J'essaye de comprendre:

Je teste avec mon propre flag:
J'essaye Avec "HelloWorld", J'ai une erreur

Je vois que il accede un charactere à au carré de l'index que je met dans le charset, modulo n+1.

Apres quelques tests, je comprends que H n'est pas encodable, car il fait tomber à la posisiton n qui n'est pas dans charset (de taille n donc de derniere position n-1)

Je vois aussi d'apres la forme de l'output donnée que l'encodage ne depend pas de la position du charactere.
Ainsi, 4 sera toujours encodé par 8, etc...

Je fait dont la table inverse de l'encodage, en evitant les charactere qui ne sont pas encodables.

> Y'a moyen qu'on ait des doublons pour le meme charactere, donc j'y fait attention

Je me rend compte que juste H se copie vers lui même(vu qu'il n'est pas dans le flag encrpypté, pas de souci a se faire), et qu'il n'y a pas de doublon.


Et on trouve:
```
404CTF{C0nstEllAt!0n}
```