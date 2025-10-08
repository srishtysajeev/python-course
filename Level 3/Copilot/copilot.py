# Demonstration of Aggregation: Team and Player

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position})"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []  # Aggregation: Team has Players

    def add_player(self, player):
        self.players.append(player)

    def show_team(self):
        print(f"Team: {self.name}")
        for player in self.players:
            print(f" - {player}")

# Commentary:
# Aggregation is a relationship where one class (Team) contains references to objects of another class (Player).
# Players can exist independently of the Team. If the Team is deleted, Players can still exist elsewhere.

# Example usage:
if __name__ == "__main__":
    p1 = Player("Alice", "Forward")
    p2 = Player("Bob", "Goalkeeper")
    team = Team("Eagles")
    team.add_player(p1)
    team.add_player(p2)
    team.show_team()
    # Even if we delete the team, players still exist:
    del team
    print(p1)  # Alice (Forward)
    print(p2)  # Bob (Goalkeeper)