#   Spara packets som flödar i nätverket i en .pcap-fil för analys i t.ex. WireShark.
#   Användaren ska kunna specificera hur många packets som ska sparas (t.ex. 25 packets)
#   Anv. ska välja vilket protokoll som ska avlyssnas, standard är TCP.

# 

import argparse
from scapy.all import *

parser = argparse.ArgumentParser(description="Simple Packet Sniffer")
parser.add_argument("count", type=int, help="Specify how many packets to sniff")
parser.add_argument("protocol", type=str, help="Specify protocol to sniff")
parser.add_argument("filename", type=str, help="Name of the .pcap file that stores all the packets")
parser.add_argument("--interface", type=str, required=False, help="Network interface to collect packets from")

def performSniff(packetNum, protocol, filename):
    if args.interface:
        capture = sniff(count=packetNum, filter=protocol, iface=args.interface)
    else:
        capture = sniff(count=packetNum, filter=protocol)
    capture.summary()
    wrpcap(filename, capture)
try:
    args = parser.parse_args()
    performSniff(args.count, args.protocol, args.filename) 
except PermissionError:
    print("Error: this program can only be executed by root")