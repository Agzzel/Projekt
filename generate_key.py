from cryptography.fernet import Fernet

def create_key(key_name):
    key = Fernet.generate_key() 
    with open(key_name, "wb") as key_file:
        key_file.write(key) 