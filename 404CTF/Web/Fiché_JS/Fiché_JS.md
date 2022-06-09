>  Après plusieurs mois de recherches à fouiller dans le passé de Hallebarde, nous avons mis la main sur une vieille plateforme d'hébergement de fichiers qu'ils utilisaient jusqu'en 2010. Cela remonte à 12 ans maintenant ! Les pratiques en termes de sécurité ont radicalement changé depuis et ce qui semblait alors incassable ne l'est peut-être plus du tout maintenant.
> 
> À vous de jouer : trouvez un moyen d'outrepasser le système de protection existant et récupérez les fichiers encore hébergés sur ce site !

> Site: https://fiche-js.404ctf.fr

1. On lance la console, puis on va dans les sources js
2. On voit une Fonction : Que j'ai mis dans "Fiché_JS_Funtion.md"
3. On l'exécute puis on voit du JSFuck : Que j'ai mis dans "Fiché_JS_JSFuck.md"
4. On enlève les guillemets et les 2 parentheses de fin
5. Sa donne :
```
) {
/* FONCTIONNEMENT */
var key = $(".keypad").keypad(function (pin) {
  if (pin == "240801300505131273100172") {
    document.location.href = "./nob03y_w1lL_Ev3r_fiNd_th15_PaGe.html";
  …
```
6. On va sur la page fiche-js.404ctf.fr/nob03y_w1lL_Ev3r_fiNd_th15_PaGe.html
7. On Copie Colle:

| `404CTF{Haha_J3_5ui$_f4N_dObfu5c4tIoN_en_JS}` |
|-----------------------------------------------|
