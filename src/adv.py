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
print(f'Hello, {player_name}')
my_player = Player(player_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# If the user enters "q", quit the game.
# Print an error message if the movement isn't allowed.

direction = input('In which direction would you like to move? ').lower().strip()
print(f'{my_player.player_room}')

directions = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}

while True:
    print(f'{my_player.player_room} \n')

    choice = input("Which way are you going? ")

    direction = directions[choice]

    try:
        my_player.player_room = getattr(my_player.player_room, direction)

    except AttributeError:
        print("Sorry, you cannot go that way \n") 
