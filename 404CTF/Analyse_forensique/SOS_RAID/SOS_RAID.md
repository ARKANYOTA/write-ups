> Nous avons réussi à infiltrer **Hallebarde** et à exfiltrer des données. Cependant nos agents se sont fait repérer durant la copie et ils n'ont pas pu copier l'intégralité des données. Pouvez-vous analyser ce qu'ils ont réussi à récupérer ?

1. On xor disk0.img avec disk1.img vers le fichier disk2.img:
   `python2 xorpython2.py disk0.img disk1.img disk2.img` (Source Internet)
2. Puis on execute PythonRaid5.py. Un programe que j'ai fait: (Perdu a cause d'une mauvaise manipulation)
3. On a le disque original dans EndDisk.img
4. On le binwalk: On obtient un zip avec un flag.txt
5. On l'ouvre et on a:


| `404CTF{RAID_5_3st_p4s_tr3s_c0mpl1qu3_1abe46685ecf}` |
| ------------------------------------------------------ |

> Bravo, vous avez réussi à récupérer les données. Cependant, il s'avère que l'un des fichiers a été corrompu pendant la copie. Pouvez-vous le réparer pour en extraire des informations ?

6. On a aussi un fichier flag_....png
7. Si on l'ouvre on appercoit que il est corompu
8. Avec le wikipedia PNG: On decouvre que le headeur est mauvais
9. On change la Signature PNG 89 50 4E 47 0D 00 00 0A => 89 50 4E 47 0D 0A 1A 0A
10. On change la taille du IDHR chunk 00 00 FF 0D => 00 00 00 0D (13)
11. On change la taille de l'image de 00 00 F2 88 => 00 00 02 88 (648)
    Car: On sait que la width est de 1152 Donc si l'image est en 16:9 On trouve 648 height
12. Finalement on ouvre la version modifié on appercoit:


| `404CTF{L4_C0rr_pt10N_s3_r_p4r_}` |
| ----------------------------------- |
