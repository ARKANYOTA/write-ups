#!/usr/bin/env sage
from sage.all import ZZ
import pyperclip
import time


while False:
    a = int(input("a:").split(" ")[-1])
    b = int(input("b:").split(" ")[-1])
    c = int(input("c:").split(" ")[-1])
    print(a,b,c)
    # a,b,c = 129748011239318971419419099113380388234, 8314724981232796464104623162815968501622239507789606871315987361933464118508, 624075198444090721826682402815071185511598806447785877595960594893773776783159296194476483502398027735795697852904
    R = ZZ['x']
    x = R.gen()

    # Exemple : polynôme x^3 - 6x^2 + 11x - 6 (racines : 1, 2, 3)
    coeffs = [-a**3-2*c+3*b*a, 3*(a**2-b), -6*a, 6]  # Coefficients de degré 0 à 3
    p = sum(c * x**i for i, c in enumerate(coeffs))
    print(f"Polynôme : {p}")

    # Trouver les racines
    racines = p.roots(multiplicities=False)
    racines.sort()
    result = str(racines).replace(" ", "")[1:-1]
    pyperclip.copy(result)
    print("Racines :", result)


# https://realpython.com/python-sockets/
import socket
import select


HOST = "challenges.404ctf.fr"  # The server's hostname or IP address
PORT = 30069  # The port used by the server

print("start connection")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.setblocking(False)

    time.sleep(1)
    readable, writable, _ = select.select([s], [s], [], 0.5)
    if readable:
        print("Read userName")
        data = s.recv(1024)
        if data:
            print(f"Received Name: {data!r}")
            time.sleep(1)

    readable, writable, _ = select.select([s], [s], [], 0.5)
    if writable:
        print("Se,n username")
        s.send(b"nolan\n")
        time.sleep(1)





    
    while True:
        readable, writable, _ = select.select([s], [s], [], 0.5)


        result = ""
        if readable:
            data = s.recv(1024)
            if data:
                print(f"Received: {data!r}")
                ase,bse,cse,*args = data.decode().split("\n")
                a = int(ase.split(" ")[-1])
                b = int(bse.split(" ")[-1])
                c = int(cse.split(" ")[-1])
                print(a,b,c)
                # a,b,c = 129748011239318971419419099113380388234, 8314724981232796464104623162815968501622239507789606871315987361933464118508, 624075198444090721826682402815071185511598806447785877595960594893773776783159296194476483502398027735795697852904
                R = ZZ['x']
                x = R.gen()

                # Exemple : polynôme x^3 - 6x^2 + 11x - 6 (racines : 1, 2, 3)
                coeffs = [-a**3-2*c+3*b*a, 3*(a**2-b), -6*a, 6]  # Coefficients de degré 0 à 3
                p = sum(c * x**i for i, c in enumerate(coeffs))
                print(f"Polynôme : {p}")

                # Trouver les racines
                racines = p.roots(multiplicities=False)
                racines.sort()
                result = str(racines).replace(" ", "")[1:-1]
                print("Racines :", result)

            else:
                print("Connection closed by server.")
                break

        if writable:
            print("Send Hi")
            s.send(result.encode() + b"\n")
            time.sleep(1)
        
        
    
    

