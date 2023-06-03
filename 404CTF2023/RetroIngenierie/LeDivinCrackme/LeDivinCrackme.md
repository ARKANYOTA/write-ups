# Le Divin Crackme

## Description

```
Jean-Jacques Rousseau vous prend à part : « J'ai déjà raconté la fois où j'ai rencontré le Marquis de Sade ? Non ? Tu en as de la chance... Mes amis avaient plannifié une entrevue entre lui et moi en ville. Avant même de lui parler, il me paraissait étrange. Quoique l'air bien à l'aise, les premiers mots qu'il prononça furent 'Me feriez vous le plaisir de jouer en ma compagnie ?'. Malgré sa demande, j'avais comme l'impression de ne pas vraiment avoir le choix et, en effet, avant de pouvoir lui répondre il poursuivit 'Voici ce que nous allons entreprendre : Vous trouvez mon mot de passe et vous voilà libre. Autrement, je ne réponds plus de rien.'.
Tandis que je m'essayais à son drôle jeu, il me présentait ses points de vue sur les institutions, et, bien que je partage ses opinions sur la nécessité d'accepter l'humain le plus naturel, laissant la corruption des mœurs installée par les institutions derrière nous, je restais critique face à ses aspects les plus libertins... »
 
« Il serait malvenu de te raconter ce qui se passa par la suite considérant mon échec, mais je suis curieux, aurait tu réussi, toi ? Essaye donc, tu ne risques rien en ce qu'il te concerne ! Pour vérifier que tu ne m'as pas répondu au hasard, j'aimerais que tu me précises avec quel programme le binaire a été compilé ainsi que la fonction spécifique qui est utilisée pour tester le mot de passe. »
 
 
Format : 404CTF{compilateur:fonction:mot_de_passe} | tout en minuscules sauf le mot de passe
Lowengeist#9608
```


format:
404CTF{compilateur:fonction:mot_de_passe}
404CTF{gcc:main:L4_pH1l0soPh13_d4N5_l3_Cr4cKm3}

On lance avec ghidra:

on obtient le main:


```
undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  char local_48 [10];
  char acStack_3e [10];
  char acStack_34 [44];

  printf("Mot de passe ? : ");
  __isoc99_scanf(&DAT_0010201a,local_48);
  sVar2 = strlen(local_48);
  if ((((sVar2 == 0x1e) && (iVar1 = strncmp(acStack_3e,"Ph13_d4N5_",10), iVar1 == 0)) &&
      (iVar1 = strncmp(local_48,"L4_pH1l0so",10), iVar1 == 0)) &&
     (iVar1 = strncmp(acStack_34,"l3_Cr4cKm3",10), iVar1 == 0)) {
    printf(&DAT_00102040);
    return 0;
  }
  printf(&DAT_00102078);
  return 1;
}
```
On reformate:

```

undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  char local_48 [10];
  char acStack_3e [10];
  char acStack_34 [44];

  printf("Mot de passe ? : ");
  __isoc99_scanf(&DAT_0010201a,local_48);
  sVar2 = strlen(local_48);
  if (((
            (sVar2 == 0x1e) &&   // On comprend que il y a 30 chars
            (iVar1 = strncmp(acStack_3e,"Ph13_d4N5_",10), iVar1 == 0)
        ) &&
       (iVar1 = strncmp(local_48,"L4_pH1l0so",10), iVar1 == 0)
       ) &&
     (iVar1 = strncmp(acStack_34,"l3_Cr4cKm3",10), iVar1 == 0)
     ) {
    printf(&DAT_00102040);
    return 0;
  }
  printf(&DAT_00102078);
  return 1;
}
```

On a le mot de passe:
    L4_pH1l0soPh13_d4N5_l3_Cr4cKm3



On execute:
arkanyota@Arkans-MacBook-Air LeDivinCrackme % objdump -s --section .comment divin-crackme

divin-crackme:	file format elf64-x86-64
Contents of section .comment:
 0000 4743433a 20284465 6269616e 2031322e  GCC: (Debian 12.
 0010 322e302d 31342920 31322e32 2e3000    2.0-14) 12.2.0.


On a le compilateur:
    GCC


