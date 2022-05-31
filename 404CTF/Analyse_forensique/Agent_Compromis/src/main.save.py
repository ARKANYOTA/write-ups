#!/usr/bin/env python

from scapy.all import *
import binascii

pcap_file = "capture-reseau.pcapng"

data = rdpcap(pcap_file)

print("Nombre de data", len(data))

def get_name_file():
    for ind,i in enumerate(data):
        if "never-gonna-give-you-up" in str(i):
            print(ind)

# Pour la v2: prendre tout les truc avec hallebarde.404ctf.fr
# Sachant que des packet on ete perdus

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

# >>> ["flag.txt", "hallebarde.png", "super-secret.pdf", "exfiltration.py"]
# [(25721, 25721), (26074, 26081), (26075, 26082), (26332, 29926), (26333, 29927), (29980, 31278), (29981, 31279), (31324, 31475), (31325, 31476)]

start_end = [(26074, 26081), (26332, 29926), (29980, 31278), (31324, 31475)]
file_name = ["flag.txt", "hallebarde.png", "super-secret.pdf", "exfiltration.py"]


# Apres faudra verifier si avec le time
def get_one_packet(bdata):
    if not(b"404ctf" in bdata and b"hallebarde" in bdata): # on verifie si le packet est bien un dns vers ...hallebarde.404ctf.fr
        return None

    if bdata[33] == 1: # On prend une seule ip sur les deux
        return None

    bdata = bdata[55:]
    new_sdata = ""
    for c in bdata:
        if 32 <= c < 126:
            new_sdata += chr(c)
        else:
            return new_sdata
    if len(new_sdata)==0: return None
    return new_sdata
def get_all_packets(filename, start, end):
    file_data = b""
    for c in data[start:end]:
        bdata = eval(str(c))
        debug = get_one_packet(bdata)
        if debug is not None:
            file_data += binascii.unhexlify(debug)
    with open("My_version_of."+filename, "wb") as f:
        f.write(file_data)

for i in range(4):
    get_all_packets(file_name[i], start_end[i][0], start_end[i][1])



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

# acc = ""
# for i in data:
#     s = hex_print(i)
#     if s is not None:
#         acc += s
# 
# acc = acc[len('never-gonna-give-you-up'):]
# print(acc)
# # print(data[0])
# all_data = set()
# for i in range(0, len(data)):
#     all_data.add(str(data[i]))
# 
# for i in all_data:
#     print(i)
# 
# for i in range(0, len(data)):
#     #if data[i].getlayer(IP).dst == "10.1.0.10":
#     if True:
#         payload = data[i].load.decode("utf-8")
#         print(payload)
#         output += payload
# 
# output_file = open("result.b64", "w")
# output_file.write(output)
# output_file.close()
#
