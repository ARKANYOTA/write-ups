> :warning: J'ai pas réussi ce challenge.

### J'essaye de comprendre

Je vois que chaque block de 16 caractere donne toujours le meme resultat, que quand je change une valeur, c'est une valeur autre position qui est changée:
Par exemple:
```
Donne moi un bloc en hexadécimal à chiffrer > (00)000000000000000000000000000000
Et voilà le chiffré > 33cf27508fc1aa9611(98)747d2baccfa2
Donne moi un bloc en hexadécimal à chiffrer > (01)000000000000000000000000000000  
Et voilà le chiffré > 33cf27508fc1aa9611(f4)747d2baccfa2
Donne moi un bloc en hexadécimal à chiffrer > (02)000000000000000000000000000000  
Et voilà le chiffré > 33cf27508fc1aa9611(e6)747d2baccfa2

Avec une autre clé:
Et voilà le chiffré > d3992114a3b99b2a0e(4f)ba7cc91a673e
Et voilà le chiffré > d3992114a3b99b2a0e(e7)ba7cc91a673e

Donne moi un bloc en hexadécimal à chiffrer > 00000000000000000000000000000000
Donne moi un bloc en hexadécimal à chiffrer > 00010000000000000000000000000000
Et voilà le chiffré > dd0fbdc9681224014208(d5)f739736175
Et voilà le chiffré > dd0fbdc9681224014208(67)f739736175

```

Donc les postions ne changent pas des swap ne change pas, surement liée à: self.perm = [6, 0, 4, 5, 15, 1, 14, 11, 2, 12, 9, 13, 8, 10, 7, 3]

Le FLAG fait 48 caracteres dont 3 blocks de 16

On sait qu'on à un maximum de 300 essais

J'essaye de faire un truc qui encode la partie d'avant pour voir si a un moment ça fait un cercle, mais non (StaturnCipherTest1.py)

Avec TestPermutation.py, on sait que les permutation reviennent au la liste initiale au bout de 14 essais (en plus de l'original)

Don on pourriat essayer d'encoder une partie connue 15 fois, comme ça la permuattion est annulée. Ainsi on a juste le xor et le SubBytes





