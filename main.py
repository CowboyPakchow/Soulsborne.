# Course: CS 30
# Period: 1
# Date Created: 20/09/21
# Date Modified: 20/10/16
# Name: Michael Nguyen
# Description: Player class for Soulsborne.

from player import Player
import floor1
from collections import OrderedDict
from time import sleep


def play():
    """ Character movement and accessing the inventory."""
    print("Welcome to...")
    intro_text()
    floor1.parse_floor1_dsl()
    player = Player()
    # Player directions and actions they can perform while alive.
    while player.is_alive() and not player.victory:
        # Defining the player's starting position
        position = floor1.tile_at(player.x, player.y)
        # The intro of the game is printed at the starting position.
        print(position.intro_text())
        # Health points of the player are modified when they take damage.
        position.modify_player(player)
        if player.is_alive() and not player.victory:
            action_choice(position, player)


def intro_text():
    words = r"""
  _________            .__
 /   _____/ ____  __ __|  |   ______
 \_____  \ /  _ \|  |  \  |  /  ___/
 /        (  <_> )  |  /  |__\___ \
/_______  /\____/|____/|____/____  >
        \/                       \/
___.
\_ |__   ___________  ____   ____
 | __ \ /  _ \_  __ \/    \_/ __ \
 | \_\ (  <_> )  | \/   |  \  ___/
 |___  /\____/|__|  |___|  /\___  >
     \/                  \/     \/
"""
    for char in words:
        sleep(0.005)
        print(char, end=" ", flush=True)


def add_action(action_dict, hotkey, action, name):
    """Adds actions to the dictionary and prints the commands."""
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


def actions_available(position, player):
    """Only make valid actions. Actions are stored in a dictionary"""
    # All actions are stored in an ordered dictionary.
    actions = OrderedDict()
    print("\nIt's your turn, time to make a move!:  ")
    print("\n")
    # Prints items inside the inventory (If there are any.)
    if player.inventory:
        add_action(actions, "Inventory", player.print_inventory, "Inventory")
    # Prints the map of the first floor.
    if isinstance(position, floor1.ViewMapTile):
        add_action(actions, "Map", position.print_map, "Floor 1 Map")
    # Add an option for items if there are any items remaining.
    if isinstance(position, floor1.ItemTile) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    # Attack and Defend options when in battle with enemy.
    elif isinstance(position, floor1.EnemyTile) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor1.OptionalTile) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    # Move to another tile when all other actions are completed.
    else:
        if floor1.tile_at(position.x, position.y - 1):
            add_action(actions, "North", player.move_north, "Move North.")
        if floor1.tile_at(position.x, position.y + 1):
            add_action(actions, "South", player.move_south, "Move South.")
        if floor1.tile_at(position.x - 1, position.y):
            add_action(actions, "West", player.move_west, "Move West.")
        if floor1.tile_at(position.x + 1, position.y):
            add_action(actions, "East", player.move_east, "Move East.")
    # Healing for when the player's hp value is lower than 40.
    if player.hp < 40:
        add_action(actions, "Heal", player.heal, "Heal")

    return actions


def action_choice(position, player):
    """The user is asked an action to perform."""
    action = None
    while not action:
        available_actions = actions_available(position, player)
        print("\n")
        action_input = input("Make your move!:  ").lower().strip()
        action = available_actions.get(action_input)
        if action:
            action()

        else:
            print("\nWhat?! You have a list of actions! Try Again!")


def move_player(actions, player, position):
    """Depending ont the player's position, movement is changed."""
    if floor1.tile_at(position.x, position.y - 1):
        return add_action(actions, "North", player.move_north, "Move North.")
    if floor1.tile_at(position.x, position.y + 1):
        return add_action(actions, "South", player.move_south, "Move South.")
    if floor1.tile_at(position.x - 1, position.y):
        return add_action(actions, "West", player.move_west, "Move West.")
    if floor1.tile_at(position.x + 1, position.y):
        return add_action(actions, "East", player.move_east, "Move East")


play()
