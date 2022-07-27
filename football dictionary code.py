team_dictionary = {}
for i in range(5):
    team_name = input("Enter a team name: ")
    games_won = eval(input("Enter the number of games won: "))
    games_lost = eval(input("Enter the number of games lost: "))
    team_dictionary[team_name] = [games_won, games_lost]

print(team_dictionary)
user_team = input("Enter a team's name: ")
team_winning_percentage = team_dictionary[user_team][0] / 5 * 100
print(f"The winning percentage of {user_team} is", team_winning_percentage)

winnings_entry = []
for team in team_dictionary:
    winnings_entry.append(team_dictionary[team][0])

print("A list with the number of wins in each teams", winnings_entry)

winnings_records_team_list =  []
for team in team_dictionary:
    if team_dictionary[team][0] >= 1:
        winnings_records_team_list.append(team)

print("The list of teams with winning records are", winnings_records_team_list)
