# De la poésie

## Description
```
Debout dans l'allée, un homme singulier regarde fixement l'imposante horloge qui, d'un vert canard, plonge la rangée de livres dans une ambiance bucolique très agréable. Perturbé par cette étrange figure, vous n'avez même pas remarqué que quelqu'un s'était rapproché de vous.
 
« Ne faites pas attention à lui, dit la figure à moitié cachée par l'ombre d'une rangée de livres. Il cherche de l'inspiration pour son nouveau poème, et depuis quelque temps, il est fasciné par les chiffres. Je ne sais pas ce qu'il a fait, mais cela lui a complètement retourné le cerveau, il est devenu incompréhensible. »
 
La voix féminine laissa place à une grande dame à lunette ronde, elle tenait en main un livre fraichement imprimé.
 
« Vous le connaissez ?
— Bien sûr ! Nous nous échangeons nos poèmes pour les commenter et les améliorer, mais ces dernières semaines il ne me parle presque plus, et je ne comprends rien du tout à ce qu'il m'a donné ! Regardez ça. »
 
Elle vous tendit le livre pour que vous puissiez l'examiner. La couverture est toute simple, il y a seulement marqué le titre : Être pair ou ne pas l'être.
 
Cependant, en l'ouvrant, vous vous rendez compte que ce n'est pas un livre, mais une collection d'images ! Christelle remarqua votre mine stupéfaite et ajouta :
 
« C'est ce que je vous disais, ce n'est pas de la poésie à ce que je sache. »
 
D'abord étonné, vous devenez curieux et pensif, qu'est-ce que cela peut-il bien-être ? Après quelques secondes passées à feuilleter l'ouvrage, vous vous exclamez :
 
«Bien sûr !
— Comment ça ? Vous avez une idée de ce que cela peut être ?
— Je pense oui, je crois bien pouvoir le déchiffrer. »
 
 
Sckathach#9336
```



On passe par le DeLaPoesie.ipynb

On comprend le sujet avec le titre du livre: Être pair ou ne pas l'être

On a 8 images, on les convertit en binaire, on a 8 bits par image, on a donc 64 bits, on les convertit en ascii, on a donc 8 ca

`404CTF{d3_L4_p03S1e_qU3lqU3_P3u_C0nT3mp0r4in3}`


404CTF{l3_L4_p0#S1e[qU3laU3_P3u_C0nT3mp0r4jn3}
404CTF{l3_L4_p03S1e[qU3laU3_P3u_C0nT3mp0r4jn3}
`404CTF{d3_L4_p03S1e_qU3lqU3_P3u_C0nT3mp0r4in3}`


On fix ce qui va pas en francais: avec  "i*8 + (place de 0 a 7)".jpg
  [i]   chr, binchr
 '[706],4,00110100',
 '[707],0,00110000',
 '[708],4,00110100',
 '[709],C,01000011',
 '[710],T,01010100',
 '[711],F,01000110',
 '[712],{,01111011',
 '[713],l,01101100',
 '[714],3,00110011',
 '[715],_,01011111',
 '[716],L,01001100',
 '[717],4,00110100',
 '[718],_,01011111',
 '[719],p,01110000',
 '[720],0,00110000',
 '[721],#,00100011',
 '[722],S,01010011',
 '[723],1,00110001',
 '[724],e,01100101',
 '[725],[,01011011',
 '[726],q,01110001',
 '[727],U,01010101',
 '[728],3,00110011',
 '[729],l,01101100',
 '[730],a,01100001',
 '[731],U,01010101',
 '[732],3,00110011',
 '[733],_,01011111',
 '[734],P,01010000',
 '[735],3,00110011',
 '[736],u,01110101',
 '[737],_,01011111',
 '[738],C,01000011',
 '[739],0,00110000',
 '[740],n,01101110',
 '[741],T,01010100',
 '[742],3,00110011',
 '[743],m,01101101',
 '[744],p,01110000',
 '[745],0,00110000',
 '[746],r,01110010',
 '[747],4,00110100',
 '[748],j,01101010',
 '[749],n,01101110',
 '[750],3,00110011',
 '[751],},01111101',



