text = "2i1s4i1s15d1o49i1o4d1o3i1o15d1o22d1o20d1o19i1o7d1o5d1o2i1o55i1o1d1o19d1o17d1o18d1o29i1o12i1o26i1o8d1o59d1o27i1o6d1o17i1o12d1o7d1o5i1o1d1o2d1o12i1o9d1o26d1o"


import re

# a = re.compile(r'[0-9]*[a-z]*').findall(text)
df = ""
c = re.compile(r'([0-9]*)([a-z]*)').findall(text)[:-1]
for b in c:
    df += b[1]*int(b[0])
print(df)

import deadfish
dff = df.split("o")
anc_val = 0
for i in dff:
    h = deadfish.deadfish((anc_val*"i")+i)
    anc_val = int(h)
    print(chr(int(h)), end="")
print()
# print(a)
