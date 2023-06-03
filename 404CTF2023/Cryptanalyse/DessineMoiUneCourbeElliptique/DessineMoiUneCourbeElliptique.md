# Dessine-moi une courbe elliptique

## Description
```
Dessine-moi une courbe elliptique

825

Au cours d'une de vos explorations dans le café, vous surprenez la conversation suivante :
Oh ! Ce jour, je m'en souviens parfaitement, comme si c'était hier. À cette époque, je passais mes journées à mon bureau chez moi, avec comme seule occupation de dessiner les illustrations qui m'étaient commandées par les journaux du coin. Je ne m'en rendais pas compte à ce moment, mais cela faisait bien 6 ans que je vivais cette vie monacale sans réelle interaction humaine. Le temps passe vite quand on n'a rien à faire de ses journées. Mais ce jour-là, c'était différent. Je m'apprêtais à commencer ma journée de travail, un peu stressé parce que j'avais des illustrations que je devais absolument finir aujourd'hui. Alors que je venais de m'installer devant ma planche à dessin, quelle ne fut pas ma surprise d'entendre une voix venir de derrière-moi : 
« S'il-te plaît, dessine moi une courbe elliptique. » 
Je me suis retourné immédiatement. Un petit bonhomme se tenait derrière moi, dans mon appartement, habillé de façon tout à fait incongrue. Il portait une sorte de tenue de mousquetaire céleste ? Même aujourd'hui je ne sais toujours pas comment la décrire.
« Quoi ?
— S'il-te plaît, dessine moi une courbe elliptique. »
Devant cette situation ubuesque, mon cerveau a lâché, a abandonné. Je ne cherchais plus à comprendre et je me contentais de répondre:
« Je ne sais pas ce que c'est.
— Ce n'est pas grave, je suis sûr que tu pourras en dessiner une belle! Répondit l'enfant en rigolant. »
Machinalement, je pris mon crayon, et je dessinai à main levée une courbe, sans réfléchir. Après quelques instants, je me suis retourné, et j'ai montré le résultat à l'enfant, qui secoua immédiatement la tête.
« Non, regarde: cette courbe à un déterminant nul, je ne veux pas d'une courbe malade ! »
À ce moment, je ne cherchais plus à comprendre ce qu'il se passait. J'ai donc fait la seule chose que je pouvais faire, j'en ai redessiné une. Cette fois, l'enfant était très heureux.
« Elle est magnifique ! Je suis sûr qu'elle sera très heureuse toute seule. »
Et là, sous mes yeux ébahis, la courbe pris vie depuis mon dessin, et s'envola dans la pièce. Elle se mit à tourner partout, avant de disparaître. J'étais bouche bée, enfin encore plus qu'avant.
« Ah, elle avait envie de bouger visiblement !
— Où est-elle partie ?
— Je ne sais pas. Mais c'est toi qui l'a dessinée ! Tu ne devrais pas avoir de mal à la retrouver. En plus je crois qu'elle t'a laissé un petit souvenir, dit-il en pointant le sol, où une série de chiffres étaient effectivement dessinés sur le parquet.
— Merci encore ! Sur ce, je dois partir. Au revoir ! »
Avant que je puisse ouvrir la bouche, il disparût.
Je ne sais toujours pas ce qu'il s'est passé ce jour-là, mais je retrouverais cette courbe un jour !
 
 
Peut-être pourriez-vous l'aider ?
Alternatif#7526
```


On sait que l'equation de la courbe elyptique $y^2 = x^3 + ax + b$


On a comme valeur connue:
G_x = 93808707311515764328749048019429156823177018815962831703088729905542530725
G_y = 144188081159786866301184058966215079553216226588404139826447829786378964579
H_x = 139273587750511132949199077353388298279458715287916158719683257616077625421
H_y = 30737261732951428402751520492138972590770609126561688808936331585804316784
p = 231933770389389338159753408142515592951889415487365399671635245679612352781


On resoult l'equation: avec sympy

```
from sympy import symbols, Eq, solve

a, b = symbols('a b')
equation_1 = Eq(G_y**2, G_x**3 + a*G_x + b)
equation_2 = Eq(H_y**2, H_x**3 + a*H_x + b)
solutions = solve((equation_1, equation_2), (a, b))

print(solutions)
```

on a un unique couple: on le met dans sagemath
```
sage: a,b = -2084427415787573107307163445898635120031985043395279235018345820115926972549642455543309578884716641729449
....: 41708080271071369533168969487407690706382667101401618264550643942845259100061159336900412215419453352907290409467
....: 769/5051653382110596513383336592662126828475744052439258557399391967837232744,15383485425814774245193475118141355
....: 54822438053171392168273790509092982610499564334760114202774343883388903461800919224470765131276722775896112268346
....: 91805612610594224739841999363721868981291387816780346969646360084869117665652362958084089382174429739238254333456
....: 03225420982709209943966469500036829/5051653382110596513383336592662126828475744052439258557399391967837232744

# On verifie que ca soit la bonne courbe

sage: E = EllipticCurve(GF(p), [a,b])
sage:     G = E(G_x, G_y)
....:     H = E(H_x, H_y)
sage: if G in E and H in E:
....:     print("ok")
....: 
ok
sage: 4 * a**3 + 27 * b**2
# On a un truc non nul pour le determinant

# On affiche E:
sage: E
Elliptic Curve defined by y^2 = x^3 + 14902775479549176103916693271068277706052934716440896707334978512750519253*x + 220048944991955967308525489300590382240260882141745561912602020777012600739 over Finite Field of size 231933770389389338159753408142515592951889415487365399671635245679612352781

# On identifie le bon a et b

sage: a = 14902775479549176103916693271068277706052934716440896707334978512750519253
sage: b = 220048944991955967308525489300590382240260882141745561912602020777012600739
sage: E = EllipticCurve(GF(p), [a,b])
sage:     G = E(G_x, G_y)
....:     H = E(H_x, H_y)
# C'est toujours la bonne courbe

# On affiche stra+strb
sage: str(a)+str(b)
'14902775479549176103916693271068277706052934716440896707334978512750519253220048944991955967308525489300590382240260882141745561912602020777012600739'
```

Dans python maintenant:
```
>>> key = "14902775479549176103916693271068277706052934716440896707334978512750519253220048944991955967308525489300590382240260882141745561912602020777012600739"
>>> (hashlib.sha1(key.encode()).digest()[:16]).hex()                                                                   '2a21e2e5284d67652d0dc838c30daed9'
```

On va sur cyberchef:
`https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'Hex','string':'2a21e2e5284d67652d0dc838c30daed9'%7D,%7B'option':'Hex','string':'00b7822a196b00795078b69fcd91280d'%7D,'CBC/NoPadding','Hex','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=ODIzM2QwNGEyOWJlZmQyZWZiOTMyYjRkYmFjOGQ0MTg2OWUxM2VjYmE3ZTVmMTNkNDgxMjhkZGQ3NGVhMGM3MDg1YjRmZjQwMjMyNjg3MDMxM2UyZjFkZmJjOWRlM2Y5NjIyNWZmYmU1OGE4N2U2ODc2NjViN2Q0NWE0MWFjMjI`


On trouve:
`404CTF{70u735_l35_gr4nd35_p3r50nn3s_0nt_d_@b0rd_373_d35_3nf4n7s}`

