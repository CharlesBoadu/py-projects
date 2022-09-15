#importing the random and time module
from random import randint
import time

#a function for player to decide whether to play again or end game
def decision():
        player_dec = ''
        while player_dec != 'yes' or player_dec != 'no':
                player_dec = input("Play again? Type 'yes' to play again and 'no' to end game: ")
                if player_dec.lower() == 'yes':
                    guesses = 0
                    end_game = False
                    no_of_guesses = 3
                    break
                elif player_dec.lower() == 'no':
                    guesses = 3
                    end_game = True
                    no_of_guesses = 0
                    print('\n')
                    print("statistics of the game: \n")
                    print("Total games played:", games_played)
                    print("Wins:", wins)
                    print("Losses:", losses)
                    print('\n')

                    print("Thanks for playing Guess Random number! Bye!")
                    break
                print("invalid input! Please enter 'yes' or 'no'")
        return [guesses, end_game, no_of_guesses]
    
guesses = 0
no_of_guesses = 3
guess_num = randint(1, 10)
end_game = False
games_played = 0
wins = 0
losses = 0

name = input("Hello Player! What is your name: ")
for element in name:
        name = name[0].upper() + name[1:]

#Deciding if player is ready to start the game
ready = ''
while ready != 'yes' or ready != 'no':
    print("Type 'yes' if you are ready and 'no' if you are not.")    
    ready = input("Are you ready, "+name+": ")
    if ready.lower() == 'yes':
        break
    elif ready.lower() == 'no':
        print("You have another 5 seconds to decide")
        time.sleep(5)
    elif ready != 'yes' or ready != 'no':
        print("invalid input! Please enter 'yes' or 'no'")
        

print('\n')
print("Welcome to the Guessing Game! \nYou only have to guess secret number. \nGame starts in 3 seconds")       
time.sleep(3)

#Loop to allow player to play game with three tries
while guesses < 3 and end_game == False:
    try:
        guess = eval(input("What is the number: "))
        if guess == guess_num:
            print("Correct! The Guess number was", guess_num)
            print("Congrats! You have won the game!")
            wins += 1
            games_played += 1
            print('\n')
            guesses, end_game, no_of_guesses = decision()
            guess_num = randint(1, 10)
        else:
            if guesses == 2 and guess != guess_num:
                print("incorrect! No more guesses left, You lose! The Guess number was", guess_num)
                losses += 1
                games_played += 1
                print('\n')
                guesses, end_game, no_of_guesses = decision()
                guess_num = randint(1, 10)
            else:
                no_of_guesses = no_of_guesses - 1
                print(f"Incorrect, {no_of_guesses} guess left! Guess again!")
                guesses += 1
    except (NameError, SyntaxError):
        print("Invalid input! Please enter a number")
        print('\n')






    
