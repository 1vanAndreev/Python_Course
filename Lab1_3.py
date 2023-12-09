def split_players_into_teams(players):
  number_of_players = len(players)
  number_of_players_per_team = number_of_players // 2
  team_1 = players[:number_of_players_per_team]
  team_2 = players[number_of_players_per_team:]
  return team_1, team_2

players = ["Иван", "Петр", "Сергей", "Евгений", "Дмитрий", "Александр"]
team_1, team_2 = split_players_into_teams(players)
print("Команда 1:", team_1)
print("Команда 2:", team_2)
