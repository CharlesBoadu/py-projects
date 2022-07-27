num_list = []
for i in range(2):
    num = eval(input("Enter a number: "))
    num_list.append(num)

num_list_1 = []
for i in range(1, num_list[0]):
    if num_list[0] % i == 0:
        num_list_1.append(i)

num_list_2 = []
for i in range(1, num_list[1]):
    if num_list[1] % i == 0:
        num_list_2.append(i)

common = []
for i in range(len(num_list_2)):
    for j in range(len(num_list_1)):
        if num_list_2[i] == num_list_1[j]:
            common.append(num_list_2[i])
gcd = 0
for i in range(len(common)):
    gcd = common[i]
    
print("The greatest common divisor of the two numbers is", gcd)
