from random import choice

players_money = 100
flip = ["Heads", "Tails"]

while players_money != 0 and players_money != 50:
    players_guess = input("Heads or Tails: ")
    for i in range(len(players_guess)):
        players_guess = players_guess[0].upper() + players_guess[1:]
    random_flip = choice(flip)
    if players_guess == random_flip:
        print("Correct! It was a", random_flip)
        players_money += 10
        print("Money Left:", players_money)
    else:
        print("Oops! It was a", random_flip)
        players_money -= 10
        print("Money Left:", players_money)

    
if players_money == 0:
    print("Game Over! You ran out of money!")
elif players_money == 200:
    print("Game Over! You reached $200")
