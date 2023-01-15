from Crypto.Protocol.KDF import PBKDF2 #This module is used to derive a key from a password using the PBKDF2 (Password-Based Key Derivation Function 2) algorithm.
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b'\xe2\x16]\xe3\x08\x91\xe8\x15\xe84\x05\x11\xbf\xea\x17?\x1f]#G\xb8\x00\x1e*\xa7DGJX\xe414'
password = 'mypassword'

key = PBKDF2(password, salt, dkLen=32)

msg = input("Enter a Message: ")

message = msg.encode()

cipher = AES.new(key, AES.MODE_CBC)
cipher_data = cipher.encrypt(pad(message, AES.block_size))

print("Encrypted Data = ", cipher_data)

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(cipher_data)

with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)
