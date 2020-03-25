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


def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = Count(Motifs)
    for symbol in "ACGT":
        for c in range(k):
            profile[symbol][c] /= t
    return profile


a = []
a = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
print(Profile(a))
