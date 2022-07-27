def is_sorted(a, b, c, d, e):
    L = [a, b, c, d, e]
    M = sorted(L)
    for i in range(5):
        if M[i] == L[i] and i == 4:
            print("True")
        elif M[i] != L[i]:
            print("False")
            break
        

is_sorted(1, 2, 4, 3, 5)
