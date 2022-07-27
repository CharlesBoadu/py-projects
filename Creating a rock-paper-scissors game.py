from random import choice

move = ['Rock', 'Paper', 'Scissors']
player_count = 0
computer_count = 0

for i in range(5):
    player = input("\nRock-Paper-Scissors. Choose one: ")
    for i in range(len(player)):
        player = player[0].upper() + player[1:]
    computer = choice(move)
    print("\nComputer chose:", computer)
    if player_count == 3 and computer_count == 0:
        print("Best out of 3, player wins!")
        break
    elif computer_count == 3 and player_count == 0:
        print("Best out of 3, computer wins!")
        break
    elif player == 'Scissors' and computer == 'Paper':
        player_count += 1
        print('\nScissor cuts paper. Player gains 1 point')
    elif computer == 'Scissors' and player == 'Paper':
        computer_count += 1
        print('\nScissor cuts paper. Computer gains 1 point')
    elif player == 'Rock' and computer == 'Scissors':
        player_count += 1
        print('\nRock crushes scissors. Player gains 1 point')
    elif computer == 'Rock' and player == 'Scissors':
        computer_count += 1
        print('\nRock crushes scissors. Computer gains 1 point')
    elif player == 'Paper' and computer == 'Rock':
        player_count += 1
        print('\nPaper covers rock. Player gains 1 point')
    elif computer == 'Paper' and player == 'Rock':
        computer_count += 1
        print('\nPaper covers rock. Computer gains 1 point')
    elif player == 'Scissors' and computer == 'Scissors':
        player_count += 0
        computer_count += 0
        print('\nBoth Player and Computer gains no point')
    elif player == 'Paper' and computer == 'Paper':
        player_count += 0
        computer_count += 0
        print('\nBoth Player and Computer gains no point')
    elif player == 'Rock' and computer == 'Rock':
        player_count += 0
        computer_count += 0
        print('\nBoth Player and Computer gains no point')
    

print('\n'+"Game Over! Player had:", player_count, " and Computer had:", computer_count)
if player_count > computer_count:
    print('\nPlayer wins!')
elif player_count == computer_count:
    print("\nThe game was a tie! Nobody wins!")
else:
    print("\nComputer wins!")
