from Question import questions

question_prompts = [
        "1. A(n) is any hardware component that allows you to enter data and instructions into a computer or mobile device.\na. Output Device\nb. Communication Device\nc. Input Device\nd. Display\nChoose one: ",
        "\n2. Which of the following is not an example of an Output device?\na. Scanner\nb. Printer\nc. Display\nd. Speaker\nChoose one: ",
        "\n3._______ consists of electronic components that store instructions waiting to be executed and the data needed by those instructions.\na. Storage\nb. Cloud storage\nc. Solid-state Drives\nd. Memory\nChoose one: "
    ]


questions = [
    questions(question_prompts[0], "c"),
    questions(question_prompts[1], "a"),
    questions(question_prompts[2], "d"),
    ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    if score >= 2:
        print("Well done!""\nYou got" +str(score)+ "/" +str(len(questions))+ "correct")
    else:
        print("You can do better!""\nYou got" +str(score)+ "/" +str(len(questions))+ "correct")
    

run_test(questions)
