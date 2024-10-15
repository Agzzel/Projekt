# Axel Sterner
# Scriptet har enbart testats på Linux

import nmap

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

running = True
while running:
    option = input("Choose an option: scan input, scan file, exit \n")

    if option == "scan input":
        target = input("Enter the target's IP: ")
        scanTarget(target)

    elif option == "scan file":
        target = input("Enter filename: ")
        print(target)
        scanFile(target)

    elif option == "exit":
        print("Shutting down \n")
        running = False
    
    else:
        print("Invalid option")
