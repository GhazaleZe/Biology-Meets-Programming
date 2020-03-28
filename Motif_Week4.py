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
    n = len(Dna)
    my_list = []
    for i in range(n):
        new = ProfileMostProbableKmer(Dna[i], k, Profile)
        my_list.append(new)
    return my_list


profilr = {"A": [0.8, 0.0, 0.0, 0.2], "C": [0.0, 0.6, 0.2, 0.0], "G": [0.2, 0.2, 0.8, 0.0], "T": [0.0, 0.2, 0.0, 0.8]}
dna = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]
print(Motifs(profilr, dna))
