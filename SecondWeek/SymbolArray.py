def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n // 2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n // 2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i - 1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i - 1] == symbol:
            array[i] = array[i] - 1
        if ExtendedGenome[i + (n // 2) - 1] == symbol:
            array[i] = array[i] + 1
    return array


def PatternCount(Pattern, Text):
    n = len(Text)
    k = len(Pattern)
    num = 0
    for i in range(n - k + 1):
        if Text[i:i + k] == Pattern:
            num = num + 1
    return num


print(FasterSymbolArray("AAAAGGGG", "A"))
import sys
lines = sys.stdin.read().splitlines()
print(FasterSymbolArray(lines[0], lines[1]))


