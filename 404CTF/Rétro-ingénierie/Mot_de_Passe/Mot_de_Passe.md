> Nous avons retrouvé un petit ordinateur avec un drôle de programme pour chiffrer le mot de passe administrateur. Ta mission est simple : déchiffrer ce mot de passe !

1. On passe `Mdp.class` dans [https://jdec.app/](https://jdec.app)  
2. On peut même le tester avec: https://www.tutorialspoint.com/compile_java_online.php/
3. On a:
```javascript
String var1 = "4/2@PAu<+ViNgg%^5NS`#J\u001fNK<XNW(_";
```
4. on fait un script python:
```python
>>> a = "4/2@PAu<+ViNgg%^5NS`#J\u001fNK<XNW(_"
>>> for i in range(len(a)):
...     print(chr(ord(a[i]) + i), end="")
```

| `404CTF{C3_sYst3mE_es7_5ecUrisE}` |
|-----------------------------------|
