# Course: CS 30
# Period: 1
# Date Created: 20/10/15
# Date Modified: 20/10/16
# Name: Michael Nguyen
# Description: Player class for Soulsborne.

import items
import floor1
import sys


class Player:
    """Player class with inventory and strongest weapon in inventory."""
    def __init__(self):
        # Items that are in the player's inventory at the beginning.
        self.inventory = [items.Rapier(), items.Basic_Shield()]
        # Starting coordinates of the player.
        self.x = floor1.start_tile_location[0]
        self.y = floor1.start_tile_location[1]
        self.hp = 40
        self.victory = False

    def is_alive(self):
        """The player is still alive when their hp is at least 1."""
        return self.hp > 0

    def print_inventory(self):
        """Print the inventory of items and the strongest weapon."""
        print("Inventory:")
        for item in self.inventory:
            print("* " + str(item))
        op_weapon = self.most_powerful_weapon()
        print("Your strongest weapon is your {}".format(op_weapon))

    def most_powerful_weapon(self):
        """Determines the weapon that is the most powerful in the inventory."""
        max_damage = 0
        op_weapon = None
        # Checks damage of each weapon in your innventory and prints best one.
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    op_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return op_weapon

    def move(self, dx, dy):
        """Define player."""
        self.x += dx
        self.y += dy

    def move_north(self):
        """Defines movement that goes north. (Up)"""
        self.move(dx=0, dy=-1)

    def move_south(self):
        """Define movement that goes south. (Down)"""
        self.move(dx=0, dy=1)

    def move_east(self):
        """Define movement that goes east. (Left)"""
        self.move(dx=1, dy=0)

    def move_west(self):
        """Define movement that goes west.(Right)"""
        self.move(dx=-1, dy=0)

    def attack(self):
        """Attack the enemy by removing health points"""
        # Strongest weapon in inventory is used.
        op_weapon = self.most_powerful_weapon()
        # Position of the enemy found on the first floor.
        position = floor1.tile_at(self.x, self.y)
        enemy = position.enemy
        # Declares which weapon is used and how much it affects enemy hp value.
        print("You use {} against {}!".format(op_weapon.name, enemy.name))
        enemy.hp -= op_weapon.damage
        # Prints out if enemy remains alive and remaining hp points.
        if not enemy.is_alive():
            print("The {} has been slain.".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def heal(self):
        """Check for and use consumables to heal player hp."""
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]

        # If there are no consumables to use, print message.
        if not consumables:
            print("You do not have any items to heal you!")
            return

        # Prints out list of consumables in the inventory.
        print("Choose an item to use to heal yourself: ")
        for i, item in enumerate(consumables, 1):
            print("{}. {}".format(i, item))

        # Chooses consumable from inventory and uses it.
        valid = False
        while not valid:
            choice = input("")
            try:
                to_use = consumables[int(choice) - 1]
                # HP cap is 40 (Might be changed down the line.)
                self.hp = min(40, self.hp + to_use.healing)
                # Removes the used item from the inventory.
                # Prints current amount of health potions in inventory.
                self.inventory.remove(to_use)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("That is not a valid choice, try again!")

    def defend(self):
        """Check for and use protection items."""
        # Add protection items to the inventory.
        protection = [item for item in self.inventory
                      if isinstance(item, items.Armour)]
        # If there are no armour items, print a message.
        if not protection:
            print("You do not have any items to protect you!")
            return
        position = floor1.tile_at(self.x, self.y)
        enemy = position.enemy
        if enemy.name == "Hollow Knight":
            print("Perhaps you can parry its attacks?...")
        # Prints out list of armour items in inventory to use.
        print("Choose an item to use to protect yourself: ")
        for i, item in enumerate(protection, 1):
            print("{}. {}".format(i, item))
        # Choose protection item from inventory and use it.
        valid = False
        while not valid:
            choice = input("")
            try:
                use = protection[int(choice) - 1]
                # Armour items are used and then broken. (Defend wisely.)
                self.inventory.remove(use)
                if enemy.name == "Hollow Knight":
                    if use.name == "Basic_Shield":
                        use.protection = 10
                else:
                    if use.name == "Basic_Shield":
                        use.protection = 10

                # Damage is decreased when protection item is used.
                # Enemy damage is limited for it to not go below 0.
                enemy.damage = enemy.damage - use.protection
                if enemy.damage > 0:
                    return enemy.damage
                else:
                    enemy.damage = 0
                    return enemy.damage
                print("Damage Reduced: {}".format(enemy.damage))
                valid = True
            except (ValueError, IndexError):
                print("That is not a valid choice! Try Again!")

    def add_items(self):
        """Add items to the player's inventory when items are found."""
        # Define the position on the map of the first floor.
        position = floor1.tile_at(self.x, self.y)
        # Add the inventory from the items tile to the player's inventory.
        current_inventory = self.inventory
        position.add_inventory(current_inventory)

    def quit(self):
        """Quits out of game"""
        while True:
            word = input("Are you sure you want to quit out of the game?  ")
            if word in ['yes,']:
                print("They always return eventually...")
                sys.exit()
