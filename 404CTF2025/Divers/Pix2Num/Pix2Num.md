## Partie compréhension

On sait que c'est du png, on à un xor de l'image et d'une clé aléatoire.
La clé est de 64 bits, on sait que le header d'un png fait 64 bits (d'apres le wiki: 89 50 4E 47 0D 0A 1A 0A)

On va donc essayer de trouver la clé en xorant le header du png avec le header de l'image.

Mais avant faut transformer le nombre en hexadécimal.

## Partie exploration

On Essaye d'ajouter des prints, genre à pixels et image pour voir leurs valeurs

Je me rends compte que la fonction encrpyt à aucune idée du fait que ça soit un png, donc le fait de faire un match header n'est pas possible.

A la place je vais supposer que le debut de l'image est soit tout noir soit tout blanc.
Je vais donc faire un xor avec 0x00 et 0xFF pour voir si ça fonctionne.

Je me rends compte que ça marche car j'ai 
b'~\xd8y7\xd8\xed\n\x11~\xd8y7\xd8\xed\n\x11'
en boucle puis des caracteres aléatoires vers le milieu.

PLus que a xor toute l'image avec cette chaine de byte.

Je transorme en binaire, j'aurais donc une image avec majoritairement des 0, je vais essayer de resize jusqu'a avoir un texte lisible.

Je trouve un texte lisible:
Je teste le mdp:
404CTF{4n_Al1eN_hA9_b33n_7OUnD}
404CTF{4n_AlleN_hA9_b33n_7OUnD}
404CTF{4n_Al1eN_hA9_b33n_70UnD}
404CTF{4n_A11eN_hA9_b33n_70UnD}
404CTF{4n_Al1eN_hA9_b33n_70UnD}
404CTF{4n_A1leN_hA9_b33n_70UnD}
404CTF{4n_A11eN_hA9_b33n_70UnD} Il marche yhoopi