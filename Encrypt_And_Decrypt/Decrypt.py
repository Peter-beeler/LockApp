#coding=utf-8
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os
import sys
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
    flag = 0;
    for root, dirs, files in list_dirs: 
        flag = 1;
        if(files == []):
            print("No Files In The Current Directory")
        # 切换加密和解密过程
        if(Flag == "decrypt"):   
            # 遍历文件，解密
            for f in files: 
                filename = os.path.join(root, f)
                print("Decrypt the file: " + filename)
                Decrypt(filename)
        else:
            print("Wrong parameters")
            return
    if(flag == 0):
        print("Current Directory Does Not Exist")
            
if __name__ == '__main__':
    #CreateRSAKeys()
    if(len(sys.argv) > 2): 
        d = sys.argv[2]
        Flag = sys.argv[1]
        if(Flag == 'decrypt'):
            Main(d, Flag)
        else: print("Wrong parameters")
    elif(len(sys.argv) == 2):
        print("Miss address or command:'decrypt'")
    else: print("Miss address and command:'decrypt'")