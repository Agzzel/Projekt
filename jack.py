import argparse
import hashlib

def crackPassword(hashedPass, wordList):
    with open(wordList, "r") as f:
        for line in f:
            hashedLine = hashlib.sha1()
            hashedLine.update(line.encode())
            hashValue = hashedLine.hexdigest()
            if hashValue == hashedPass:
                print("Found password:", line)

parser = argparse.ArgumentParser(description="A simple tool for cracking SHA1-hashed passwords")
parser.add_argument("hashedpass")
parser.add_argument("wordlist")

args = parser.parse_args()
crackPassword(args.hashedpass, args.wordlist)
