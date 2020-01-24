from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
player_name = input('What is your name? ')
# Make a new player object that is currently in the 'outside' room.
print(f'Hello, {player_name}')
my_player = Player(player_name, Room("outside", room['outside'])) #Room() shouldn't be just a string it should be a Room Obj

# Write a loop that:
#
# * Prints the current room name
# print(my_player.player_room.room_name)

# * Prints the current description (the textwrap module might be useful here).
print(my_player.player_room.room_desc)
# * Waits for user input and decides what to do.
direction = input('In which direction would you like to move? ').lower().strip()
# If the user enters a cardinal direction, attempt to move to the room there.
if direction == 'n':
    print('you moved north')
elif direction == 'e':
    print('you moved east')
elif direction == 's':
    print('you moved south')
elif direction == 'w':
    print('you moved west')
elif direction == 'q':
    print('the game will now end')
else:
    print('Invalid input, try N, E, S, W, or Q to quit the game')

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# class Adv:
#     def __init__(self):
