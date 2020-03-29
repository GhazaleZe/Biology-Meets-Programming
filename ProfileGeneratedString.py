import random


def Normalize(Probabilities):
    sum = 0
    for key in Probabilities:
        sum += Probabilities[key]
    for key in Probabilities:
        Probabilities[key] /= sum
    return Probabilities


def WeightedDie(Probabilities):
    kmer = ''  # output variable
    num = random.uniform(0, 1)
    for i in Probabilities:
        num -= Probabilities[i]
        kmer = i
        if num <= 0:
            return kmer


def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p


def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0, n - k + 1):
        probabilities[Text[i:i + k]] = Pr(Text[i:i + k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)


print(ProfileGeneratedString("AAACCCAAACCC", {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}, 2))
