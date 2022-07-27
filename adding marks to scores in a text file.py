class_scores_file = [line.strip() for line in open('class_scores.txt')]
class_scores_file_one = [line.split() for line in class_scores_file]

result_list = []
scores2 = open('scores2.txt', 'w')
for i in range(len(class_scores_file_one)):
    for j in range(1, 2):
        result = int(class_scores_file_one[i][j]) + 5
        result_list.append(result)
c = 0
for m in range(len(class_scores_file_one)):
    for n in range(0, 1):
        z = result_list[0+c]
        print(class_scores_file_one[m][n], z, file=scores2)
        c += 1
scores2.close()




