import random


def RandomMotifs(Dna, k, t):
    col = len(Dna[0])
    s = []
    for i in range(t):
        new = random.randint(0, (col - k))
        s.append(Dna[i][new:new + k])
    return s


dna = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]
print(RandomMotifs(dna, 3, 5))
