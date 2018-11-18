import os,time
import sys
sys.path.append('../Encrypt_And_Decrypt')
from Decrypt import Work_Decrypt

if __name__ == "__main__":
    filepath = '/home/foenix/test'
    codepath = '/media/foenix/tmp'
    x = codepath + "/code/my_private_rsa_key.bin"
    datakey =open(x).read()
    Work_Decrypt(filepath,datakey)
	
