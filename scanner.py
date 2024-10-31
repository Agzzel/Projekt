import nmap
import argparse
import ipaddress

nm = nmap.PortScanner()

def scanTarget(target):
    try:
        ipaddress.ip_address(target)
    except ValueError:
        print("Error: invalid IP adress")
        return
    nm.scan(target, '1-1024', '-sV')
    print("Scan complete")
    response = input("Do you wish to save the scan to a text file? (y/n)\n")
    if response == "y":
        resultFile = open("results.txt", "w")
        resultFile.write(str(nm[target])) 
        resultFile.close()
        print("Saved scan results to results.txt")
    else:
        print(nm[target])

def scanFile(targetFile):
    try:
        f = open(targetFile, "r")
    except FileNotFoundError:
        print("Error: file not found")
        return
    response = input("Do you wish to save the scan to a text file? (y/n)\n")
    if response == "y":
        print("Scanning in progress...")
        resultFile = open("results.txt", "w")
        for line in f:
            try:
                ipaddress.ip_address(line)
            except ValueError:
                print(f"Error: line {line.strip()} is not a valid IP address")
                return
            nm.scan(line, '1-1024', '-sV')
            resultFile.write(str(nm[line]))
        resultFile.close()
        print("Saved scan results to results.txt")
    else:
        print("Scanning in progress...")
        for line in f:
            try:
                ipaddress.ip_address(line)
            except ValueError:
                print(f"Error: line {line.strip()} is not a valid IP address")
                return
            nm.scan(line)
            print(str(nm[line]))
    f.close()
parser = argparse.ArgumentParser(description="A simple network scanner. The program will scan ports 1-1024 in a single IP adress or a range of adresses from a file.")
subparsers = parser.add_subparsers(dest="command")

ip_parser = subparsers.add_parser("scan_ip", help="Scan an IP adress.")
ip_parser.add_argument("adress", type=str, help="IP adress to scan")

file_parser = subparsers.add_parser("scan_file", help="Scan IP adresses from file")
file_parser.add_argument("file", type=str, help="The target file to scan")

args = parser.parse_args()
if args.command == "scan_ip":
    scanTarget(args.adress)
elif args.command == "scan_file":
    scanFile(args.file)
