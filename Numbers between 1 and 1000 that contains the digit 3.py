x = [i for i in range(1, 1001)]

num_list = []
for i in range(len(x)):
    if '3' in str(x[i]):
        num_list.append(x[i])

print("Numbers between 1 and 1000 that contains the digit 3 are", len(num_list))
