#!/usr/bin/python3.10
import random

s = [16, 3, 12, 9, 1, 60, 1, 3, 14, 39, 13, 16, 16, 1, 9, 13, 3, 39, 60,
    16, 16, 1, 60, 7, 39, 13, 3, 13, 18, 3, 13, 25, 14, 3, 1, 14, 60,
    13, 32, 13, 3, 39, 16, 18, 18, 3, 43, 16, 18, 3, 1, 43, 18, 16,
    13, 16, 1, 3, 1, 16, 13, 18, 60, 16, 3, 3, 14, 18, 13, 14, 16, 18,
    7, 3, 7, 25, 7, 7, 13, 13, 13, 3, 60, 1, 3, 13, 1, 25, 18, 16, 32,
    16, 60, 1, 7, 44, 18, 39, 39, 39, 60, 3, 1, 60, 3, 16, 13, 13, 14,
    1, 3, 39, 39, 31, 32, 39, 32, 18, 39, 3, 13, 32, 60, 7, 7, 39, 14,
    3, 18, 14, 60, 39, 18, 7, 1, 32, 13, 3, 14, 39, 39, 7, 1, 1, 13,
    29, 60, 13, 39, 14, 14, 16, 60, 1, 3, 44, 14, 3, 1, 1, 1, 39, 13,
    14, 39, 18, 3, 7, 13, 39, 32, 1, 43, 1, 16, 1, 3, 18, 14, 25, 32,
    7, 13, 39, 7, 1, 3, 60, 13, 13, 7, 18, 1, 3, 18, 1, 60, 7, 1, 39,
    14, 3, 39, 7, 31, 1, 7, 18, 7, 32, 3, 3, 14, 32, 14, 1, 32, 12,
    18, 31, 39, 1, 13, 13, 43, 44, 32, 3, 32, 60, 14, 60, 60, 7, 3, 1,
    3, 3, 14, 1, 60, 16, 44, 3, 1, 32, 13, 5, 16, 39, 3, 60, 7, 14, 3,
    13, 7, 31, 13, 39, 9, 3, 44, 13, 16, 14, 18, 18, 3, 7, 3, 3, 3, 7,
    3, 3, 16, 39, 3, 3, 13, 32, 13, 3, 18, 7, 10, 3, 18, 1, 7, 7, 18,
    13, 43, 18, 3, 32, 39, 32, 13, 1, 18, 10, 1, 32, 1, 16, 32, 3, 44,
    3, 18, 1, 1, 1, 16, 18, 25, 60, 1, 39, 1, 18, 60, 16, 1, 7, 3, 13,
    16, 18, 39, 14, 7, 14, 3, 14, 13, 7, 16, 10, 18, 13, 3, 16, 13, 3,
    32, 43, 13, 14, 1, 13, 1, 14, 18, 60, 7, 3, 7, 31, 1, 18, 26, 7,
    3, 3, 32, 1, 7, 18, 7, 1, 16, 18, 39, 14, 7, 3
]

def svalue(elt):
    random.seed(elt)
    return random.randint(0,30)
svalues = [svalue(elt) for ind, elt in enumerate(s)]

print("____________________TOP___________")
for i in range(len(svalues)//10):
    print(svalues[i*10:i*10+10], sum(svalues[i*10:i*10+10]))
print("____________________BOTTOM________")




def a(c, r=True):  # input character
    n = ord(c)
    if r: 
        random.seed(n)
    match n:
        case 0:
            return dict.fromkeys(range(10), 0)
        case _:
            return (d:=a(chr(n - 1), False)) | {(m:=random.randint(0, 9)): d[m] + random.randint(0,2)}

avalue = {chr(i) : a(chr(i)) for i in range(32, 128)}
print("____________________TOP___________")
for i,j in avalue.items():
    print(i, "|", list(j.values()), sum(list(j.values())))
# print("___________________MIDDEL_______")
# qsdfjklmqsdf = [(chr(i).encode(),list(a(chr(i)).values())) for i in range(0, 255)]
# qsdfjklmqsdf.sort(key=lambda x: x[1])
# for i in qsdfjklmqsdf:
#     print(i)
print("____________________BOTTOM________")

def b(p, n): # string mis en input, with n=1 pour l'input puis *2
    match list(p):
        case []:
            return []
        case [f, *rest]:
            print("f", f)
            print("a", list(a(f).values()))
            l = list(a(f).values()) + b(''.join(rest), n*2)
            random.seed(n)
            random.shuffle(l)
            return l

## p: array
#  Tu prend le premier nombre de la liste et si il est bon avec la fonction randomseed.randin(30) et que le reste de la liste passe la fonction il return True

def c(p, n=0):
    match p:
        case []:  # Si liste vide
            return n!=0
        case [f, *rest]:   # Si la liste a un elements minimum
            random.seed(s[n])
            print("En a 1 de vrai", p, len(p), sum(p))
            return random.randint(0,30) == f and c(rest, n + 1)
#

def bforindex(p, n): # string mis en input, with n=1 pour l'input puis *2
    match list(p):
        case []:
            return []
        case [f, *rest]:
            l = [f] + bforindex(''.join(rest), n*2)
            random.seed(n)
            random.shuffle(l)
            return l

def voirlindexb():
    s = "".join(chr(32+i) for i in range(38))
    print(s)
    out = bforindex(s, 1)
    print("ordre", {ind: ord(i)-32 for ind, i in enumerate(out)})

voirlindexb()

print(svalues[230:240])


# inpt = input("password:")
inpt = "CCCCCCCCCCCCCCCCCCCCCCCCCCMCCCCCCCCCCC"
islebonpass = c(b(inpt, 1))
print(len(s), len(inpt))
if islebonpass:
    print("Utilise ce mot de passe pour valider le challenge!")
else:
    print("Essaye Encore!")
