import nmap
import argparse

nm = nmap.PortScanner()

def scanTarget(target):
    print("Scanning in progress...")
    nm.scan(target)
    response = input("Do you wish to save the scan to a text file? (y/n)\n")
    if response == "y":
        resultFile = open("results.txt", "w")
        resultFile.write(str(nm[target])) 
        resultFile.close()
    else:
        print(nm[target])

def scanFile(targetFile):
    f = open(targetFile, "r")
    response = input("Save scan results to file? (y/n)\n")
    if response == "y":
        resultFile = open("results.txt", "w")
        for line in f:
            nm.scan(line)
            resultFile.write(str(nm[line]))
    else:
        for line in f:
            nm.scan(line)
            print(str(nm[line]))
    f.close()

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

ip_parser = subparsers.add_parser("scan_ip", help="Scan an IP adress")
ip_parser.add_argument("adress", type=str, help="IP adress to scan")

file_parser = subparsers.add_parser("scan_file", help="Scan IP adresses from file")
file_parser.add_argument("file", type=str, help="The target file to scan")

args = parser.parse_args()
if args.command == "scan_ip":
    scanTarget(args.adress)
elif args.command == "scan_file":
    scanFile(args.file)
