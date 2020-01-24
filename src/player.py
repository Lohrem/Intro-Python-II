# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, player_name, player_room):
        self.player_room = player_room
        self.player_name = player_name
    def __str__(self):
        return f"{self.player_name} is currently in {self.player_room}"