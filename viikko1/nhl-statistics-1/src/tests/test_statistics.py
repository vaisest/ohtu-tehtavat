import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
        for player in PlayerReaderStub().get_players():
            result_player = self.statistics.search(player.name)
            self.assertEqual(player.team, result_player.team)
            self.assertEqual(player.goals, result_player.goals)
            self.assertEqual(player.assists, result_player.assists)

    def test_invalid_search(self):
        self.assertEqual(self.statistics.search("minijoni"), None)

    def test_team(self):
        player = self.statistics.team("PIT")[0]
        reference = Player("Lemieux", "PIT", 45, 54)
        self.assertEqual(player.name, reference.name)
        self.assertEqual(player.goals, reference.goals)
        self.assertEqual(player.team, reference.team)
        self.assertEqual(player.assists, reference.assists)

    def test_top_scorers(self):
        for player, name in zip(self.statistics.top_scorers(1), ["Gretzky", "Lemieux"]):
            self.assertEqual(player.name, name)
