import argparse
from scapy.all import *

parser = argparse.ArgumentParser(description="A simple program for capturing packets. Requires root privileges to run!")
parser.add_argument("count", type=int, help="Specify how many packets to sniff")
parser.add_argument("protocol", type=str, help="Specify protocol to sniff")
parser.add_argument("filename", type=str, help="Name of the file where packets will be stored after capture")
parser.add_argument("--interface", type=str, required=False, help="Network interface to collect packets from")

def performSniff(packetNum, protocol, filename):
    print("Working...")
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
    sys.exit()
args = parser.parse_args()
performSniff(args.count, args.protocol, args.filename)