# Koden har enbart testats på Linux

from generate_key import create_key
from cryptography.fernet import Fernet
import argparse

def generate_key(key_name):
    create_key(key_name)

def encrypt(message, keyInput):
    with open(keyInput, "rb") as keyFile:
        key = keyFile.read()
    cipher = Fernet(key) 
    message = message.encode()
    cipher_text = cipher.encrypt(message)
    fileName = input("Enter the name to save the encrypted file as (must end in .enc):")
    with open(fileName, "wb") as encoded_file:
        encoded_file.write(cipher_text)


def decrypt(fileName, key):
    with open(fileName, "rb") as encrypted_message:
        message = encrypted_message.read()
    with open(key, "rb") as key_file:
        key = key_file.read()
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(message)
    plainTextFile = open("output.txt","w")
    plainTextFile.write(plain_text.decode())
    plainTextFile.close()

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

key_parser = subparsers.add_parser("generate", help="Generate an encryption key")
key_parser.add_argument("name", type=str, help="name of the key file")

encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a text string")
encrypt_parser.add_argument("message", type=str, help="text to encrypt")
encrypt_parser.add_argument("key", type=str, help="encryption key")

decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt an encrypted file")
decrypt_parser.add_argument("filename", type=str, help="File to decrypt")
decrypt_parser.add_argument("key", type=str, help="Decryption key")

args = parser.parse_args()
if args.command == "encrypt":
    encrypt(args.message, args.key)
elif args.command == "decrypt":
    decrypt(args.filename, args.key)
elif args.command == "generate":
    generate_key(args.name)




