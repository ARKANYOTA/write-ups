> Nos experts ont réussi à mettre la main sur un algorithme d'authentification ultra secret utilisé par notre ennemi !
>
> Un unique mot de passe est accepté mais nous n'avons pas pu le recupérer. Pouvez-vous nous aider ?

1. On simplifie le code
2. On teste char by char en mettant des prints de partout, tel "reverse1_solution.py"
3. On trouve :


| `404CTF{P4sS1R0bUst3Qu3C4}` |
|-----------------------------|

> Nos experts ont eu vent d'un tout nouvel algorithme d'authentification qui donne du fil à retordre à nos agents ! Certains disent que réussir à le craquer pourrait inverser le cours des choses.
>
> Attention, nous ne sommes pas sûr que ce fichier soit exactement ce qu'il semble être.

4. On écrit reverse2.py
5. Dans le but que `dis.dis(a())` revoie environ reverse2.asm
6. on execute avec un bruteforce char by char


| `404CTF{L3s4pp4rencesS0ntTr0mp3uses}` |
|---------------------------------------|
