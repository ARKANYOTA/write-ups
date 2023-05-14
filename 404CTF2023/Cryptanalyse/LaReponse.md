aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa => gvshnmijdwalablggmejiqvrhkixhns
mais

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab => hwtionjkexbmbcmhhnfkjrwsiljyiot


on conclut que en changant le dernier char: sa change le premier



On change ainsi
on se rend compte que quand on change un char a la place -i (en partant de la fin) de +1

le prmier char est changer de +1
le deuxieme                   +2
.
.
.
le i eme                  de +i
et le reste en bordel



```
In [7]: def diff_entre_chaines(chaine1, chaine2):
   ...:     if len(chaine1) != len(chaine2):
   ...:         raise ValueError("Les chaînes doivent avoir la même longueur.")
   ...:
   ...:     difference = []
   ...:     for c1, c2 in zip(chaine1, chaine2):
   ...:         difference.append((ord(c2) - ord(c1))%26)
   ...:
   ...:     return difference
   ...:
   ...: chaine1 = "gvshnmijdwalablggmejiqvrhkixhns"
   ...: chaine2 = "hwtionjkexbmbcmhhnfkjrwsiljyiot"
   ...:
   ...: difference = diff_entre_chaines(chaine1, chaine2)
   ...: print(difference)
```

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaabaa
aaaaaaaaaaaaaaaaaaaaaaaaaaabaaa
aaaaaaaaaaaaaaaaaaaaaaaaaabaaaa
aaaaaaaaaaaaaaaaaaaaaaaaabaaaaa
aaaaaaaaaaaaaaaaaaaaaaaabaaaaaa
aaaaaaaaaaaaaaaaaaaaaaabaaaaaaa
aaaaaaaaaaaaaaaaaaaaaabaaaaaaaa
aaaaaaaaaaaaaaaaaaaaabaaaaaaaaa
aaaaaaaaaaaaaaaaaaaabaaaaaaaaaa
aaaaaabaaaaaaaaaaaaaaaaaaaaaaaa
aaaaabaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaabaaaaaaaaaaaaaaaaaaaaaaaaaa
abaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

zbaaaaaaaaaaaaaaaaaaaaaaaaaaaaa



En changant le dernier      (-1) on a +1 partout
En changant le avant dernier(-2) on a +1 partout saut en 0 et 29 ou on a +2
Out[5]: '[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]'

En changant le              (-3) on a +2 partout saut en 0 et 29 ou on a +2
Out[8]: '[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]'


-4:
Out[9]: '[1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]'

Out[10]: '[1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]'


-11:
Out[11]: '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]'


-25:
Out[13]: '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 25, 25, 25, 25, 25]'

-26
Out[14]: '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 0, 0, 0, 0, 0]'

-30
Out[15]: '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5]'



A trouver:
Out[16]: '[15, 21, 5, 3, 7, 19, 20, 22, 6, 1, 15, 23, 5, 7, 14, 2, 8, 3, 16, 2, 25, 13, 20, 15, 0, 12, 25, 18, 4, 25, 15]'




A trouver en diff:
Out[22]: '[9, 0, 13, 22, 20, 7, 12, 13, 3, 5, 15, 12, 5, 6, 3, 22, 2, 17, 12, 19, 17, 23, 25, 24, 19, 2, 17, 21, 23, 12, 23]'

xdaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  lettre -1
oyoaaaaaaaaaaaaaaaaaaaaaaaaaaaa  lettre -2
+
lboaaaaaaaaaaaaaaaaaaaaaaaaaaaa  sum des 2, les 2 derniere lettre de juste

xgudaaaaaaaaaaaaaaaaaaaaaaaaaaa

```
In [77]: for x,i in zip([23, 12, 23, 21, 17, 2, 19, 24, 25, 23, 17, 19, 12, 17, 2, 22, 3, 6, 5, 12, 15, 5, 3, 13, 12, 7, 20, 22, 13, 0, 9],range(1,32)):
    ...:     arr = nb_pi(i)
    ...:     arr2 = arr*x
    ...:     arr3 = arr2%26
    ...:     arr4 = arr3+97
    ...:     arr5 = numpy.vectorize(lambda x:chr(x))(arr4)
    ...:     print(i, str("".join(list(arr5))))
```

