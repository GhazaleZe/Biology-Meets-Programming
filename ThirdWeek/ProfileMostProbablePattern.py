def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p


def ProfileMostProbableKmer(Text, k, Profile):
    n = len(Text)
    goal = Text[0:k]
    m = 0
    for i in range(n - k + 1):
        val = Pr(Text[i:i + k], Profile)
        if val > m:
            m = val
            goal = Text[i:i + k]
    return goal


t = "AACCGGTT"
p = {"A": [1.0, 1.0, 1.0], "C": [0.0, 0.0, 0.0], "G": [0.0, 0.0, 0.0], "T": [0.0, 0.0, 0.0]}

print(ProfileMostProbableKmer(t, 3, p))
