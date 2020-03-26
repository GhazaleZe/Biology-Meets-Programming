
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

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
