#coding=utf-8
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os
import sys
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
def Encrypt(filename):         
    data = ''
    with open(filename, 'rb') as f:
        data = f.read()
    with open(filename, 'wb') as out_file:
        # 收件人秘钥 - 公钥
        recipient_key = RSA.import_key(open('my_public_rsa_key.pem').read())
        session_key = get_random_bytes(16)
        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))
        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        out_file.write(cipher_aes.nonce)
        out_file.write(tag)
        out_file.write(ciphertext)
        
def Decrypt(filename):
    code = 'nooneknows'
    with open(filename, 'rb') as fobj:
        private_key = RSA.import_key(open('my_private_rsa_key.bin').read(), passphrase=code)
        enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                    for x in (private_key.size_in_bytes(), 
                                                    16, 16, -1) ]
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    with open(filename, 'wb') as wobj:
        wobj.write(data)     
def Main(rootDir, Flag): 
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        # 切换加密和解密过程
        #if False: 
        if Flag == "Encrypt":
            # 遍历文件，加密
            for f in files: 
                filename = os.path.join(root, f)
                print("Encrypt the file: " + filename)
                Encrypt(filename)
        elif Flag == "Decrypt":   
            # 遍历文件，解密
            for f in files: 
                filename = os.path.join(root, f)
                print("Decrypt the file: " + filename)
                Decrypt(filename)
        else:
            print("Wrong parameters")
            return
            
if __name__ == '__main__':
    #CreateRSAKeys()
    d = '/home/foenix/test'
    if(len(sys.argv) > 1): 
        Main(d, sys.argv[1])
    else: print("Miss parameters")