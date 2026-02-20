import random
import json
from Game import Game
from Group import Group
from Team import Team
from Sport import Sport
from Athlete import Athlete

class Tournament:
    """ Tournament class represents a tournament. It has a name, a sport, and a list of teams. """

    def __init__(self, name):
        """ Custom constructor for Tournament class. """
        self.name = name
        self.teams = []
        self.games = []

    def add_team(self, team: Team):
        """ Add a team to the tournament. """
        if isinstance(team, Team):
            self.teams.append(team)
        else:
            raise ValueError("Only Team objects can be added to the tournament.")

    def schedule_games(self):
        """ Schedule games for the tournament by pairing teams randomly. """
        if len(self.teams) < 2:
            raise ValueError("At least two teams are required to schedule games.")
        
        random.shuffle(self.teams)
        for i in range(0, len(self.teams) - 1, 2):
            game = Game(self.teams[i], self.teams[i + 1])
            self.games.append(game)

    def play_tournament(self):
        """ Simulate playing all games in the tournament. """
        for game in self.games:
            game.play()

    def __str__(self):
        """ String representation of the Tournament class. """
        return f"Tournament: {self.name}, Teams: {len(self.teams)}, Games: {len(self.games)}"

    def __repr__(self):
        """ String representation of the Tournament class. """
        return f"Tournament(name={self.name}, teams={repr(self.teams)}, games={repr(self.games)})"

    def to_json(self):
        """ Convert the Tournament object to a JSON string. """
        return {
            "name": self.name,
            "teams": [team.to_json() for team in self.teams],
            "games": [game.to_json() for game in self.games]
        }
    
    def set_group(self,group_list, group_name):
        """ Set a group for the tournament by pairing teams randomly. """
        group = Group(group_name)
        for team in group_list:
            group.add_team(team)
        self.groups[group_name] = group

    def set_group_stage(self):
        """ Set the group stage for the tournament by pairing teams randomly. """
        if len(self.teams) == 8:
            group_a = self.teams[:4]
            group_b = self.teams[4:]
            for i in range(len(group_a)):
                game = Game(group_a[i], group_b[j])
                self.games.append(game)


    def load_json(self, filename)       :
        """ Load a Tournament object from a JSON file. """
        with open(filename, 'r', encoding="utf-8") as f:
            data = json.load(f)
        for team_data in data["teams"]:
            team = Team(team_data["name"], team_data["name"])
            players = team_data["athletes"]
            for player in players:
                team.add_athlete(Athlete(player))
            self.add_team(team)

if __name__ == "__main__":  
    tournament = Tournament("FIFA World Cup")
    tournament.load_json("tournament.json")
    print(tournament)