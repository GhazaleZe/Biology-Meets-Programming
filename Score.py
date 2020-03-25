def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]  # range over all elements symbol = Motifs[i][j] of the count matrix
            count[symbol][j] += 1  # add 1 to count[symbol][j].
    return count


def Consensus(Motifs):
    consensus = ""
    count = Count(Motifs)
    k = len(Motifs[0])
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def Score(Motifs):
    count = Count(Motifs)
    consensus = Consensus(Motifs)
    score = 0
    i = 0
    r = len(Motifs)
    for char in consensus:
        p = count[char][i]
        x = r - p
        score += x
        i = i+1
    return score


a = []
a = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
print(Score(a))
