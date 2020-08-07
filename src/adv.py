import cmd
import textwrap
import sys
import os
import time
import random


from room import Room
from player import *
from item import Item


# Declare all the rooms
item = {
    'backpack': Item("Backpack", "The bag to carry all your goodies"),
    'shield': Item("Shield", "The protection"),
    'arrows': Item("Arrows", "Pointy wooden flying weapons"),
    'sword': Item("Sword", "Sharp metal swingy thing"),
    'bow': Item('Bow', 'To shoot the arrows'),
    'axe': Item("Axe", "Cut down some trees of people"),
    'health': Item("Health Potion", "The big healer")
}

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mouth beckons", item['axe']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['arrows']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['sword']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['backpack']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['health']),
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

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#Items


# navigation

player = Player("", room['outside'])


# interface functions
def adventure_screen(header, body):
    os.system('cls')
    print("##################################")
    text_display(f"     {header}")
    print("\n##################################")
    print("                                  ")
    print("                                  ")
    text_display(body)
    print("\n                                  ")
    print("                                  ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def prompt():
    room_name = player.current_room.name
    room_desc = player.current_room.description
    adventure_screen(room_name, room_desc)
    while player.hp > 0 and player.game_over is False:
        choose_action()


## player action functions

# routes function based on player input
def choose_action():
    print(f"Which do you want to do?")
    print(f"[Move, Search, Inventory]")
    user_input = input("> ").lower().strip()
    actions = ("move", "m", "search", "s", "quit", "q", "inventory", "i", "help", "?", "h")
    if user_input in ("move," "m"):
        move_action()
    elif user_input in ("search," "s"):
        search()
    elif user_input in ("q", "quit", "exit"):
        quit_game()
    elif user_input in ("help", "?", "h"):
        help_menu()
    elif user_input in ("inventory", "i"):
        inventory()
    else:
        print("not a valid instruction")

# handles game navigation
def move_action():
    print(f"\n ===============")
    print(f"Which way?")
    user_input = input("> ").lower().strip()
    cardinal = ("n", "s", "e", "w", "north",
                "south", "east", "west", "actions", "a")

    if user_input not in cardinal:
        print("Not a valid direction or instruction, try again or press 'Q' to quit.\n")
        move_action()
    if user_input in ("n", "s", "e", "w"):
        # stores current room in temp variable for player.curr_room to be reused shold the try fail
        this_room = player.current_room
        try:
            player.current_room = player.change_room(
                player.current_room, user_input)
            prompt()
        except:
            print("Nothing lies for you that way...")
            player.current_room = this_room
            move_action()
    if user_input in ("actions", "a"):
        choose_action()

# General game functions
def quit_game():
    text_display("are you sure? (Y/N)\n")
    user_input = input("> ").lower().strip()
    if user_input == "y":
        print("See you next time...")
        os.system('cls')
        sys.exit()
    elif user_input == "n":
        prompt()


def help_menu():
    print("Type 'Play' to start the game or type 'Q' or'Quit' to Quit. use N, S, E, W to navigate")
    print("In game use 'N', 'S', 'E', 'W' to navigate and 'Enter' to confirm an action")

# renders text characters when entering room
def text_display(text_var):
    for character in text_var:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)


def main_game():
    welcome()
    prompt()


# title screen & options
def title_screen():
    os.system('cls')
    print("##################################")
    print("#         Darkest Dungeon        #")
    print("##################################")
    print("                                  ")
    print("              -Play-              ")
    print("              -Help-              ")
    print("              -Quit-              ")
    print("                                  ")
    print("##################################")
    title_screen_options()


def title_screen_options():
    print("Please choose")
    option_input = input("> ")
    option = option_input.lower().strip()
    if option in ("help", "h", "?"):
        help_menu()
        title_screen_options()
    if option in ("p", "play"):
        main_game()
    if option in ("quit", "exit", "q"):
        text_display("See you next time, brave warrior")
        os.system('cls')
        sys.exit()
    else:
        title_screen_options()


def welcome():
    os.system('cls')
    header = "Darkest Dungeon"
    name_question = "Welcome my lord, what is your name?"
    adventure_screen(header, name_question)
    player_name = input("> ")
    player.name = player_name
    text_display(f"Welcome brave hero " + player_name + "!!!!")
    print("")


def search():
    if (player.current_room.item == None):
        print("The room is empty")
    else:
        print(f'You look down and find a {player.current_room.item}\n\n')

    direction = input(
        "\n\n Please type [take]+[item] or [drop]+[item]:  ").lower()
    direction = direction.strip().split(maxsplit=1)
    if (direction[0] == 'take' or direction[0] == 'grab'):
        if(len(direction) == 2):
            if (player.current_room.item.name.lower() == direction[1]):
                player.addItem(direction[1])
                player.current_room.item = None
                print(f"{direction[1]} picked up\n\n")
            else:
                print(
                    f"{direction[1]} not found in {player.current_room.name}")
        else:
            print("Specify item to grab")
    elif (direction[0] == 'drop' or direction[0] == 'throw'):
        if (len(direction) == 2):
            if (direction[1] in player.items):
                    player.dropItem(direction[1])
                    player.current_room.item = direction[1]
                    # player.current_room.items = 1
                    print(f"{direction[1]} dropped \n\n")
            else:
                print(f"{direction[1]} not found in your inventory")
    # else:
    #     print("Specify item to grab")
    else:
        print(f"input not recognized, please follow instructions")

#inventory
def inventory():
    player.view_items()


# Game start
title_screen()