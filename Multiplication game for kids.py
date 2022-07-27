from random import randint

count = 0
for i in range(1, 11):
    x = randint(1, 12)
    y = randint(1, 12)
    z = x * y
    answer = eval(input(f"Question {i}: {x} x {y} = "))
    if answer == z:
        print("Right!")
        count += 1
    else:
        print(f"Wrong. The answer is {z}") 
    
print("\nYou got", count, "correct!")
