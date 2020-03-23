def HammingDistance(p, q):
    count = 0
    n = len(p)
    for i in range(n):
        if p[i] != q[i]:
            count = count + 1
    return count


def ApproximatePatternMatching(Text, Pattern, d):
    positions = []  # initializing list of positions
    n = len(Text)
    k = len(Pattern)
    for i in range(n - k + 1):
        if (HammingDistance(Pattern, Text[i:i + k]) <= d):
            positions.append(i)
    return positions


print(
    ApproximatePatternMatching("CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT", "ATTCTGGA", 3))
