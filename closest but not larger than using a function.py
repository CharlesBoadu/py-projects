def closest(a,b,c,d,e, n=1):
    L = [a,b,c,d,e]
    M = []
    O = []
    for i in range(len(L)):
        if L[i] < n:
            M.append(L[i])

    O = sorted(M)
    for i in range(len(O)):
        answer = O[i]

    print("from the list", str(L)+',', answer, "is the closest to", n, "and not larger than it")

closest(1,6,3,9,11, 6)
