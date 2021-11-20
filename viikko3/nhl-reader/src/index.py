from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    filtered_players = stats.top_scorers_by_nationality("FIN")

    for player in filtered_players:
        print(player)

if __name__ == "__main__":
    main()
