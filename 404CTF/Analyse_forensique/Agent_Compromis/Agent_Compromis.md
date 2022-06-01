> Nous avons surpris un de nos agents en train d'envoyer des fichiers confidentiels depuis son ordinateur dans nos locaux vers Hallebarde. Malheureusement, il a eu le temps de finir l'exfiltration et de supprimer les fichiers en question avant que nous l'arrêtions.
>
> Heureusement, nous surveillons ce qu'il se passe sur notre réseau et nous avons donc une capture réseau de l'activité de son ordinateur. Retrouvez le fichier qu'il a téléchargé pour exfiltrer nos fichiers confidentiels.

1. On ouvre le .pcapng avec wireshark
2. On voit que le packet `25719` est un GET exfiltration.py
3. On récupère le résultat, on l'ouvre et a la dernière ligne on a :


| `404CTF{t3l3ch4rg3m3n7_b1z4rr3}` |
|----------------------------------|

> Maintenant, nous avons besoin de savoir quels fichiers il a exfiltré.
>
> Format du flag : 404CTF{fichier1,fichier2,fichier3,...} Le nom des fichiers doit être mis par ordre alphabétique.

4. On crée le programme `main.py`: on a:

```python
25720
26069
26070
26327
26328
29975
29976
31319
31320
```

5. On `unhexlify` les packets suivant : pour avoir le nom de chaque fichier

```python
>>> import binascii
>>> binascii.unhexlify("666c61672e747874")
b'flag.txt'
>>> binascii.unhexlify("68616c6c6562617264652e706e67")
b'hallebarde.png'
>>> binascii.unhexlify("73757065722d7365637265742e706466")
b'super-secret.pdf'
>>> binascii.unhexlify("657866696c74726174696f6e2e7079")
b'exfiltration.py'
```

6. On tape:

```python
>>> "404CTF{"+",".join(sorted(["flag.txt", "hallebarde.png", "super-secret.pdf", "exfiltration.py"]))+"}" 
```

Et on a:


| `404CTF{exfiltration.py,flag.txt,hallebarde.png,super-secret.pdf}` |
|--------------------------------------------------------------------|

> Il semblerait que l'agent compromis a effacé toutes les sauvegardes des fichiers qu'il a exfiltré. Récupérez le contenu des fichiers.
>
> Le réseau était un peu instable lors de la capture, des trames ont pu être perdues.


7. On continue le programme main.py

... Et j'y arrive pas a flag
