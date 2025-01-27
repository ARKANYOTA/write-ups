# Man vs Matrix x3c.tf

## Code source de résolution du challenge
```python
from a import bytes_to_long
from sage.all import *

p = next_prime(2**24)
F = GF(p)
S = vector(F, map(ord, "Mvm"))
B = matrix(F, 9,9, [0]*9*9)
A = [[0]*9 for i in range(9)]
print(A)
gen = F(2)

for i in range(9):
    print("en ------------")
    A[i][0] = S[0]
    A[i][1] = S[1]
    A[i][2] = S[2]
    A[i][3] = S[0]
    A[i][4] = S[1]
    A[i][5] = S[2]
    A[i][6] = S[0]
    A[i][7] = S[1]
    A[i][8] = S[2]
    print(S)

    for j in range(len(S)):
        S[j] = gen**S[j]

    A[i][0] *= S[0]
    A[i][1] *= S[0]
    A[i][2] *= S[0]
    A[i][3] *= S[1]
    A[i][4] *= S[1]
    A[i][5] *= S[1]
    A[i][6] *= S[2]
    A[i][7] *= S[2]
    A[i][8] *= S[2]
    print(S)

    print("vm ------------")

print(A)
C = matrix(F, 9,9, A)

print(C)

print(C.det())
print("inversematrix")
print(C.inverse())
print("result")
print(C.inverse() * vector(F, [6192533, 82371, 86024, 4218430, 12259879, 16442850, 6736271, 7418630, 15483781]))
print("endinv")
# print(C * vector(F, [11144394, 16776215, 1555054, 3471308, 1510282, 12133261, 829684, 7548780, 13046208]))

# flag = b"MVM{???????????????????????????}"
# seed = flag[4:-1]
# 
# flag = vector(F, [bytes_to_long(seed[i:i+3]) for i in range(0, len(seed), 3)])
# print(flag)
# 
# print("rese: ", C * flag)
# 
# 
# class RNG:
# 
#     def __init__(self, seed):
#         self.p = next_prime(2**24)
#         self.F = GF(self.p)
#         # self.M = matrix(self.F, 3,3, [bytes_to_long(seed[i:i+3]) for i in range(0, len(seed), 3)])
#         self.state = vector(self.F, map(ord, "Mvm"))
#         self.gen = self.F(2)
#         print(self.p)
#         print("F: ", self.F)
#         print("state: ", self.state)
#         print(self.gen)
# 
#     def get_random_num(self):
#         print("gen ---------")
#         print(self.state)
#         # out = self.M * self.state
# 
#         for i in range(len(self.state)):
#             self.state[i] = self.gen**self.state[i]
# 
#         print("end gen gen ---------")
#         # return out * self.state
#         return self.state
# 
# 
# # for i in range(255):
# #     for j in range(255):
# #         for k in range(255):
# #             print(bytes([i,j,k]))
# # 
# #             rng = RNG(seed)
# #             if 6192533 == rng.get_random_num():
# #                 print(i,j,k)
#             
# 
# 
# rng = RNG(b"???")
# 
# print(rng.get_random_num())
```

### Explication du code:

#### Code de a
J'arrive pas à executer sage et Crypto en meme temps, donc je recode la fonction bytes_to_long
```python
import struct
import sys
def bytes_to_long(s):
    """Convert a byte string to a long integer (big endian).

    In Python 3.2+, use the native method instead::

        >>> int.from_bytes(s, 'big')

    For instance::

        >>> int.from_bytes(b'\x00P', 'big')
        80

    This is (essentially) the inverse of :func:`long_to_bytes`.
    """
    acc = 0

    unpack = struct.unpack

    # Up to Python 2.7.4, struct.unpack can't work with bytearrays nor
    # memoryviews
    if sys.version_info[0:3] < (2, 7, 4):
        if isinstance(s, bytearray):
            s = bytes(s)
        elif isinstance(s, memoryview):
            s = s.tobytes()

    length = len(s)
    if length % 4:
        extra = (4 - length % 4)
        s = b'\x00' * extra + s
        length = length + extra
    for i in range(0, length, 4):
        acc = (acc << 32) + unpack('>I', s[i:i+4])[0]
    return acc

bytes_to_long(b"AAA")
```

### Explication du code:

```python
class RNG:
    def __init__(self, seed):
        self.p = next_prime(2**24)
        self.F = GF(self.p)
        self.M = matrix(self.F, 3,3, [bytes_to_long(seed[i:i+3]) for i in range(0, len(seed), 3)])
        self.state = vector(self.F, map(ord, "Mvm"))
        self.gen = self.F(2)

    def get_random_num(self):
        out = self.M * self.state

        for i in range(len(self.state)):
            self.state[i] = self.gen**self.state[i]

        return out * self.state

flag = b"MVM{???????????????????????????}"
seed = flag[4:-1]

rng = RNG(seed)
samples = []

for i in range(9):
    samples.append(rng.get_random_num())

print(f"{samples = }")
# samples = [6192533, 82371, 86024, 4218430, 12259879, 16442850, 6736271, 7418630, 15483781]
```

On à la longeur du flag qui est $27 = 9*3$ (en enlevant le flag MVM{ et la } à la fin)

Pourquoi $9*3?$ ?  
On a que le seul endroit ou est uilisé le flag est ce bout de code:
```python 
self.M = matrix(self.F, 3,3, [bytes_to_long(seed[i:i+3]) for i in range(0, len(seed), 3)])
```
On se rend compte que le flag est découpé en par 9 blocs de 3 caractères mit dans une matrice 3x3. 

Dans la suite je noterai cette matrice:

$$M = \begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}$$

