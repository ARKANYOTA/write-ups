# Le Jour de l'espace

## Description

```
Rimbaud vous propose une séance initiatique au Oui-ja dans l'aile mystique du café littéraire (oui, oui, ça existe), vous avez une vision ésotérique :
Alors que vous voyez le texte suivant ueomaspblbppadgidtfn, Rimbaud vous décrit voir un étrange cadre de 50cm de côté, avec des petits carrés de 10cm de côtés, numérotés de 0 à 24 et jetés pêle-mêle sur le sol. Rimbaud n'y comprends rien, mais vous restez obsédé par cette idée, et décidez de résoudre l'énigme.
 
 
Toutes les informations nécéssaires à la résolution de ce challenge sont présentes dans l'énoncé ci-dessus.
 
Format : 404CTF{cequevousalleztrouver}
NainCapable#2614
 
nc challenges.404ctf.fr 31451
```


On tatone on obtient
```
a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z  
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

a=1,b=0,c=17,d=9,e=0
  21,4,11,12,0
  0,18,18,0,18
  18,8,13,4,0

Last char -> 
	a->a
	b->i
	c->q
	d->y
	e->h
	f->x



Last char->
	first char -> +8
	secon char -> +3
	third      -> +12
	forut      -> +17
	fivth      -> +24

(-2) char ->
	first char -> -5
	           -> +1
		   -> +10
		   -> 
```

On teste baaaa, puis abaaa, puis ... puis aaaab

On a 
```
In [3]: def diff(w):
   ...:     return [ord(x)-97 for x in w]
   ...:

In [4]: diff("jlfnt")
Out[4]: [9, 11, 5, 13, 19]

In [5]: diff("eagov")
Out[5]: [4, 0, 6, 14, 21]

In [6]: diff("schpw")
Out[6]: [18, 2, 7, 15, 22]

In [7]: diff("ubkqx")
Out[7]: [20, 1, 10, 16, 23]

In [8]: diff("idmry")
Out[8]: [8, 3, 12, 17, 24]

Et pour la sortie finalle
In [9]: diff("ueomaspblbppadgidtfn")
Out[9]: [20, 4, 14, 12, 0,
	18, 15, 1, 11, 1, 
	15, 15, 0, 3, 6, 
	8, 3, 19, 5, 13]
```

On rentre ça dans décode: "https://www.dcode.fr/solveur-equation-modulaire#:~:text=Qu%27est%20ce%20qu%27une,usage%20de%20parler%20de%20congruence."

avec un modulo de 25 et en inconue "a b c d e"

On rentre:
```
9a  + 4b  + 18c + 20d + 8e = 20  mod 25
11a + 0b  + 2c  + 1d  + 3e = 4   mod 25
5a  + 6b  + 7c  + 10d + 12e = 14 mod 25
13a + 14b + 15c + 16d + 17e = 12 mod 25
19a + 21b + 22c + 23d + 24e = 0  mod 25
```
On obtient 4 passage:
```
a=1,b=0,c=17,d=9,e=0
  21,4,11,12,0
  0,18,18,0,18
  18,8,13,4,0

Que on traduit en lettre
```

On a donc:   
message en clair : barjavelmaassassinea  
message chiffre  : ueomaspblbppadgidtfn  
toutes mes felicitations !  

On enleve le a a la fin car il est supposée comme 0.

barjavelmaassassine

`404CTF{barjavelmaassassine}`




