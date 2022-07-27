from random import randint
secret_num = randint(1,100)
num_guesses = 0
guess = 0
while guess != secret_num and num_guesses <= 4:
    guess = eval(input('Enter your guess (1-100): '))
    if guess < secret_num and num_guesses == 0:
        print("HIGHER. 4 guesses left.\n")
        num_guesses = num_guesses + 1
    elif guess > secret_num and num_guesses == 0:
        print("LOWER. 4 guesses left.\n")
        num_guesses = num_guesses + 1
    elif guess < secret_num and num_guesses == 1:
        print("HIGHER. 3 guesses left.\n")
        num_guesses = num_guesses + 1
    elif guess > secret_num and num_guesses == 1:
        print("LOWER. 3 guesses left.\n")
        num_guesses = num_guesses + 1
    elif guess < secret_num and num_guesses == 2:
        print("HIGHER. 2 guesses left.\n")
        num_guesses = num_guesses + 1
    elif guess > secret_num and num_guesses == 2:
        print("LOWER. 2 guesses left.\n")
        num_guesses = num_guesses + 1
    elif guess < secret_num and num_guesses == 3:
        print("HIGHER. 1 guess left.\n")
        num_guesses = num_guesses + 1
    elif guess > secret_num and num_guesses == 3:
        print("LOWER. 1 guess left.\n")
        num_guesses = num_guesses + 1
    elif guess < secret_num and num_guesses == 4:
        print("HIGHER. you are out of guesses.\n")
        num_guesses = num_guesses + 1
    elif guess > secret_num and num_guesses == 4:
        print("LOWER. you are out of guesses.\n")
        num_guesses = num_guesses + 1
    else:
        print('You got it!')
if num_guesses==5 and guess != secret_num:
    print('You lose. The correct number is', secret_num)