```python
self.state = vector(self.F, map(ord, "Mvm"))
```
et on a un vecteur state initialisé à $[77, 118, 109]$ (Mvm en ascii):

$$state = \begin{pmatrix}
77 \\
118 \\
109
\end{pmatrix} = \begin{pmatrix}
M \\
v \\
m
\end{pmatrix}$$


```python
self.p = next_prime(2**24)
self.F = GF(self.p)
```
On a aussi que absoluement tout ce qui est présenté (Avant et apres) est modulo $p$ (le prochain nombre premier après $2^{24}$)

On essaye de comprendre ce que fait la fonction get_random_num:
```python
def get_random_num(self):
    out = self.M * self.state              # Ligne 1

    for i in range(len(self.state)):  # Partie 2
        self.state[i] = self.gen**self.state[i]  

    return out * self.state               # Retour
```

#### Ligne 1 
On a $out = M \times state$ (Multiplication de matricielle clasique, car les tailles sont good) 

Soit 

$$M = \begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix} * \begin{pmatrix}
M \\
v \\
m
\end{pmatrix} = \begin{pmatrix}
aM + bV + cM \\
dM + eV + fM \\
gM + hV + iM
\end{pmatrix}$$

#### Partie 2 
On modifie le state:

$$state_{old} = \begin{pmatrix}
M \\
v \\
m
\end{pmatrix}$$

Et:

$$state_{new} = \begin{pmatrix}
2^M \\
2^v \\
2^m
\end{pmatrix}$$

(Je rappelle que tout est modulo $p$)

#### Retour
On retourne $out \times state_{new}$ (Oh non les tailles sont pas bonnes, mais on peut faire un produit scalaire)

$$out \times state_{new} = \begin{pmatrix}
aM + bV + cM \\
dM + eV + fM \\
gM + hV + iM
\end{pmatrix} \times \begin{pmatrix}
2^M \\
2^v \\
2^m
\end{pmatrix} = 
2^M(aM + bV + cM) + 2^v(dM + eV + fM) + 2^m(gM + hV + iM)$$

On a donc que la fonction get_random_num retourne:

$$2^M(aM + bV + cM) + 2^v(dM + eV + fM) + 2^m(gM + hV + iM)$$

Et modifie $state$

$$state = \begin{pmatrix}
2^M \\
2^v \\
2^m
\end{pmatrix}$$

Pour le premier appel de get_random_num on a en se basant sur les valeurs de samples (premiere valeur):
$$2^M(aM + bV + cM) + 2^v(dM + eV + fM) + 2^m(gM + hV + iM) = 6192533$$

### Oh non il font ça plusieurs fois (9 pour être précis) (Spoiler ça nous arange)

Il font ça 9 fois, ce qui nous fait 9 équations: (Et chaqune a 9 inconues)
Sauf que les state sont differants, si on en sait le suite ça donne:

$$state_0 = (M, v, m), state_1 = (2^M, 2^v, 2^m), state_2 = (2^{2^M}, 2^{2^v}, 2^{2^m}), \dots$$
On calcule (toujours modulo $p$) les valeurs de state pour les 9 premiers états:

$$2^M(aM + bv + cm) + 2^v(dM + ev + fm) + 2^m(gM + hv + im) = 6192533$$
$$2^{2^M}(a2^M + b2^v + c2^m) + 2^{2^v}(d2^M + e2^v + f2^m) + 2^{2^m}(g2^M + h2^v + i2^m) = 82371$$

$$\dots$$

9 équations, 9 inconues, de facon modulaire, on met tout ça dans un matrice:

On calcule les valeurs de la matrice a trouver noté A: (equation qui s'affiche pas sur github)

$$C = \begin{pmatrix}
2^M*M & 2^M*v & 2^M*m & 2^v*M & 2^v*v & 2^v*m & 2^m*m & 2^m*v & 2^m*m \\
2^{2^M}*2^M & 2^{2^M}*2^v & 2^{2^M}*2^m & 2^{2^v}*2^M & 2^{2^v}*2^v & 2^{2^v}*2^m & 2^{2^m}*2^m & 2^{2^m}*2^v & 2^{2^m}*2^m \\
\dots & \dots & \dots & \dots & \dots & \dots & \dots & \dots & \dots
\end{pmatrix}$$


Ainsi en posant (T de la tranposé) $S$ les valeurs du sample 
$$S=[6192533\;82371\;86024\;4218430\;12259879\;16442850\;6736271\;7418630\;15483781]^T$$

et en posant $$X= (a \; b \; c \; d \; e \; f \; g \; h \; i)^T$$ les valeurs a obtenir

On a $CX = S$

On inverse A:
$$C^{-1}CX = C^{-1}S$$
$$X = C^{-1}S$$
```pyhton 
print(C.inverse() * vector(F, [6192533, 82371, 86024, 4218430, 12259879, 16442850, 6736271, 7418630, 15483781]))
```
Output: $(7090542, 3355762, 6252149, 5137236, 3223662, 3497780, 7484255, 7174495, 6698102)$


On a donc les valeurs de X, on les convertis en caractères et on a le flag

Je vais sur un python terminal pout re avoir le module Crypto:
On passe de long to bytes
```python
from Crypto.Util.number import long_to_bytes
for i in [7090542, 3355762, 6252149, 5137236, 3223662, 3497780, 7484255, 7174495, 6698102]:
    print(long_to_bytes(i))
```

Output:
```
b'l1n'
b'34r'
b'_fu'
b'NcT'
b'10n'
b'5_4'
b'r3_'
b'my_'
b'f4v'
```

On a donc le flag: `MVM{l1n34r_fuNcT10n5_4r3_my_f4v}`
