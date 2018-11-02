'''
TODO to make this bad boy work
1) Get passwords --> Bash script to format and save to pot file
2) With those passwords get their corresponding shares.
3) Get enough shares to get the secret
4) Use the secret to decrypt the cipher and get the next layer
5) Rinse and repeat
'''
import as5-makeinferno as as5
import Crypto
import secretsharing as sss
from Crypto.Cipher import AES

# getting passwords
passFile = open("allPasswords.pot", "w")
print passFile