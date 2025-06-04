perm_orig = [6, 0, 4, 5, 15, 1, 14, 11, 2, 12, 9, 13, 8, 10, 7, 3]
perm = perm_orig.copy()

j = 0
while True:
    perm = [perm[perm_orig[i]] for i in range(len(perm))]
    print(perm)
    if str(perm) == str(list(range(len(perm)))):
        print(j, perm)
        exit(0)
    j+=1