#coding=utf-8
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os
def CreateRSAKeys():
    code = 'nooneknows'
    key = RSA.generate(2048)
    encrypted_key = key.exportKey(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")
    # 私钥
    with open('my_private_rsa_key.bin', 'wb') as f:
        f.write(encrypted_key)
    # 公钥
    with open('my_public_rsa_key.pem', 'wb') as f:
        f.write(key.publickey().exportKey())
if __name__ == '__main__':
    CreateRSAKeys()
