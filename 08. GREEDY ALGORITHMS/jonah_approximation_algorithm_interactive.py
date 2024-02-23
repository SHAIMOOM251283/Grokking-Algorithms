def select_players(players, abilities, team_size):
    selected_team = []
    uncovered_abilities = set(abilities)
    
    while len(selected_team) < team_size and uncovered_abilities:
        best_player = max(players, key=lambda p: len(p['abilities'].intersection(uncovered_abilities)))
        selected_team.append(best_player)
        uncovered_abilities -= best_player['abilities']
    
    return selected_team

def main():
    players = []
    abilities = set()
    
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        player_name = input(f"Enter name for Player {i+1}: ")
        player_abilities = set(input(f"Enter abilities for Player {i+1} (comma-separated): ").split(','))
        players.append({'name': player_name, 'abilities': player_abilities})
        abilities.update(player_abilities)
    
    team_size = int(input("Enter team size: "))
    
    print("\nEnter the desired abilities (comma-separated): ")
    abilities = set(input().split(','))
    
    selected_team = select_players(players, abilities, team_size)
    
    print("\nSelected Team:")
    for player in selected_team:
        print(player['name'])

if __name__ == "__main__":
    main()
