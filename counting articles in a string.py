from string import punctuation

text = input("Enter some text: ")

for c in punctuation:
    text = text.replace(c, '')

text = text.lower()
L = text.split()
count = L.count(L)
count_1 = 0
count_2 = 0
count_3 = 0
for word in L:
    if word == "a":
        count_1 += 1
    elif word == "an":
        count_2 += 1
    elif word == "the":
        count_3 += 1
        
if count_1 == 1:
    print("The article, 'a' appears once.")
else:
    print("The article, 'a' appears " +str(count_1)+ " times.")
if count_2 == 1:
    print("The article, 'an' appears once.")
else:
    print("The article, 'an' appears " +str(count_2)+ " times.")
if count_3 == 1:
    print("The article, 'the' appears once.")
else:
    print("The article, 'the' appears " +str(count_3)+ " times.")

