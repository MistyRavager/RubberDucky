import os
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(file_name):
    with open(f"./target/{file_name}", 'rb') as f:
        data = f.read()

    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(f"./target/{file_name}", 'wb') as f:
        f.write(encrypted)

for file in os.listdir("./target"):
    encrypt_file(file)
