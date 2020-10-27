# Course: CS 30
# Period: 1
# Date Created: 20/09/21
# Date Modified: 20/10/26
# Name: Michael Nguyen
# Description: Main file to run Soulsborne.

from player import Player
import floor
from collections import OrderedDict
from time import sleep
import sys


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


def move_player(actions, player, position):
    """Depending on the player's position, movement is changed."""
    if floor.tile_at(position.x, position.y - 1):
        return add_action(actions, "North", player.move_north, "Move North.")
    if floor.tile_at(position.x, position.y + 1):
        return add_action(actions, "South", player.move_south, "Move South.")
    if floor.tile_at(position.x - 1, position.y):
        return add_action(actions, "West", player.move_west, "Move West.")
    if floor.tile_at(position.x + 1, position.y):
        return add_action(actions, "East", player.move_east, "Move East")

    def quit(self):
        """Quits out of game"""
        while True:
            word = input("Are you sure you want to quit? ")
            if word in ['yes']:
                print("They always return eventually...")
                sys.exit()
            else:
                break


def actions_available(position, player):
    """Only make valid actions. Actions are stored in a dictionary"""
    # All actions are stored in an ordered dictionary.
    actions = OrderedDict()
    print("\nIt's your turn, time to make a move!:  ")
    print("\n")
    # Prints items inside the inventory (If there are any.)
    if player.inventory:
        add_action(actions, "Inventory", player.print_inventory, "Inventory")
    # Prints the map of the Starting Room.
    if isinstance(position, floor.ViewMapTile):
        add_action(actions, "Map", position.print_map, "Floor Map")
    if isinstance(position, floor.RightMap):
        add_action(actions, "Map", position.print_map, "Right Path Map")
    if isinstance(position, floor.LeftMap):
        add_action(actions, "Map", position.print_map, "Left Path Map")
    if isinstance(position, floor.TopMap):
        add_action(actions, "Map", position.print_map, "Top Path Map")
    if isinstance(position, floor.BotMap):
        add_action(actions, "Map", position.print_map, "Bot Path Map")
    if isinstance(position, floor.SafeRoomTile):
        add_action(actions, "Trade", player.trade, "Trade")
    # Add an option for items if there are any items remaining.
    if isinstance(position, floor.ItemTileL) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    if isinstance(position, floor.ItemTileR) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    if isinstance(position, floor.ItemTileT) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    if isinstance(position, floor.ItemTileB) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    if isinstance(position, floor.BossLootL) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    if isinstance(position, floor.BossLootR) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    if isinstance(position, floor.BossLootT) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    if isinstance(position, floor.SpecialLootT) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    if isinstance(position, floor.SpecialLootR) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    if isinstance(position, floor.SpecialLootL) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    if isinstance(position, floor.ArtoriasLoot) and position.inventory:
        add_action(actions, "Add", player.add_items, "Add Items")
    # Attack and Defend options when in battle with enemy.
    elif isinstance(position, floor.EnemyTileR) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor.EnemyTileT) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor.EnemyTileL) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor.EnemyTileB) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor.OptTileL) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor.OptTileR) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor.OptTileT) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor.BossTileR) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor.BossTileL) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor.BossTileT) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    elif isinstance(position, floor.BossTileB) and position.enemy.is_alive():
        add_action(actions, "Attack", player.attack, "Attack")
        add_action(actions, "Defend", player.defend, "Defend")
    # Move to another tile when all other actions are completed.
    else:
        if floor.tile_at(position.x, position.y - 1):
            add_action(actions, "North", player.move_north, "Move North.")
        if floor.tile_at(position.x, position.y + 1):
            add_action(actions, "South", player.move_south, "Move South.")
        if floor.tile_at(position.x - 1, position.y):
            add_action(actions, "West", player.move_west, "Move West.")
        if floor.tile_at(position.x + 1, position.y):
            add_action(actions, "East", player.move_east, "Move East.")
    # Healing for when the player's hp value is lower than 60.
    if player.hp < 60:
        add_action(actions, "Heal", player.heal, "Heal")
    if player.quit:
        add_action(actions, "Quit", player.quit, "Quit out of game.")

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


def play():
    """ Character movement and accessing the inventory."""
    print("Welcome to...")
    intro_text()
    floor.parse_floor_dsl()
    player = Player()
    # Player directions and actions they can perform while alive.
    while player.is_alive() and not player.victory:
        # Defining the player's starting position
        position = floor.tile_at(player.x, player.y)
        # The intro of the game is printed at the starting position.
        print(position.intro_text())
        # Health points of the player are modified when they take damage.
        position.modify_player(player)
        if player.is_alive() and not player.victory:
            action_choice(position, player)


play()
