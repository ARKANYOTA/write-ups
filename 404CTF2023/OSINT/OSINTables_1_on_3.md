# Les OSINTables [1/3]

## Description
```
En pleine discussion au Procope, Cosette vous raconte autour d'une part de fraisier la première fois qu'elle a essayé d'envoyer une lettre à son bienfaiteur : Jean Valjean.
 
Débutante dans la démarche postale, elle s'est trompée sur les informations nécessaires, elle en a même oublié l'adresse du destinataire, n'écrivant que la sienne. Elle vous montre la photo ci-jointe et vous met au défi de trouver d'où elle l'a écrite.
 
 
Trouvez l'adresse d'envoi de la lettre (celle de Cosette).
 
Format : 404CTF{numero_adresse_rue_ville}
exemple : 404CTF{36_quai_des_orfevres_paris}
 
Contact en cas de problème : Racoon#8487
```


On reconais le nombre 83 en rommain: LXXXIII =>

83_rue_victor_hugo


On va sur google map on tape Rue victor hugo:
On a: Velaux, Venissieux Vergeze

On teste les input on a bon avec le 3 eme

404CTF{83_rue_victor_hugo_vergeze}