```
In [89]: for x,i in zip([23, 12, 23, 21, 17, 2, 19, 24, 25, 23, 17, 19, 12, 17, 2, 22, 3, 6, 5, 12, 15, 5, 3, 13, 12, 7
    ...: , 20, 22, 13, 0, 9],range(1,32)):
    ...:     arr = nb_pi(i)
    ...:     arr2 = arr*x
    ...:     arr3 = arr2%26
    ...:     arr4 = arr3+97
    ...:     arr5 = numpy.vectorize(lambda x:chr(x))(arr4)
    ...:     print(i, str("".join(list(arr5))))
    ...:
1 xdaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
2 oyoaaaaaaaaaaaaaaaaaaaaaaaaaaaa
3 xgudaaaaaaaaaaaaaaaaaaaaaaaaaaa
4 fqkqfaaaaaaaaaaaaaaaaaaaaaaaaaa
5 rsisijaaaaaaaaaaaaaaaaaaaaaaaaa
6 yeweweyaaaaaaaaaaaaaaaaaaaaaaaa
7 tomomomhaaaaaaaaaaaaaaaaaaaaaaa
8 cwewewewcaaaaaaaaaaaaaaaaaaaaaa
9 zcycycycybaaaaaaaaaaaaaaaaaaaaa
10 dugugugugudaaaaaaaaaaaaaaaaaaaa
11 rsisisisisijaaaaaaaaaaaaaaaaaaa
12 hmomomomomomhaaaaaaaaaaaaaaaaaa
13 mcycycycycycyoaaaaaaaaaaaaaaaaa
14 jisisisisisisijaaaaaaaaaaaaaaaa
15 cweweweweweweweyaaaaaaaaaaaaaaa
16 esisisisisisisiseaaaaaaaaaaaaaa
17 dugugugugugugugugxaaaaaaaaaaaaa
18 umomomomomomomomomuaaaaaaaaaaaa
19 fqkqkqkqkqkqkqkqkqkvaaaaaaaaaaa
20 oycycycycycycycycycyoaaaaaaaaaa
21 pwewewewewewewewewewelaaaaaaaaa
22 vkqkqkqkqkqkqkqkqkqkqkvaaaaaaaa
23 dugugugugugugugugugugugxaaaaaaa
24 naaaaaaaaaaaaaaaaaaaaaaanaaaaaa
25 mcycycycycycycycycycycycyoaaaaa
26 tomomomomomomomomomomomomotaaaa
27 umomomomomomomomomomomomomogaaa
28 esisisisisisisisisisisisisiseaa
29 naaaaaaaaaaaaaaaaaaaaaaaaaaaana
30 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
31 jisisisisisisisisisisisisisisis
```



Avec ça on a leidaaaaaaaaaaaaaaaaaaaaaaaaaaa : les 3 dernierers



def nb_pi(index):

    arr = numpy.array([0]*31)
    if index == 1:
        arr[index-1] = +1
        arr[index] = -1
        return arr
    if index == 31:
        arr[index-1] = 1
        return arr-nb_pi(index-1)
    arr[index-1] = 1
    arr[index] = -1
    return arr-nb_pi(index-1)


----
Evolution finale:

```
message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaj
message chiffre  : pebqwvrsmfjujkuppvnsrzeaqtrgqwb

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaaaarj
message chiffre  : gmjyedzaunrcrscxxdvazhmiybzoyej

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaaaars
message chiffre  : pvshnmijdwalablggmejiqvrhkixhns

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaaanes
message chiffre  : pvfuazvwqjnynoyttzrwvdieuxvkuaf

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaajees
message chiffre  : pvfdjiefzswhwxhcciafemrndgetdjo

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaachees
message chiffre  : pvfdlkghbuyjyzjeekchgotpfigvflq

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaweaaa
message chiffre  : gvshjiefzswhwxhcciafemrndgetdjo

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaylees
message chiffre  : pvfdhgcdxqufuvfaagydckplbecrbhm

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaanllees
message chiffre  : pvfdhtpqkdhshisnntlqpxcyorpeouz

message en clair : aaaaaaaaaaaaaaaaaaaaaaaafillees
message chiffre  : pvfdhtuvpimxmnxssyqvuchdtwujtze

message en clair : aaaaaaaaaaaaaaaaaaaaaaabeillees
message chiffre  : pvfdhtuwqjnynoyttzrwvdieuxvkuaf

message en clair : aaaaaaaaaaaaaaaaaaaaaaqleillees
message chiffre  : pvfdhtuwgzdodeojjphmltyuknlakqv

message en clair : aaaaaaaaaaaaaaaaaaaaacoleillees
message chiffre  : pvfdhtuwgbfqfgqllrjonvawmpncmsx

message en clair : aaaaaaaaaaaaaaaaaaaaksoleillees
message chiffre  : pvfdhtuwgbpapqavvbtyxfkgwzxmwch

message en clair : aaaaaaaaaaaaaaaaaaaxnsoleillees
message chiffre  : pvfdhtuwgbpxmnxssyqvuchdtwujtze

message en clair : aaaaaaaaaaaaaaaaaatensoleillees
message chiffre  : pvfdhtuwgbpxfgqllrjonvawmpncmsx

message en clair : aaaaaaaaaaaaaaaaabsensoleillees
message chiffre  : pvfdhtuwgbpxfhrmmskpowbxnqodnty

message en clair : aaaaaaaaaaaaaaaaxesensoleillees
message chiffre  : pvfdhtuwgbpxfhojjphmltyuknlakqv

message en clair : aaaaaaaaaaaaaaateesensoleillees
message chiffre  : pvfdhtuwgbpxfhocciafemrndgetdjo

message en clair : aaaaaaaaaaaaaagneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocioglksxtjmkzjpu

message en clair : aaaaaaaaaaaaaprneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidvazhmiybzoyej

message en clair : aaaaaaaaaaaavurneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqvuchdtwujtze

message en clair : aaaaaaaaaaahourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcbjokadbqagl

message en clair : aaaaaaaaaayjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqczhmiybzoyej

message en clair : aaaaaaaaagsjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznsoehfuekp

message en clair : aaaaaaaacesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznuqgjhwgmr

message en clair : aaaaaaabcesjourneesensoleillees
message chiffre  : qxihmzbeplajsvdszvjwujroehfuekp

message en clair : aaaaaaazdesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupfigvflq

message en clair : aaaaaavedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupadbqagl

message en clair : aaaaajmedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamkzjpu

message en clair : aaaapumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzoyej

message en clair : aaaelumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzscin

message en clair : aacclumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzsekp

message en clair : anpclumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzsexc

message en clair : ncpclumedesjourneesensoleillees
message chiffre  : rzllrfimyvlvfjsiqncqpfolymbwkfx

message en clair : anpclumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzsexc

message en clair : clpclumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzsexe

message en clair : rlpclumedesjourneesensoleillees
message chiffre  : ezylefvmlvyvsjfidnpqcfbllmowxfb

message en clair : aapclumedesjourneesensoleillees
message chiffre  : cvsduthwtbcxshbcvddcmnhpnmmsrxc

message en clair : clpclumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzsexe

message en clair : acyaaaaaaaaaaaaaaaaaaaaaaaaaaaa
message chiffre  : gvshnmijdwalablggmejiqvrhkixhpu

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
message chiffre  : gvshnmijdwalablggmejiqvrhkixhns

message en clair : lpaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
message chiffre  : gvshnmijdwalablggmejiqvrhkixhnd

message en clair : cjnclumedesjourneesensoleillees
message chiffre  : lntnnvsqwnxbfdgqsjsatdgxemvksjq

message en clair : clpclumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzsexe

message en clair : napclumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzsexp

message en clair : ncnclumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzsezr

message en clair : lenclumedesjourneesensoleillees
message chiffre  : pvfdhtuwgbpxfhocidqcznupamzsezp
Alors la, chapeau !
``` 

Methode a suivre:
``` 
#Inutile
def nb_pi(index):

    arr = numpy.array([0]*31)
    if index == 1:
        arr[index-1] = +1
        arr[index] = -1
        return arr
    if index == 31:
        arr[index-1] = 1
        return arr-nb_pi(index-1)
    arr[index-1] = 1
    arr[index] = -1
    return arr-nb_pi(index-1)

def diff_entre_chaines(chaine1, chaine2):
    if len(chaine1) != len(chaine2):
        raise ValueError("Les chaînes doivent avoir la même longueur.")
    difference = []
    for c1, c2 in zip(chaine1, chaine2):
        difference.append((ord(c2) - ord(c1))%26)
    return difference

def ar(lis):
    h = numpy.array([0]*31)
    for x,i in zip(lis,range(1,32)):
        arr = numpy.array([0]*31)
        if i!=31: arr[i] = -1
        arr[i-1] = 1
        arr2 = (arr*x)%26
        h += arr2
        print("".join(list(numpy.vectorize(lambda x:chr(x))((arr2)+97))))
    "".join(list(numpy.vectorize(lambda x:chr(x))((h%26)+97)))

dist = diff_entre_chaines("<message chiffre courant>", "pvfdhtuwgbpxfhocidqcznupamzsezp")
print(dist)
ar(dist[::-1])
```
Prendre a derniere sortie qui n'est pas `aaa...aaa`

et la sommer avec le `<message en clair courant>`

Jusqu'a que il n'ai plus que des aaa...aaa


404CTF{lenclumedesjourneesensoleillees}
