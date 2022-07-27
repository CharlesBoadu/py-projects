print("What comes down and never goes up?")
print("What am I?")
print("NB: You only have 3 tries")

answer = "Rain"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != answer and not(out_of_guesses):
    if guess_count<guess_limit:
        guess = input("What is the answer: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, Better luck next time!")
else:
    print("Congratulations, You did it!")
