

with open("reducedCrackstation.txt", "r+") as wordlist:
    words = wordlist.read().splitlines()

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

splits = chunkIt(words, 4)

#writing to files
for i in range(len(splits)):
    with open("wordlist%d.txt" % i, "w+") as outlfile:
        for j in range(len(splits[i])):
            outlfile.write("%s\n" % splits[i][j])
