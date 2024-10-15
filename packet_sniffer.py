#   Spara packets som flödar i nätverket i en .pcap-fil för analys i t.ex. WireShark.
#   Användaren ska kunna specificera hur många packets som ska avlyssnas (t.ex. 25 packets)
#   Anv. ska välja vilket protokoll som ska avlyssnas, standard är TCP.

import argparse
from scapy.all import *

parser = argparse.ArgumentParser(description="Simple Packet Sniffer")
parser.add_argument("count", help="Specify how many packets should be sniffed")
parser.add_argument("protocol", help="Specify protocol to sniff")
parser.add_argument("filename", help="Name of the .pcap file that stores all the packets")

args = parser.parse_args()
capture = sniff(count = int(args.count), filter=args.protocol)
capture.summary()
wrpcap(args.filename, capture) 