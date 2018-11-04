
with open("rockyou.txt", "r") as wordlist:
    words = wordlist.read().splitlines()

shortened = []
for i in range(len(words)):
    if len(words[i]) < 8:
        shortened.append(words[i])

with open("wordlist.txt", "w+") as newWordlist:
    for i in range(len(shortened)):
        newWordlist.write("%s\n" % shortened[i])

