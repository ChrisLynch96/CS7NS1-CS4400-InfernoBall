'''
Applies the  rules we've discovered for layer 2 to the english 4 words concatanation from
the previous practicle
'''

import re

with open("dualwords.ciaran.txt", "r") as wordlist:
    words = wordlist.read().splitlines()

#applying regular explression to slim down the wordlist
newList = []
for i in range(len(words)):
    matchObj = re.match(r'([A-Z]|[a-z]).{3}[A-Z].{3}', words[i])
    if matchObj:
        newList.append(matchObj.group())

#Writing to new wordlist
with open("wordlist.txt", "w+") as wordlist:
    for i in range(len(newList)):
        wordlist.write("%s\n" % newList[i])