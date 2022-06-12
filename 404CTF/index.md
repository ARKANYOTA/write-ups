# 404 CTF

## Analyse_forensique

- [Floppy](./Analyse_forensique/Floppy/Floppy.md)
- [Ping_Pong](./Analyse_forensique/Ping_Pong/Ping_Pong.md)
- [Agent_Compromis 1/3,2/3](./Analyse_forensique/Agent_Compromis/Agent_Compromis.md)
- [SOS_RAID 1/2, 2/2](./Analyse_forensique/SOS_RAID/SOS_RAID.md)

## Rétro-ingénierie

- [Renverse la tour 1/2 2/2](./Rétro-ingénierie/Renverse_la_tour/Renverse_la_tour.md)
- [Mise à jour requise](./Rétro-ingénierie/Mise_a_jour_requise/Mise_a_jour_requise.md)
- [Pas de mise à jour](./Rétro-ingénierie/Pas_de_mise_a_jour/Pas_de_mise_a_jour.md) (Oublié)
- [Mot de passe](./Rétro-ingénierie/Mot_de_Passe/Mot_de_Passe.md)

## Stéganographie

- [La plume à la main](./Stéganographie/La_plume_à_la_main.md)
- [PNG : Un logo obèse 1/4](./Stéganographie/Un_logo_obèse.md)

## Web
- [Fiché JS](./Web/Fiché_JS/Fiché_JS.md)
- [Le Braquage](./Web/Le_braquage/Le_braquage.md)

## Cryptanalyse
- [Un Rsa Incassable?](./Cryptanalyse/Un_RSA_incassable.md)
- [Un Simple Oracle 1/2](./Cryptanalyse/Un_Simple_Oracle.md)
- [Un Simple Oracle 2/2](./Cryptanalyse/Un_Simple_Oracle2.md)
- [Weak Signature](./Cryptanalyse/Week_Signature/Weak_Signature.md)
- [La Fonte des hashs](./Cryptanalyse/La_fonte_des_hashs.md)

## OSINT:
> Je n'ai rien d'intéressant à expliquer, allez sur d'autres writes-ups
- Equipment Désuet
- À l'aube d'un échange

## Programmation

- [Compression](./Programmation/Compression/Compression.md)
- [Découpe](./Programmation/Découpe/Découpe.md)
- [128code128](./Programmation/128code128/128code128.md)

## Exploitation de binaire
- [Trop facile](./Exploitation_de_binaires/Trop_Facile.md)

## Divers
- [pierre-papier-hallebarde](./Divers/Pierre-papier-Hallebarde.md)
- [Je suis une théière](./Divers/Je_suis_une_théière.md)
- [Discord](./Divers/Discord.md)
- [Bienvenu](./Divers/Bienvenu.md)
- Sondage

## Web3:
- [Pense-bête](./Web3/Pense-bête.md)
- [La guerre des contrats 1/2](./Web3/La_Guerre_des_Contrats.md)


## Mes resultats

### Classement

![Classement](./MarkdownImages/Classement.png)

### CTFD_PARSER

```markdown
$ python ctfd_parser.py -t https://ctf.404ctf.fr/ -u ARKANYOTA -T 12 -p 404CTF{0h_n0n_c'35t_p45_ç4.}
       _____ _______ ______  _   _____
      / ____|__   __|  ____|| | |  __ \
     | |       | |  | |__ __| | | |__) |_ _ _ __ ___  ___ _ __
     | |       | |  |  __/ _` | |  ___/ _` | '__/ __|/ _ \ '__|    v1.1
     | |____   | |  | | | (_| | | |  | (_| | |  \__ \  __/ |
      \_____|  |_|  |_|  \__,_| |_|   \__,_|_|  |___/\___|_|       @podalirius_

[+] Found 10 categories !
[>] Parsing challenges of category : Analyse forensique
   [>] ✅ Floppy
   [>] ✅ Ping Pong
   [>] ✅ Un agent compromis [1/3]
   [>] ✅ Un agent compromis [2/3]
   [>] ✅ SOS RAID [1/2]
   [>] ❌ Hackllebarde ransomware [1/4]
   [>] ✅ SOS RAID [2/2]
   [>] ❌ Un agent compromis [3/3]
   [>] ❌ Hackllebarde ransomware [2/4]
   [>] ❌ Hackllebarde ransomware [3/4]
[>] Parsing challenges of category : Cryptanalyse
   [>] ✅ Un RSA incassable?
   [>] ✅ La fonte des hashs
   [>] ✅ Un simple oracle [1/2]
   [>] ✅ Un simple oracle [2/2]
   [>] ✅ Weak Signature
   [>] ❌ Une lettre bien mystérieuse
   [>] ❌ Enigma
   [>] ❌ Hackllebarde ransomware [4/4]
   [>] ❌ Puisse Kocher être avec vous
   [>] ❌ Un point c'est tout
   [>] ❌ Dégâts collatéraux
[>] Parsing challenges of category : Divers
   [>] ✅ Sondage
   [>] ✅ Bienvenue
   [>] ✅ Discord
   [>] ✅ Pierre-papier-Hallebarde
   [>] ✅ Je suis une théière
   [>] ❌ Par câble
   [>] ❌ Un utilisateur suspicieux [1/2]
   [>] ❌ Un utilisateur suspicieux [2/2]
   [>] ❌ GoGOLFplex
   [>] ❌ 8 vers 10
   [>] ❌ Joutes, Arches, Vallées & Arbalètes
[>] Parsing challenges of category : Exploitation de binaires
   [>] ✅ Trop facile
   [>] ❌ Sans protection
   [>] ❌ Cache-cache
   [>] ❌ Patchwork
   [>] ❌ Coffre-fort
   [>] ❌ Changement d'architecture [2/2]
[>] Parsing challenges of category : Programmation
   [>] ✅ Compression
   [>] ✅ Découpé
   [>] ✅ 128code128
   [>] ❌ Données corrompues
[>] Parsing challenges of category : Renseignement en sources ouvertes
   [>] ✅ Equipement désuet
   [>] ✅ À l'aube d'un échange
   [>] ❌ Nous sommes infiltrés !
   [>] ❌ Collaborateur suspect
   [>] ❌ Nom d'une nouvelle recrue !
[>] Parsing challenges of category : Rétro-ingénierie
   [>] ✅ Mot de passe ?
   [>] ✅ Renverse la tour ! [1/2]
   [>] ✅ Mise à jour requise
   [>] ✅ Renverse la tour ! [2/2]
   [>] ✅ Pas de mise à jour...
   [>] ❌ Frida-me
   [>] ❌ Changement d'architecture [1/2]
   [>] ❌ Nos amies les portes
   [>] ❌ Fourchette
[>] Parsing challenges of category : Stéganographie
   [>] ✅ La plume à la main
   [>] ✅ PNG : Un logo obèse [1/4]
   [>] ❌ PNG : Drôles de chimères [2/4]
   [>] ❌ PNG : Toujours obèse [3/4]
   [>] ❌ Stéréographie
   [>] ❌ La Méthode Française
   [>] ❌ PNG :  Une histoire de filtres [4/4]
[>] Parsing challenges of category : Web
   [>] ✅ Fiché JS
   [>] ✅ Le braquage
   [>] ❌ Du gâteau
   [>] ❌ En construction
[>] Parsing challenges of category : Web3
   [>] ✅ Pense-bête
   [>] ✅ La guerre des contrats [1/2]
   [>] ❌ Clé publique
   [>] ❌ La guerre des contrats [2/2]
```
