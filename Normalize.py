def Normalize(Probabilities):
    sum = 0
    for key in Probabilities:
        sum += Probabilities[key]
    for key in Probabilities:
        Probabilities[key] /= sum
    return Probabilities


print(Normalize({'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}))
