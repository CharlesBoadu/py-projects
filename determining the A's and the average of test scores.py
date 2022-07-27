test_scores_list = []

for i in range(10):
    test_scores = int(input("Enter the test scores: "))
    if test_scores < 0:
        break
    test_scores_list.append(test_scores)
count = 0
score = 0
for score in test_scores_list:
    if score >= 90:
        count += 1

print(str(count) + " of the scores are A's.")

average_of_test_scores = sum(test_scores_list) / len(test_scores_list)
print(str(average_of_test_scores)+ " is the average of the test scores.")
    
