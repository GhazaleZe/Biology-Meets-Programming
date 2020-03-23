def SkewArray(Genome):
    Skew = [0]
    for i in range(1, len(Genome) + 1):
        j = i - 1
        if Genome[j] == 'A' or Genome[j] == 'T':
            Skew.append(Skew[i - 1])
        elif Genome[j] == 'G':
            Skew.append(Skew[i - 1] + 1)
        else:
            Skew.append(Skew[i - 1] - 1)
    return Skew


print(SkewArray("CATGGGCATCGGCCATACGCC"))
