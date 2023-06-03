from ECDSA import *
from secret import FLAG


p = 0xf1fd178c0b3ad58f10126de8ce42435b3961adbcabc8ca6de8fcf353d86e9c03
a = 0xf1fd178c0b3ad58f10126de8ce42435b3961adbcabc8ca6de8fcf353d86e9c00
b = 0xee353fca5428a9300d4aba754a44c00fdfec0c9ae4b1a1803075ed967b7bb73f
n = 0xf1fd178c0b3ad58f10126de8ce42435b53dc67e140d2bf941ffdd459c6d655e1
G = Point(0xb6b3d4c356c139eb31183d4749d423958c27d2dcaf98b70164c97a2dd98f5cff, 0x6142e0f7c8b204911f9271f0f3ecef8c2701c307e8e4c9e183115a1554062cfb)
E = Curve(a, b, p, n, G)

def signature():
    global COUNTER_QUERY
    while True:
        m = input('Entrez le message à signer, au format hexadécimal:\n>')
        try:
            b = bytes.fromhex(m)
            sig = E.sign(b)
            print(m, b, sig, E.verify(sig, b))
            assert E.verify(sig, b)
        except:
            print("Erreur dans la génération de la signature, l'oracle va fermer")
            return 0

        print("Voici la signature associée à votre message")
        print(sig)


def verify():
    while True:
        print("Tapez exit pour quitter le service")
        try:
            print("Entrez le message à vérifier (hexadécimal)")
            m = input('>')
            if m == 'exit':
                return 0
            b = bytes.fromhex(m)
            print("Entrez la première partie de la signature:")
            r = int(input('>'))
            print("Entrez la seconde partie de la signature:")
            s = int(input('>'))
            sig = (r, s)
        except:
            print("Erreur, le service doit fermer")
            return 0
        check = E.verify(sig, b)
        if check:
            print("La signature est valide")
        else:
            print("La signature est invalide")


def debug():
    print("Cette partie est strictement interdite au public!")
    print("Pour vous authentifier, merci d'entrer le secret principal de la session:")
    try:
        secret = int(input('>'))
    except:
        return 0
    if secret == E.d1:
        print("Login réussi. Voici les informations que vous avez sauvegardées la dernière fois:")
        print(FLAG)
    else:
        print("Erreur, authentification échouée")
        return 0


def main():
    print(E.PK)
    while True:
        print("Que souhaitez-vous faire?")
        print("1 - Accéder à l'oracle de signature")
        print("2 - Accéder à l'oracle de vérification des signatures")
        print("3 - Revoir la clé publique de cette session")
        print("4 - Accéder au DEBUG, strictement interdit au public")
        choice = int(input('>'))
        match choice:
            case 1:
                signature()
            case 2:
                verify()
            case 3:
                print(E.PK)
            case 4:
                debug()
            case _:
                print("Erreur dans votre saisie, merci de réessayer")



if __name__ == '__main__':
    main()