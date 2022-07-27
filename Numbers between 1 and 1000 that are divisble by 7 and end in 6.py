num_list = []
for i in range(1, 1001):
    if i % 7 == 0:
        num_list.append(i)

num_list_1 = []
for j in range(len(num_list)):
    x = list(str(num_list[j]))
    if len(x) == 2 and x[1] == '6':
        num_list_1.append(x)
    elif len(x) == 3 and x[2] == '6':
        num_list_1.append(x)
print("Numbers between 1 and 1000 that are divisble by 7 and end in 6 are:")
for k in range(len(num_list_1)):
    z = ''.join(num_list_1[k])
    print(z)
