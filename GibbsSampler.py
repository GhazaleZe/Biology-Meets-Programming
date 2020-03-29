import random


def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]  # range over all elements symbol = Motifs[i][j] of the count matrix
            count[symbol][j] += 1  # add 1 to count[symbol][j].
    return count


def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    t += 4
    k = len(Motifs[0])
    profile = CountWithPseudocounts(Motifs)
    for symbol in "ACGT":
        for c in range(k):
            profile[symbol][c] /= t
    return profile


def Consensus(Motifs):
    consensus = ""
    count = CountWithPseudocounts(Motifs)
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
    count = CountWithPseudocounts(Motifs)
    consensus = Consensus(Motifs)
    score = 0
    i = 0
    r = len(Motifs)
    for char in consensus:
        p = count[char][i]
        x = r - p
        score += x
        i = i + 1
    return score


def RandomMotifs(Dna, k, t):
    col = len(Dna[0])
    s = []
    for i in range(t):
        new = random.randint(0, (col - k))
        s.append(Dna[i][new:new + k])
    return s


def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p


def ProfileMostProbableKmer(Text, k, Profile):
    n = len(Text)
    goal = Text[0:k]
    m = 0
    for i in range(n - k + 1):
        val = Pr(Text[i:i + k], Profile)
        if val > m:
            m = val
            goal = Text[i:i + k]
    return goal


def Motifs(Profile, Dna):
    k = len(Profile['A'])
    my_list = ProfileMostProbableKmer(Dna, k, Profile)
    return my_list


def GibbsSampler(Dna, k, t, N):
    motifs = RandomMotifs(Dna, k, t)
    BestMotifs = motifs
    temp = motifs
    for j in range(1, N):
        i = random.randint(1, (t - 1))
        motifs.pop(i)
        profile = ProfileWithPseudocounts(temp)
        motifs.insert(i, Motifs(profile, Dna[i]))
        if Score(motifs) < Score(BestMotifs):
            BestMotifs = motifs
    return BestMotifs


k = 8
t = 5
N = 100
dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
print(GibbsSampler(dna, k, t, N))
