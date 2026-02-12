from Team import Team
from Athlete import Athlete
from Sport import Sport
import random
import json

class Game:

    def __init__(self, A:Team, B:Team):
        self.set_team_a(A, "local")
        self.set_team_a(B, "visitor")
        self.score = {
            A.name: 0, B.name: 0
            }
        
    def set_team_a(self, team, role):
        if isinstance(team, Team):
            if role == "local":
                self.team_a = team
            elif role == "visitor":
                self.team_b = team
            else:
                raise ValueError("Role must be 'local' or 'visitor'")
            
    def play(self):
        self.score[self.team_a.name] = random.randint(0,Sport.max_score[self.team_a.sport.name])
        self.score[self.team_b.name] = random.randint(0,Sport.max_score[self.team_b.sport.name])

    def __str__(self):
        return f"{self.team_a.name} vs {self.team_b.name} - Score: {self.score[self.team_a.name]}:{self.score[self.team_b.name]}"
    
    def to_json(self):
        """
        """
        return {
            "team_a":self.team_a.to_json(),
            "team_b":self.team_b.to_json(),
            "score": self.score
        }
    
def a_game():
        """
        Docstring for a_game
        """
        players_mex = ('Chicharito', 'Raul Jimenez', 'Hirving Lozano')
        players_arg = ('Lionel Messi', 'Serigio Aguero', 'Paulo Dybala')
        sport = Sport("Futbol", 11, "FIFA")
        team_mex = Team("Mexico", sport)
        team_arg = Team("Argentina", sport)
        for player in players_mex:
            team_mex.add_athlete(Athlete(player))
        for player in players_arg:
            team_arg.add_athlete(Athlete(player))
        game = Game(team_mex, team_arg)
        game_string = game.to_json()
        return game_string

def save_game_to_json(game_data, filename):
        """
        """
        with open(filename, 'w', encoding='utf-8') as f:json.dump(game_data, f, indent=4)
        
if __name__ == "__main__":
    string_game = a_game()
    save_game_to_json(string_game, "game.json")
