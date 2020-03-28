import random




def WeightedDie(Probabilities):
    kmer = ''  # output variable
    num = random.uniform(0, 1)
    for i in Probabilities:
        num -= Probabilities[i]
        kmer = i
        if num <= 0:
            return kmer


