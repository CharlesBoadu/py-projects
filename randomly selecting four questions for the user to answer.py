from project import rand_questions
from random import choice, shuffle

questions = ["1. Which of the following contains requests, recommendations, responses, invitations, offers, and complaints?\na. business letter\n b.cover letter\nc. wizard\nd. resume letter\nType in the correct answer: ",
             "2. A ____ is the section of a letter that identifies an organization or individual. \na. template\nb. cover letter\nc. letter head\nd. resume\nType in the correct answer: ",
             "3. Word prióvides a(n) _____ button, which increases the font size of selected text each time you click the button \na. Grow font\nb. Percent\nc. Increase\nd. Maximize\nType in the correct answer: ",
             "4. The ___ box arrow on the Home tab allows you to change the font size or text \na. Font size\nb. Format\nc. Character\nd. Review\nType in the correct answer: ",
             "5. A ____ is preprinted on stationery that everyone in a company uses for correspondence\na. template\nb. letter head\nc. resume\nd. cover letter\nType in the correct answer: ",
             "6. A(n) ___ is a graphic that you create using word. \na. graphic shape\nb. drawing object\nc. display\nd. art drawing\nType in the correct answer: ",
             "7. A collection of rows and columns is a _____ \na. cell\nb. box\nc. chart\nd. table\nType in the correct answer: ",
             "8. The intersection of a row and a column is a ____ \na. cell\nb. handle\nc. table\nd. gridline\nType in the correct answer: ",
             "9. Each cell in a table has a(n) ____ which is a foramtting mark that assists you with selecting and formatting cells. \na. Property Key\nb. end-of-cell mark\nc. Grid\nd. intersection reference\nType in the correct answer: ",
             "10. You can resize an entire table by dragging the table resize handle, which is a small ____ that appears when you point to the corner of the table. \na. square\nb. cell border\nc. asterisk\nd. gridline\nType in the correct answer: ",
]

random_questions_list = []
for i in range(4):
    random_question = choice(questions)
    random_questions_list.append(random_question)

rand_questions = [rand_questions(random_questions_list[0]),
                  rand_questions(random_questions_list[1]),
                  rand_questions(random_questions_list[2]),
                  rand_questions(random_questions_list[3])
]
def run_test1(rand_questions):
    score = 0
    for question in rand_questions:
        answer = input(question.prompt)
        if random_questions_list[0][:1] == '1' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[0][:1] == '2' and answer == "c":
            score += 1
            print("Correct, the answer is c\n")
        elif random_questions_list[0][:1] == '3' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[0][:1] == '4' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[0][:1] == '5' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[0][:1] == '6' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[0][:1] == '7' and answer == "d":
            score += 1
            print("Correct, the answer is d\n")
        elif random_questions_list[0][:1] == '8' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[0][:1] == '9' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[0][:2] == '10' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[1][:1] == '1' and answer == "a":
            score += 1
            print("Correct, the answer is c\n")
        elif random_questions_list[1][:1] == '2' and answer == "c":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[1][:1] == '3' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[1][:1] == '4' and answer == "a":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[1][:1] == '5' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[1][:1] == '6' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[1][:1] == '7' and answer == "d":
            score += 1
            print("Correct, the answer is d\n")
        elif random_questions_list[1][:1] == '8' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[1][:1] == '9' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[1][:2] == '10' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[2][:1] == '1' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[2][:1] == '2' and answer == "c":
            score += 1
            print("Correct, the answer is c\n")
        elif random_questions_list[2][:1] == '3' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[2][:1] == '4' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[2][:1] == '5' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[2][:1] == '6' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[2][:1] == '7' and answer == "d":
            score += 1
            print("Correct, the answer is d\n")
        elif random_questions_list[2][:1] == '8' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[2][:1] == '9' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[2][:2] == '10' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[3][:1] == '1' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[3][:1] == '2' and answer == "c":
            score += 1
            print("Correct, the answer is c\n")
        elif random_questions_list[3][:1] == '3' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[3][:1] == '4' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[3][:1] == '5' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[3][:1] == '6' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[3][:1] == '7' and answer == "d":
            score += 1
            print("Correct, the answer is d\n")
        elif random_questions_list[3][:1] == '8' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        elif random_questions_list[3][:1] == '9' and answer == "b":
            score += 1
            print("Correct, the answer is b\n")
        elif random_questions_list[3][:2] == '10' and answer == "a":
            score += 1
            print("Correct, the answer is a\n")
        else:
            print("Wrong!\n")

    print("\nYour score is", score, "out of 4")
run_test1(rand_questions)
