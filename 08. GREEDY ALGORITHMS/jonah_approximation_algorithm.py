def select_players(players, abilities, team_size):
    selected_team = []
    uncovered_abilities = set(abilities)
    
    while len(selected_team) < team_size and uncovered_abilities:
        best_player = max(players, key=lambda p: len(p['abilities'].intersection(uncovered_abilities)))
        selected_team.append(best_player)
        uncovered_abilities -= best_player['abilities']
    
    return selected_team

# Example usage:
players = [
    {'name': 'Player1', 'abilities': {'good quarterback', 'good under pressure'}},
    {'name': 'Player2', 'abilities': {'good running back', 'good in rain'}},
    {'name': 'Player3', 'abilities': {'good wide receiver', 'good under pressure'}},
    # Add more players as needed
]

abilities = {'good quarterback', 'good running back', 'good in rain', 'good under pressure', 'good wide receiver'}

team_size = 2

selected_team = select_players(players, abilities, team_size)

print("Selected Team:")
for player in selected_team:
    print(player['name'])
