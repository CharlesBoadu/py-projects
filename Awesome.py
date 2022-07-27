from random import randint

alphabets = 'åabcdefghijklmnopqrstuvwxyz'
m = list(alphabets)

x = [randint(0, 49) for i in range(20)]
y = [i*i for i in range(1, 50)]
z = []
for i in range(1, 27):
    z.append(i* m[i])
 
print(x)
print(y)
print(z)
