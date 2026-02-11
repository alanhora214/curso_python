from Team import Team
from Athlete import Athlete
from Sport import Sport
import random

class Game:

    def __init__(self, A:Team, B:Team):
        self.set_team_a(A, "local")
        self.set_team_a(B, "visitor")
        self.score = {
            A.name: 0, B.name: 0
            }
        
    def set_team_a(self, team, role):
        if isinstance(team, Team):
            if role == "visitor":
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
    
if __name__ == "__main__":
    a = Athlete("Lionel Messi")
    b = Athlete("Diego Armando")
    s = Sport("Futbol",11,"FIFA")
    argentina = Team("Argentina",s)
    argentina.add_athlete(a)
    argentina.add_athlete(b)
    brazil = Team("Brazil",s)
    brazil.add_athlete(Athlete("Pele"))
    brazil.add_athlete(Athlete("Zico"))
    game = Game(argentina, brazil)
    game.play()
    print(game)