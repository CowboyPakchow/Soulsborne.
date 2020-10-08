# Course: CS 30
# Period: 1
# Date Created: 20/09/21
# Date Modified: 20/09/29
# Name: Michael Nguyen
# Description: Soulsborne dictionaries of characters, locations and inventory.


# Nested dictionary of characters in Soulsborne.
characters = {
    'hero': {
      'who': 'The protagonist of the adventure. (You!)',
      'description': 'is an ordinary hero.',
      'health points': 30,
    },
    'merchant': {
      'who': 'An NPC that sells you items.',
      'description': 'is just a merchant, nothing special.',
      'health points': 0,
    },
    'floor 1 boss': {
      'who': 'The boss of floor 1.',
      'description': 'is a weak introductory boss.',
      'health points': 30,
    },
    'floor 2 boss': {
      'who': 'The boss of floor 2.',
      'description': 'is a huge skeleton boss.',
      'health points': 45,
    },
    'floor 3 boss': {
      'who': 'The final boss, gatekeeper of floor 3.',
      'description': 'is the final boss.',
      'health points': 65,
    },
    'secret floor boss': {
      'who': 'An optional secret boss.',
      'description': 'is an optional secret boss.',
      'health points': 99,
    },
    'skeleton': {
      'who': 'Common mob found on floor 1.',
      'description': 'is a commonly found mob.',
      'health points': 15,
    },
    'slime': {
      'who': 'Common mob found on floor 1.',
      'description': 'is a weak starting enemy.',
      'health points': 5,
    },
    'hollow knight': {
      'who': 'Secret enemy found on floor 1.',
      'description': 'is an optional boss.',
      'health points': 25,
    },
}

# Looping Soulsborne characters's traits.
for characters, character_info in characters.items():
    who = (character_info['who'])
    print(f"\n{characters.title()}: {who}")
    description = (character_info['description'])
    print(f"  The {characters.title()} {description}")
    health_points = (character_info['health points'])
    print(f"  The {characters.title()} has {health_points} health points.")


print()
print()

# Dictionary of floors.
floors = {
    'floor 1': 'A relatively peaceful floor for beginners.',
    'floor 2': 'Floor with dangerous monsters, proceed with caution. ',
    'floor 3': 'The end is nigh, you sense danger all around.',
    'secret floor': 'None have survived Judgement.',
}

# Looping Soulsborne floors.
for floor, space in floors.items():
    print(f"{floor.title()}: {floors[floor]}")


print()
print()

# Dictionary of different tiles.
tiles = {
    'enemy tile': 'Location of the enemy. Defeat the enemy to proceed.',
    'boss tile': 'Location of the boss. Defeat boss to proceed to next floor.',
    'blank tile': 'Just an empty tile. Move to another location.',
    'safe tile': 'Location of safe room. Rest or move to another location.',
    'item tile': 'Location of an item. Could be a weapon or healing.',
}

# Looping different tiles in Soulsborne.
for tile, space in tiles.items():
    print(f"You are on a {tile.title()}: {tiles[tile]}")

print()
print()

# Nested dictionary of the inventory.
inventory = {
    'long sword': {
        'damage': 10,
        'description': 'A standard sword.',
        'protection': 0,
    },
    'basic shield': {
        'damage': 0,
        'description': 'Shield for blocking.',
        'protection': 10,
    },
    'fire spell': {
        'damage': 10,
        'description': 'Standard magic spell.',
        'protection': 0,
    },
    'gold coins': {
        'damage': 0,
        'description': 'Currency for bartering.',
        'protection': 0,
    }
}

# Looping each item in player's inventory.
print("Hero's Inventory:")
for inventory, inventory_info in inventory.items():
    print(f"\n* {inventory.title()}:")
    description = (inventory_info['description'])
    print(f"    Description: {description}")
    damage = (inventory_info['damage'])
    print(f"    Damage: {damage}")
    protection = (inventory_info['protection'])
    print(f"    Protection: {protection}")
