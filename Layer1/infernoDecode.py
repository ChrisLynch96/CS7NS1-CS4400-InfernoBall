import as5_makeinferno as as5
import Crypto
import json
import secretsharing as sss
from Crypto.Cipher import AES
import base64
import hashlib

#decryption function for the cipher text so we can get the next level
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
def decrypt(enc, secret):
    #private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(secret, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

#Reading in the cipher, hashes, and shares from the JSON file
with open('./InfernoBallLayer1.as5', 'r') as infernoBall:
    data = json.load(infernoBall)

hashes = data["hashes"]
shares = data["shares"]
cipher = data["ciphertext"]#.encode("utf-8")
for i in range(len(hashes)):
    hashes[i] = str(hashes[i])
    shares[i] = str(shares[i])

'''
for i in range(len(data["hashes"])):
    hashes[i] = hashes[i].encode("utf-8")
    shares[i] = shares[i].encode("utf-8")
'''

# getting recovered passwords
passFile = open('./Broken_Hashes/allPasswords.pot', 'r')
passwords = passFile.read().splitlines()
passFile.close()

#Getting original hashes of cracked passwords and the passwords themselves
justHash = []
justPass = []
for i in range(len(passwords)):
    (shash, spass) = passwords[i].split(":")
    justHash.append(shash)
    justPass.append(spass)

#Getting the indices of the hashes
hashIndices = []
for i in range(len(justHash)):
    for j in range(len(hashes)):
        if justHash[i] == hashes[j]:
            hashIndices.append(j)
            break

#Time to get a secret and see if it works
secret = as5.pwds_shares_to_secret(justPass, hashIndices, shares)

print secret

nextLevel = bytes.decode(decrypt(cipher, secret))
print nextLevel

'''
f = open('infernoBallLayer2.as5', 'w+')
f.write(nextLevel)
f.close
'''
#print nextLevel
'''
with open('InfernoBallLayer2.as5', 'w+') as outfile:
    json.dump(nextLevel, outfile)
'''