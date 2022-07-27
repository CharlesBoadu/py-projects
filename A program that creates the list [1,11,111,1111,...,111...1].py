one_list = []
j = 0
k = 0
for i in range(1, 100):
    one_list.append(1 + j)
    k += 1
    j += 10**k
    
print(one_list)
