#importing random and time module
from random import choice
import time

#function to initiate rock-paper-scissors game
def rock_paper_scissors(player_score, comp_score, plays):
    play_choic = input("Rock-paper-scissors: ")
    comp_choose = choice(comp_choices)
    if play_choic.lower() == 'rock' and comp_choose == 'scissors':
        print("Computer chose", comp_choose)
        print("Rock crushes Scissor. Player gains 1 point.\n")
        player_score += 1
        plays += 1
    elif play_choic.lower() == 'scissors' and comp_choose == 'rock':
        print("Computer chose", comp_choose)
        print("Rock crushes Scissor. Computer gains 1 point. \n")
        comp_score += 1
        plays += 1
    elif play_choic.lower() == 'scissors' and comp_choose == 'paper':
        print("Computer chose", comp_choose)
        print("Scissors cuts Paper. Player gains 1 point. \n")
        player_score += 1
        plays += 1
    elif play_choic.lower() == 'paper' and comp_choose == 'scissors':
        print("Computer chose", comp_choose)
        print("Scissors cuts Paper. Computer gains 1 point. \n")
        comp_score += 1
        plays += 1
    elif play_choic.lower() == 'paper' and comp_choose == 'rock':
        print("Computer chose", comp_choose)
        print("Paper covers paper. Player gains 1 point. \n")
        player_score += 1
        plays += 1
    elif play_choic.lower() == 'rock' and comp_choose == 'paper':
        print("Computer chose", comp_choose)
        print("Paper covers rock. Computer gains 1 point. \n")
        comp_score += 1
        plays += 1
    elif play_choic.lower() == comp_choose:
        print("Both Player and computer chose " +play_choic.lower()+ ". No points awarded. \n")
    else:
        print("Invalid input! Choose again. \n")
    return [plays, comp_score, player_score]


#Function to decide if player wants to play again or not
def decision(wins, losses, games_played):
    player_dec = ''
    while player_dec != 'yes' or player_dec != 'no':
        player_dec = input("Play again? Type 'yes' to play again and 'no' to end game: ")
        if player_dec.lower() == 'yes':
            player_score = 0
            comp_score = 0
            plays = 0
            end_game = False
            break
        elif player_dec.lower() == 'no':
            player_score = 0
            comp_score = 0 
            plays = 5
            end_game = True
            print('\n')
            print("statistics of the game: \n")
            print("Total games played:", games_played)
            print("Wins:", wins)
            print("Losses:", losses)
            print('\n')

            print("Thanks for playing Rock-Paper-Scissors game! Bye!")
            break
        print("invalid input! Please enter 'yes' or 'no'")
    return [player_score, comp_score, plays, end_game]



name = input("What is your name: ")
print("Hello " +name+ ", Welcome to Rock-Paper-Scissors\nGame starts in 5 seconds\n")
time.sleep(5)

plays = 0
player_score = 0
comp_score = 0
comp_choices = ['scissors', 'paper', 'rock']
end_game = False
games_played = 0
wins = 0
losses = 0

#Loop to ensure game lasts for five rounds where highest points wins
while plays < 5 and end_game == False:
    if plays == 4:
        plays, comp_score, player_score = rock_paper_scissors(player_score, comp_score, plays)
        if plays == 4:
            continue
        else:
            if player_score > comp_score:
                wins += 1
                games_played += 1
                player_score, comp_score, plays, end_game = decision(wins, losses, games_played)
            else:
                losses += 1
                games_played += 1
                player_score, comp_score, plays, end_game = decision(wins, losses, games_played)
    else:
        plays, comp_score, player_score = rock_paper_scissors(player_score, comp_score, plays)
        
        

    
        
