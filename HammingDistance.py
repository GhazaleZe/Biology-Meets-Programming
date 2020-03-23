def HammingDistance(p, q):
    count = 0
    n = len(p)
    for i in range(n):
        if p[i] != q[i]:
            count = count + 1
    return count


print(HammingDistance("GGGCCGTTGGT", "GGACCGTTGAC"))
