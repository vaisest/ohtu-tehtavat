class TennisGame:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.first_score = 0
        self.second_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.first_score += 1
        else:
            self.second_score += 1

    def get_score_word(self, n):
        SCORES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return SCORES[n]

    def get_draw_score(self):
        if self.first_score > 3:
            return "Deuce"
        first_score_word = self.get_score_word(self.first_score)
        return f"{first_score_word}-All"

    def get_advantage_score(self):
        score_difference = self.first_score - self.second_score
        if score_difference >= 2:
            return f"Win for {self.first_name}"
        elif score_difference <= -2:
            return f"Win for {self.second_name}"
        elif score_difference == 1:
            return f"Advantage {self.first_name}"
        elif score_difference == -1:
            return f"Advantage {self.second_name}"

    def get_normal_score(self):
        return f"{self.get_score_word(self.first_score)}-{self.get_score_word(self.second_score)}"

    def get_score(self):
        if self.first_score == self.second_score:
            return self.get_draw_score()
        elif self.first_score >= 4 or self.second_score >= 4:
            return self.get_advantage_score()
        else:
            return self.get_normal_score()
