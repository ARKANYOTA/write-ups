# L'Être ou le néant

## Description

```
Alors que vous vous détendez au comptoir en compagnie d'autres clients, un individu suspect s'approche. Malheur, vous reconnaissez Jean-Paul SAT, qui semble avoir eu une idée aussi invraisemblable que sa personne. Vous discernez dans sa main gauche qu'il tend fièrement, un petit appareil fort intriguant. Vous n'avez même pas le temps de vous enquérir de la situation qu'il s'exclame d'une voix solennelle, mais pourtant enjouée :
« Être, Néant, qu'en sera-t-il ? Vous voulez savoir ? J'ai exactement ce qui vous faut ! Toi, au comptoir, que seras-tu donc ! »
Il pointe un client, qui se laisse entrainer par la lubie de cet olibrius de Jean-Paul SAT.
« Partage ton savoir et nous saurons tous ce que tu es vraiment ! »
Le pauvre désigné bafouille d'inaudible parole et la machine s'exclame :
« Néant tu es, Néant tu resteras »
La vision de cette perturbante scène force votre regard à fuir instinctivement. Votre voisin de comptoir vous aborde :
« C'est la première fois que tu viens ici ? Ne t'en fais pas, c'est courant de voir Jean Paul SAT avec d'étranges petits appareils. Personne n'a encore réussi à passer ses épreuves ! Mais toi je suis sûr que tu as les épaules pour ! J'ai piqué ça sur sa table tout à l'heure, ce plan devrait t'aider, bonne chance à toi »
Deux autres clients se sont vu affubler la mention de Néant ! Il ne vous reste plus beaucoup de temps, dépêchez-vous !
 
 
Format : 404CTF{mot de passe}
Astate#3107 et Redhpm#8108
```

On voit assez vite que go_in doit être egal a [Signal(bool(0)) for _ in range(8)]
Plus qu'a savoir ce qu'il faut dans Flag_in tq Flag_in = [modbv(19941), modbv(92426), modbv(29012), modbv(98722), modbv(3706), modbv(131071), modbv(131071), modbv(0)]  (Nombre random)





Pour tout les block on va sur vim et on apllique `:%s/F[0-9]* = \(.*\),\([a-t \[\]0-9]*\))/\2 = \1)/`  dans `replace.py`


On obtient un chiffre pour chaque Block
```
print("Block0 70245  10001 00100 1100101")
print("Block1 8241   00010 00000 0110001")
print("Block2 39835  01001 10111 0011011")
print("Block3 34817  01000 10000 0000001")
print("Block4 29679  00111 00111 1101111")
print("Block5 65535  01111 11111 1111111")
print("Block6 106674 11010 00001 0110010")
print("Block7 0      00000 00000 0000000")
#                    Al0r5 , 54t 1sf41t?

```


Et on lit le binaire des nombre en colones de haut en bas 

On obtient `Al0r5, 54t1sf41t?`

