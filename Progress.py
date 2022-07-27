scores = 0
scores_list = []

while scores != -1:
    scores = eval(input("Enter the scores: "))
    scores_list.append(scores)

count = 0
for i in range(len(scores_list)):
    if scores_list[i] > 90:
        count += 1

print(count, "of the scores are A's")
s = sum(scores_list)
m = s + 1
n = m/len(scores_list)
print('{:.2f}'.format(n), "is the average")
