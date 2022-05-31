#!/usr/bin/env python3

from scapy.all import *
pcap_file = "ping.pcapng"

data = rdpcap(pcap_file)

if __name__ == "__main__":
    for packet in data[::2]: # On prend que 1 packet sur 2
        print(chr(packet.wirelen-42), end="")
    print()
