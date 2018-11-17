#coding=utf-8
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
import os
import sys
def Decrypt(filename,datakey):
    code = 'nooneknows'
    with open(filename, 'rb') as fobj:
        private_key = RSA.importKey(datakey, passphrase=code)
        enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                    for x in (private_key.size_in_bytes(), 
                                                    16, 16, -1) ]
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    with open(filename, 'wb') as wobj:
        wobj.write(data)     
def Work_Decrypt(rootDir,datakey): 
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        if True:   
            for f in files: 
                filename = os.path.join(root, f)
                print("Decrypt the file: " + filename)
                Decrypt(filename,datakey)
