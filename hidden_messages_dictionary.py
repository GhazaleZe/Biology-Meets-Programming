def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words


def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] += 1
    return freq


print(FrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))
