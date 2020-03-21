def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    n=len(Genome)
    k=len(Pattern)
    for i in range(n - k + 1):
        if Pattern == Genome[i:i + k] :
            positions.append(i)
    return positions
print(PatternMatching("ATAT","GATATATGCATATACTT"))