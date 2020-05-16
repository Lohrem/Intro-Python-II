# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, player_name, player_room, player_items = []):
        self.player_name = player_name #each player will have a name
        self.player_room = player_room #each player will be in a room
    def __str__(self):
        return f"{self.player_name} is currently in {self.player_room}"