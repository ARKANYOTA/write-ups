charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}-!"
n = len(charset)

reversedict = {}

def decode(message):
    for char in charset:
        if char in charset:  # tjr True
            x = charset.index(char)
            y = pow(2, x, n+1)
            try:
                corespondingValue = charset[y]
            except:
                print(char, y, "is not encodable")
                pass
            if corespondingValue in reversedict.keys():
                print(char, "est un doublon de valeur", corespondingValue)
            else:
                reversedict[corespondingValue] = char

decode("")

print(reversedict)

for i in "828x6Yvx2sOnzMM4nI2sQ":
    print(reversedict[i], end="")

print()