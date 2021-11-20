class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = sorted(
            (plr for plr in self.players if plr.nationality == nationality),
            key = lambda plr: plr.goals + plr.assists,
            reverse=True)
        return filtered_players
