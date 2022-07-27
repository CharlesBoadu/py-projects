grades_file = [line.strip() for line in open('grades3.txt')]
grades_file_one = [line.split() for line in grades_file]

i = 0
count = 0
total_count = 0
while i < len(grades_file_one):
    for score in grades_file_one[i][1:]:
        if int(score) > 50:
            count += 1
            if count == 3:
                total_count += 1
            i += 1
        else:
            break
    i += 1

print(count, "people passed!")
