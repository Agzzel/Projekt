import argparse
import hashlib

parser = argparse.ArgumentParser(description="A simple program for cracking hashed passwords using a wordlist. Supported algorithms are SHA1, SHA256 and MD5")
parser.add_argument("hashedpass",type=str, help="The hashed password to crack")
parser.add_argument("wordlist", type=str, help="Wordlist used to check for a matching password")
parser.add_argument("algo", type=str, help="The algorithm used to hash the password")

args = parser.parse_args()

def crackPassword(hashedPass, wordList, algorithm):
    a = algorithm.lower()
    foundPass = False
    try:
        f = open(wordList,"r")
    except FileNotFoundError:
        print("Error: could not find wordlist")
        return
    else:
        for line in f:
            if a == "sha1":
                hashedLine = hashlib.sha1(line.strip().encode('utf-8')).hexdigest()
            elif a == "sha256":
                hashedLine = hashlib.sha256(line.strip().encode('utf-8')).hexdigest()
            elif a == "md5":
                hashedLine = hashlib.md5(line.strip().encode('utf-8')).hexdigest()
            else:
                print("Error: unsupported algorithm. Please choose between SHA1, SHA256 or MD5.")
                return
                sys.exit()
            
            if hashedLine == hashedPass:
                f.close()
                print("Found password:", line)
                foundPass = True
                return

        if foundPass == False:
            f.close()
            print("Error: could not find a matching password. Check that the hash entered is correct or try changing the wordlist.")


crackPassword(args.hashedpass, args.wordlist, args.algo)
