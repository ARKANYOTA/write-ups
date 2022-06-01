def tour1(password):
    # string = str("".join( "".join(password[::-1])[::-1])[::-1])
    string = str(password[::-1])
    return [ord(c) for c in string]


def tour2(password):
    new = []
    while password != []:
        new.append(password[0])
        new.append(password[0] + password[password.index(password[ 1 %len(password)])])
        password.pop(0)
    return new

len_pass=34

def tour3(password):
    mdp = ["a"]*34 # ['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    for i in range(34):
        mdp[i], mdp[33-i] = chr(password[33-i]+(i%4)),  chr(password[i]+(i%4))
    return "".join(mdp)



mdp = "P4sS1R0bUst3Qu3C4" # input("Mot de passe : ")

if tour3(tour2(tour1(mdp))) == b'\xc2\xa1P\xc2\x876\xc2\xa8s\xc3\x89U\xc2\x851\xc2\x86T\xc2\x830\xc2\x95d\xc2\xb8V\xc3\x8av\xc3\xa7u\xc2\xa96\xc2\x84R\xc3\x88x\xc2\xa84xFw5':
    print("Bravo ! Le flag est 404CTF{" + mdp + "}")
else :
    print("Désolé, le mot-de-passe n'est pas correct")


#print("tour1", tour1(mdp))
#print("tour2", tour2(tour1(mdp)))
print("objecif ", b'\xc2\xa1P\xc2\x876\xc2\xa8s\xc3\x89U\xc2\x851\xc2\x86T\xc2\x830\xc2\x95d\xc2\xb8V\xc3\x8av\xc3\xa7u\xc2\xa96\xc2\x84R\xc3\x88x\xc2\xa84xFw5')
print("tour3   ", tour3(tour2(tour1(mdp))).encode())
print("tour3  !", tour3(tour2(tour1(mdp))), "!!!")
print("objecif!", "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5")
