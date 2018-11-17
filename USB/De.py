import sys
sys.path.append("../Encrypt_And_Decrypt")
from Encrypt import Encrypt
from Decrypt import Decrypt
Decrypt("/media/foenix/Ubuntu 18.01/code/code.txt",open("../Encrypt_And_Decrypt/my_private_rsa_key.bin").read())
