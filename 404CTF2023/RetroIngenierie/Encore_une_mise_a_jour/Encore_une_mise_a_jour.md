# Encore une mise à jour

## Description

```
« RAAAAAAH !! »
 
Un cri sourd se fait entendre près du comptoir. Vous vous approchez, curieux. Vous remarquez le propriétaire des lieux fou de rage.
 
« Encore cette satanée Terreur des Quincailliers, il a volé tout mon café ! Je vais devoir appeler l'inspecteur Blognard. Mais comment diable a-t-il fait ? 
Vous ! Là ! Vous êtes la personne qui avez aidé les Hackademitiens toute la journée non ? »
 
Il vous pointe du doigt.
 
« Et bien ça tombe parfaitement, j'ai un mystère sur les bras, depuis que j'ai mis à jour mon coffre fort, tout mon café disparait régulièrement ! Je suis convaincu qu'il s'agit d'un des nombreux méfaits de cette fameuse Terreur des Quincailliers, mais l'inspecteur refuse de me croire ! Vous voulez bien me prouver que c'est possible de trouver le mot de passe ? D'ailleurs le vendeur m'avait juré qu'il était inviolable ! Si vous arrivez à prouver le contraire, je vais enfin pouvoir porter plainte !»
 
 
Pour ce challenge il suffit de trouver le mot de passe qui valide le programme. Attention cepenndant, il ne fonctionne que avec Python 3.11.
 
Format : 404CTF{mot de passe}
Redhpm#8108

```


On comprend que cody vaux 518 arpres un print a la fin du fichier de `h.Bytecode(check, **dico).dis().count('I')`

On reorganise de maniere a avoir tout en bien ordonée: voir encore-une-mise-a-jour.py

puis brutforce de 3 char en 3 char

```python
In [16]: o=518

In [17]: def g(a,b,c,d):
    ...:     for c0 in range(256):
    ...:         for c1 in range(256):
    ...:             for c2 in range(256):
    ...:                 if (c0+c1+o*c2==a or c0+c1+o*c2==b) and (c0+o*c1+c2==c or c0+o*c1+c2==d):
    ...: 
    ...:                     print(chr(c0),chr(c1),chr(c2), sep="")


In [18]: def h():
    ...:     g(35329,87961,42776,17234)
    ...:     g(40542,100914,19862,49274)
    ...:     g(27099,67347,61221,152553)
    ...:     g(49360,122890,18857,46721)
    ...:     g(147438,59202,25080,62232)
    ...:     g(58164,144852,27661,68683)
    ...:     g(135810,54540,128064,51438)
    ...:     g(54563,135833,98394,39570)
    ...:     g(51973,129373,66114,26640)
    ...:     g(144847,58159,62223,25071)
    ...:     g(35402,88034,143547,57633)
    ...:     g(17228,42770,43078,107320)
    ...:     g(64773,26073,63482,25556)
    ...:     g(115125,46239,27627,68649)
    ...:     g(35842,89248,64719,26019)
    ...:     g(72505,29161,98325,39501)
    ...: 

In [19]: h()
H!D
d&N
-v4
r$_
f0r
_5p
3ci
aLi
z3d
_0p
CoD
3S!
|12
T5Y
22E
ML8
```



404CTF{H!Dd&N-v4r$_f0r_5p3ciaLiz3d_0pCoD3S!|12T5Y22EML8}

