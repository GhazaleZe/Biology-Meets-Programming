def Reverse(Pattern):
    new= Pattern[::-1]
    return new
def Complement(Pattern):
    new = ""
    for c in Pattern:
        if c == 'A':
            new += 'T'
        elif c == 'T':
            new += 'A'
        elif c == 'G':
            new += 'C'
        elif c == 'C':
            new += 'G'
    return new
print(Reverse("AAAACCCGGT"))
print(Complement("AAAACCCGGT"))