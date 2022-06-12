>Agent, nous avons découvert un smart contract de Hallebarde qui permet d'obtenir de l'argent gratuitement. Il sert également à s'authentifier en tant que nouveau membre de Hallebarde. Nous voulons que vous vous fassiez passer pour un de leurs membres. Nous avons récemment trouvé un endpoint qui semble leur servir de portail de connexion. Introduisez-vous dans leur système et récupérez toutes les informations sensibles que vous pourrez trouver.
>
>- Contrat à l'adresse : `0xb8c77090221FDF55e68EA1CB5588D812fB9f77D6`
>- Réseau de test Ropsten

1. Après une analyse du code et notamment la non-utilistion de la libraire SafeMath, ce qui nous met la puce à l'oreille on observe une possibilité d'Overflow dans la fonction `transfer`. En effet, lors de la soustraction du montant, le programme ne vérifie pas si l'on possède le montant minimum mais seulement si notre argent n'est pas nul.

2. Ainsi en effectuant `getMoney(n)`, puis `transfer(m)` avec m>n, on obtient un underflow et une somme d'argent énorme ce qui nous permet de passer la première condition de `EnterHallebarde()`

3. La seconde condition pose elle un peu plus de problèmes puisqu'elle cherche à vérifier **tx.origin != msg.sender**. En solidity ``tx.origin`` correspond à la racine de la transaction la où ``msg.sender`` est l'adresse directe de la requête (en résumé). Ainsi, pour que ``tx.origin`` soit différent de ``msg.sender``, il faut passer par un contrat intermédiaire qu'on appellera et qui fera ensuite lui les appels au contrat du chall. On aura alors ``msg.sender`` = l'adresse du contrat intermédiaire et `tx.origin` = l'adresse de l'user avec lequel on appelle le contrat intermédiaire.

4. On transcrit alors les opérations à faire dans le fichier `YesBabe.sol` qu'on deploy ensuite sur le réseau Ropsten grâce à [Remix](https://remix.ethereum.org).

5. On fait ensuite les appels au contrat et on rentre l'adresse sur laquelle est déployé le contrat dans le netcat : 


| `404CTF{5M4r7_C0N7r4C7_1NC3P710N_37_UND3rF10W_QU01_D3_P1U5_F4C113}` |
|---------------------------------------------------------------------|
