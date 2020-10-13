# Course: CS 30
# Period: 1
# Date Created: 20/10/07
# Date Modified: 20/10/08
# Name: Michael Nguyen
# Description: Map of Soulsborne detailing the 4 floors.

import random
from tabulate import tabulate


def append_list(dictionary, list):
    """Creating a list from elements in a dictionary."""
    for x in dictionary:
        list.append(x)


def random_tile(list, tile):
    """Choosing random tile to replace indices."""
    x = random.choice(list)
    y = random.choice(x)
    a = list.index(x)
    b = x.index(y)
    list[a][b] = tile
    return(a, b)


def tile_replace(list, tile1, tile2, tile3, tile4):
    """Making sure replaced tiles do not overlap."""
    while random_tile(list, tile1) == random_tile(list, tile2):
        random_tile(list, tile1)
        random_tile(list, tile2)
    while random_tile(list, tile3) == random_tile(list, tile4):
        random_tile(list, tile3)
        random_tile(list, tile4)


def generate_map(list):
    """Randomly generate a 5x6 map with different tile types."""
    map = [[random.choice(list) for z in range(6)] for v in range(6)]
    tile_replace(map, "Boss", "Start", "Optional", "Safe Room")
    return map


def print_map(dictionary):
    """Printing the map with each floor. Formats in rows and columns."""
    for key in dictionary:
        map = dictionary[key]
        print(f"{key}")
        print(tabulate(map, tablefmt="grid"))
        print("\n")

# Floors in Soulsborne.
floors = {"Floor 1": "The beginner floor, peaceful with little to no harm.",
          "Floor 2": "Many adventureres have fallen here, be careful.",
          "Floor 3": "The end is nigh, nowhere is safe.",
          "Secret Floor": "Seekers receive Judgement, None Return."
          }

# Map tiles in Soulsborne.
map_tiles = {"Start": {
                        "description": "Starting area of the player.",
                        "abbrieviation": "S",
                        "action":
                        "Move to another location"},
             "Boss": {
                        "description": "Boss of the floor.",
                        "abbrievation": "BT",
                        "action":
                        "Defeat the boss to move to next floor."},
             "Enemy": {
                        "description": "Location of an Enemy.",
                        "abbrieviation": "ET",
                        "action":
                        "Defeat the enemy to continue."},
             "Items": {
                        "description": "Location of an item",
                        "abbrieviation": "IT",
                        "action":
                        "Pick up item to continue."},
             "Safe Room": {
                        "description": "Location of safe room",
                        "abbrieviation": "ST",
                        "action":
                        "Trade with merchant, rest or move"},
             " ": {
                        "description": "Blank location, nothing happens.",
                        "abbrieviation": "BT",
                        "action":
                        "Move to a different location"},
             "Optional": {
                            "description": "Optional Boss location",
                            "abbrieviation": "OP",
                            "action":
                            "Defeat boss to continue."}}


# List of floors.
floor_level = []
append_list(floors, floor_level)
# List of tiles and Removing start, boss, optional and safe floors.
tile_types = []
append_list(map_tiles, tile_types)
tile_types.remove("Boss")
tile_types.remove("Start")
tile_types.remove("Optional")
tile_types.remove("Safe Room")

# Using loop function to help print floors into map.
main_map = {}
for floor in floor_level:
    floors = generate_map(tile_types)
    main_map[floor] = floors

# Printing the Main Map.
(print_map(main_map))
