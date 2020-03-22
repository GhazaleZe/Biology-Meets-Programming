def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array
def PatternCount(Pattern,Text):
    n = len(Text)
    k = len(Pattern)
    num = 0
    for i in range(n - k + 1):
        if Text[i:i + k] == Pattern:
            num = num + 1
    return num
print(SymbolArray("AAAAGGGG","A"))

