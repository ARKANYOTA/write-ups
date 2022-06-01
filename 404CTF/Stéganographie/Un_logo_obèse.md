> L'heure est grave. Hallebarde ne se cache plus et échange des messages en toute liberté. Un tel manque de précautions de leur part est alarmant, et même presque suspect. Un logo a été utilisé dans l'un de leurs courriels et d'après de premières analyses, il pourrait avoir été employé pour ouvrir un canal de stéganographie. Pourriez-vous tirer cela au clair ?

> Ficher: steg.png

1. On execute `binwalk steg.png --extract`
2. On aperçoit un zip, et dedans une image
3. On l'ouvre et on trouve :

| `404CTF{0b3z3_f1l3_h4z_zup3r_spy_s3cr37}` |
|-------------------------------------------|
