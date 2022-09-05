from random import randint

questions = [line.split('.') for line in open('questions.txt')]
answers = [line.strip() for line in open('answer.txt')]

total_score = 0
duplicates = []

for i in range(len(questions)):
    num = randint(0, 3)
    while num in duplicates:
        num = randint(0, 2)
    else:
        duplicates.append(num)

        
    print(questions[num][1].strip())
    solution = input("What is the answer: ")
    if solution.lower() == answers[num].lower():
        print("Correct! \n")
        total_score += 1
    else:
        print("incorrect! \n")

if total_score >= 2:
    print("Congratulations, You scored", total_score, "out of 4")
else:
    print("You scored", total_score, "out of 3. You can do better!")

        

