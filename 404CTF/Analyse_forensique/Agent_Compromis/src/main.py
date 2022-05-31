#!/usr/bin/env python3
from scapy.all import *
import binascii

pcap_file = "capture-reseau.pcapng"

data = rdpcap(pcap_file)
print("Nombre de data", len(data))


def get_name_file():
    for ind,i in enumerate(data):
        if "never-gonna-give-you-up" in str(i):
            print(ind)

def get_start_and_end():
    arr_start = []
    arr_end = []
    ecx = 1
    for i in data:
        if "626567696E" in str(i):
            arr_start.append(ecx)
        if "656E64" in str(i):
            arr_end.append(ecx)
        ecx += 1

    return list(zip(arr_start, arr_end))

# >>> get_name_file()
# Et à la main on a:
# ["flag.txt", "hallebarde.png", "super-secret.pdf", "exfiltration.py"]
# >>> get_start_and_end()
# [(25721, 25721), (26074, 26081), (26075, 26082), (26332, 29926), (26333, 29927), (29980, 31278), (29981, 31279), (31324, 31475), (31325, 31476)]

start_end = [(26074, 26081), (26332, 29926), (29980, 31278), (31324, 31475)]
file_name = ["flag.txt", "hallebarde.png", "super-secret.pdf", "exfiltration.py"]

# Apres faudra verifier si avec le time
def get_one_packet(bdata):
    if not(b"404ctf" in bdata and b"hallebarde" in bdata): # on verifie si le packet est bien un dns vers ...hallebarde.404ctf.fr
        return -2

    if bdata[33] != 1: # On prend une seule ip sur les deux
        return -1

    bdata = bdata[55:]
    new_sdata = ""
    for c in bdata:
        if 32 <= c < 126:
            new_sdata += chr(c)
        else:
            return new_sdata
    if len(new_sdata)==0:
        return -3
    return new_sdata
def get_all_packets(filename, start, end):
    print("Traitement de : "+ filename)
    time_of_packet = 0
    file_data = b""
    ecx = start+1
    for c in data[start:end]:
        bdata = eval(str(c))
        debug = get_one_packet(bdata)
        if debug == -3:
            print("has null len: ", ecx)
        if debug == -2:
            print("Not a hallebarde.404ctf.fr ", ecx)
        elif debug == -1:
            time_of_packet = float(c.time)
            pass
        else:
            new_time_of_packet = float(c.time)
            if abs(new_time_of_packet - time_of_packet) >= 0.11:
                print("Time depaced: ", ecx, new_time_of_packet - time_of_packet)
                file_data += binascii.unhexlify("4"*32) # On rajout D*16 la ou il manque de la data
            else:
                # print(new_time_of_packet - time_of_packet)
                pass
            file_data += binascii.unhexlify(debug)

            time_of_packet = new_time_of_packet

        ecx += 1
    with open("My_version_of."+filename, "wb") as f:
        f.write(file_data)


def hex_print(data):
    ssdata = eval(str(data))
    if ssdata[33] == 1:
        return None
    sdata = ssdata[55:]
    
    new_sdata = ""
    for c in sdata:
        if 32 <= c < 126:
            new_sdata += chr(c)
        else:
            return new_sdata
    if len(new_sdata): return None
    return new_sdata

for i in range(4):
    get_all_packets(file_name[i], start_end[i][0], start_end[i][1])


