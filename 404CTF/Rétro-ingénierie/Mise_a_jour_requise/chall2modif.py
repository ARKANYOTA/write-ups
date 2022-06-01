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

def nombre_de_bien_place(s, l):
    a = 0
    for i in range(len(s)):
        if s[i] == l[i]:
            a+=1
    return a


def a(c, r=True):  # input character
    n = ord(c)
    if r: 
        random.seed(n)
    match n:
        case 0:
            return dict.fromkeys(range(10), 0)
        case _:
            return (d:=a(chr(n - 1), False)) | {(m:=random.randint(0, 9)): d[m] + random.randint(0,2)}

def b(p, n): # string en inut, with n
    match list(p):
        case []:
            return []
        case [f, *rest]:
            l = list(a(f).values()) + b(''.join(rest), n*2)
            random.seed(n)
            random.shuffle(l)
            return l

def seedrandom(n):
    random.seed(s[n])
    return random.randint(0,30)
def seedrandomlistgenerator():
    return [seedrandom(n) for n in range(380)]

seedrandomlist = seedrandomlistgenerator()



def reverseShuffle(seed, liste):
    random.seed(seed)
    backwardlist = list(range(len(liste)))
    random.shuffle(backwardlist)
    new_liste = [0]*len(liste)
    for ind, i in enumerate(liste):
        new_liste[backwardlist[ind]] = i
    return new_liste

def reverseLastB(s, n):
    new_s = reverseShuffle(2**38, s)
    return new_s

def c(p, n=0):  # Verifie si b est egal a seedrandomlust
    match p:
        case []:  # Si liste vide
            return n!=0
        case [f, *rest]:   # Si la liste a un elements minimum
            return seedrandomlist[n] == f and c(rest, n + 1)

print("SeedRandomList : ", seedrandomlist)
print("START BRUTE FORCE")
inpt = "404CTF{"+chr(1)*30+"}"
index = 9
best_point = (0, 0)
work_with = [[] for i in range(38)]
print(work_with)
for index in range(0, 38):
    best_point = (0, 0)
    for i in range(32, 128):
        new_inpt = list(inpt)
        new_inpt[index] = chr(i)
        new_inpt = "".join(new_inpt)
        txt = b(new_inpt, 1) 
        if nombre_de_bien_place(txt, seedrandomlist) > best_point[1]:
            best_point = (i,nombre_de_bien_place(txt, seedrandomlist))
            work_with[index] = []
        elif nombre_de_bien_place(txt, seedrandomlist) == best_point[1]:
            # print("also work with", i, chr(i))
            work_with[index].append(chr(i))


    # print(best_point, chr(best_point[0]))
    work_with[index].append(chr(best_point[0]))
print(work_with)

print("END BRUTE FORCE")
if c(b(inpt, 1)):
    print("Utilise ce mot de passe pour valider le challenge!")
else:
    print("Essaye Encore!")

print("CEST ICI")
print(nombre_de_bien_place(b(inpt,1), seedrandomlist))



avalue = {chr(i) : a(chr(i)) for i in range(32, 128)}
print("____________________TOP___________")
nbval = {i: 0 for i in range(50)}
for i,j in avalue.items():
    if 17 in list(j.values()):
        print(i, "|", list(j.values()), sum(list(j.values())))

for i in seedrandomlist:
    nbval[i] += 1

print(nbval)



print("___________________MIDDEL_______")
qsdfjklmqsdf = [(chr(i).encode(),list(a(chr(i)).values())) for i in range(32, 128)]
qsdfjklmqsdf.sort(key=lambda x: x[1])
for i in qsdfjklmqsdf:
    print(i)
print("____________________TOP___________")

 # print(reverseLastB(s, len(s)))
 # print(reverseLastB(s, len(s))[-10:])
