import json

with open('InfernoBallLayer8.json', 'r') as infernoBall:
    data = json.load(infernoBall)

hashes = data["hashes"]
for i in range(len(hashes)):
    hashes[i] = str(hashes[i])

with open('justHash.hashes', 'w+') as outfile:
   for i in range(len(hashes)):
       outfile.write("%s\n" % hashes[i])