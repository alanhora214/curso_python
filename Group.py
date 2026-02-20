import random
from Team import Team
from Game import Game
class Group:
    """ Group class represents a group in the tournament. It has a name and a list of teams. """

    def __init__(self, name):
        """ Custom constructor for Group class. """
        self.name = name
        self.teams = []
        self.games = []

    def add_team(self, team):
        """ Add a team to the group. """
        if isinstance(team, Team):
            self.teams.append(team)
        else:
            raise ValueError("Only Team objects can be added to the group.")
        
    def add_games(self):
        """ Schedule games for the group by pairing teams randomly. """
        if len(self.teams) < 2:
            raise ValueError("At least two teams are required to schedule games.")
        
        random.shuffle(self.teams)
        for i in range(len(self.teams) - 1):
            for j in range(i + 1, len(self.teams)):
                game = Game(self.teams[i], self.teams[j])
                self.games.append(game)

    def __str__(self):
        """ String representation of the Group class. """
        return f"Group: {self.name}, Teams: {len(self.teams)}"

    def __repr__(self):
        """ String representation of the Group class. """
        return f"Group(name={self.name}, teams={repr(self.teams)})" 