import os
from cryptography.fernet import Fernet

def load_key():
    return open("key.key", "rb").read()

def decrypt_file(file_name):
    with open(f"./target/{file_name}", 'rb') as f:
        data = f.read()

    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(f"./target/{file_name}", 'wb') as f:
        f.write(decrypted)


for file in os.listdir("./target"):
    decrypt_file(file)