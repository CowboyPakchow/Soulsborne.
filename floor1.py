# Course: CS 30
# Period: 1
# Date Created: 20/10/15
# Date Modified: 20/10/16
# Name: Michael Nguyen
# Description: Floor 1 of Soulsborne.


import random
import enemies
import sys
import items


class MapTile:
    """ The map with X and Y Coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.inventory

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        """Modify_Player for every tile."""
        pass


class StartTile(MapTile):
    """Starting position of the Player character."""

    def intro_text(self):
        """Description for the Start Tile."""
        return """
        You awaken to find yourself trapped in a dungeon of sorts.
        You must escape by clearing the three floors of the dungeon.
        You may check through your inventory to see what is on hand.
        There are 4 directions to move in, North, South, East, West.
        Floor 1": "The beginner floor, peaceful with little to no harm.
        Reach the Boss Tile (BS) to move on to the next floor. (Ends Game)
        """


class SafeRoomTile(MapTile):
    def intro_text(self):
        return """
        This is a Safe Room!
        You should be safe in here...probably.
        """


class BoringTile(MapTile):
    """Position that is literally useless."""
    def intro_text(self):
        return """
        There is nothing here to be seen.
        Move along.
        """


class ViewMapTile(MapTile):
    """Position that prints the map of the first floor."""
    def intro_text(self):
        """Description for the ViewMaptile"""
        return """
        There is a map on the floor.
        The map displays...
        """

    def print_map(self):
        """Prints a map of the entire floor (You are on Map Tile)"""
        self.floor1_printable = """
        +----------+-------+-------+-------+-----------+-------+
        | Enemy    |       | Items |       | Items     | Enemy |
        +----------+-------+-------+-------+-----------+-------+
        |          | Start | Items | Enemy |           | Enemy |
        +----------+-------+-------+-------+-----------+-------+
        |          | Enemy | Items | Items | Enemy     | Items |
        +----------+-------+-------+-------+-----------+-------+
        |          | Items |       | Items | Map Tile  | Enemy |
        +----------+-------+-------+-------+-----------+-------+
        | Optional |       | Items |       | Safe Room | Enemy |
        +----------+-------+-------+-------+-----------+-------+
        | Items    | Items | Items |       | Items     | Boss  |
        +----------+-------+-------+-------+-----------+-------+
        """
        print(self.floor1_printable)


class ItemTile(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Potion()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        Wow! It's an item tile!
        I wonder what we can find here...
        WOAH! It's a Potion!
        """
        # Description after the items are taken from the tile.
        self.no_items = "No items left at this location..."
        # Descriptions of the items tile are defined.
        items_text = [self.start_items, self.no_items]
        # After items tile has been exhausted, messages are switched.
        if self.i == 0:
            self.i += 1
            return items_text[0]
        else:
            return items_text[1]

    def artifact(self):
        """Message for what items were added into the inventory."""
        for i, item in enumerate(self.inventory, 1):
            print("You added the following items to your inventory!")
            print("{}. {}.".format(i, item.name))
        self.add_inventory()

    def add_inventory(self, current_inventory):
        """Tile items are added to the player's inventory."""
        for item in self.inventory:
            current_inventory.append(item)
        # Remove the items from the tile and add to inventory.
        self.inventory = []


class BossTile(MapTile):
    def __init__(self, x, y):
        self.j = 0
        self.k = 0
        self.enemy = enemies.King_Slime
        alive_start = """
        You encounter the King Slime!
        It doesn't seem like a big threat.
        You can probably defeat it.
        """
        alive_attack = "King Slime attacks!"
        self.alive_text = [alive_start, alive_attack]
        dead_start = """
        You've defeated King Slime!
        You can move on to the next floor.
        """
        dead_return = "Moving to next floor..."
        self.dead_text = [dead_start, dead_return]

    def modify_player(self, player):
        player.victory = True
        sys.exit()

    def intro_text(self):
        return """
        Thanks for playing the demo of Soulsborne!
        More is on the way soon!
        """


class OptionalTile(MapTile):
    def __init__(self, x, y):
        self.j = 0
        self.k = 0
        # Optional Boss 100% spawns on this tile. (Hollow Knight)
        self.enemy = enemies.Hollow_Knight()
        alive_start = """
        You encounter the Hollow Knight!
        A former shell of a Knight.
        """
        alive_attack = "Hollow Knight attacks!"
        self.alive_text = [alive_start, alive_attack]
        dead_start = """
        You've defeated the Hollow Knight!
        You've defeated 1 of 3 Optional Bosses!
        """
        dead_return = "Congratulations..."
        self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Intro message changes as the player attacks the enemy.
            if self.j == 0:
                self.j += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.k == 0:
                self.k += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        """
        Checks the enemy's current strength so it can respond to the player
        """
        if self.enemy.is_alive():
            # If the player has hp remaining, continue the game.
            if player.hp > self.enemy.damage:
                player.hp -= self.enemy.damage
                print("The {} does {} damage. You have {} HP remaining".
                      format(self.enemy.name,
                             self.enemy.damage,
                             player.hp))
            # When the player runs out of hp, end the game.
            elif player.hp <= self.enemy.damage:
                print("The {} causes mortal damage. You die.".
                      format(self.enemy.name))
                sys.exit()


class EnemyTile(MapTile):
    """Enemy position and messages"""
    def __init__(self, x, y):
        """Creates a random position for each enemy"""
        # Indices of j and k to switch out alive and dead messages.
        self.j = 0
        self.k = 0
        # Generates a random number that spawns a certain enemy.
        r = random.random()
        # Slime encounters are about 50%.
        if r < 0.30:
            self.enemy = enemies.Slime()
            alive_start = """
            You encounter a little slime!
            It doesn't seem very harmful.
            Looks very easy to kill.
            """
            alive_attack = "The Slime attacks."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The slime disappears into thin air.
            """
            dead_return = "Slime condensate floats on the ground..."
            self.dead_text = [dead_start, dead_return]

        # Goblin encounters are about 20%.
        elif r < 0.50 and r >= 0.30:
            self.enemy = enemies.Goblin()
            alive_start = """
            You encounter a Goblin!
            A good goblin? You could find one if you looked hard enough.
            """
            alive_attack = "The Goblin attacks!"
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
              The Goblin falls over and dies.
            """
            dead_return = "The Goblin has been defeated."
            self.dead_text = [dead_start, dead_return]

        # Lizard encounters are about 20%.
        elif r < 0.80 and r >= 0.60:
            self.enemy = enemies.Lizard()
            alive_start = """
            You encounter a Lizard!
            Why is there a Lizard here?
            Does that even matter?
            Probably not.
            Good, then don't ask.
            """
            alive_attack = "The Lizard attacks!"
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The Lizard literally disappears.
            What how?!
            Uh, it did the disappearing thing.
            Oh.
            """
            dead_return = "The Lizard has been defeated."
            self.dead_text = [dead_start, dead_return]

        else:
            self.enemy = enemies.Skeleton()
            alive_start = """
            You encounter a Skeleton!
            Are Skeletons even on this floor?
            If not, why is here?
            """
            alive_attack = "The Skeleton waves its arms!"
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The Skeleton crumbles into a pile of bones.
            It's not gonna do the "come back to life" thing is it?
            Uh... Who knows.
            """
            dead_return = "The Skeleton has been defeated."
            self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message depending on enemy hp."""
        if self.enemy.is_alive():
            # After the player attacks, message switches.
            if self.j == 0:
                self.j += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.k == 0:
                self.k += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        """
        Checks the enemy's current strength so it can respond to the player
        """
        if self.enemy.is_alive():
            # Game will continue to run as long as the player has hp.
            if player.hp > self.enemy.damage:
                player.hp -= self.enemy.damage
                print("The {} does {} damage. You have {} HP remaining".
                      format(self.enemy.name,
                             self.enemy.damage,
                             player.hp))
            # If the player runs out of hp, the game ends.
            elif player.hp <= self.enemy.damage:
                print("The {} causes mortal damage. You die.".
                      format(self.enemy.name))
                sys.exit()


floor1_map = []


def tile_at(x, y):
    """Locates the tile at a coordinate"""
    if x < 0 or y < 0:
        return None
    try:
        return floor1_map[y][x]
    except IndexError:
        return None


# Floor 1's map in abbreviations.
floor1_dsl = """
|ET|BT|IT|BT|IT|ET|
|BT|ST|IT|ET|BT|ET|
|BT|ET|IT|IT|ET|IT|
|BT|IT|BT|IT|MT|ET|
|OT|BT|IT|BT|SF|ET|
|IT|IT|IT|BT|IT|BS|
"""


def is_dsl_valid(dsl):
    """
    Check to make sure there is only one start tile and escape pod.
    Also check that each row has the same number of columns
    """
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|BS|") == 0:
        return False
    if dsl.count("|OT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True

# Key to Floor 1's tiles.
tile_type_dict = {"ST": StartTile,
                  "IT": ItemTile,
                  "ET": EnemyTile,
                  "BT": BoringTile,
                  "MT": ViewMapTile,
                  "BS": BossTile,
                  "OT": OptionalTile,
                  "SF": SafeRoomTile,
                  "  ": None}
# Initializes the Starting Tile.
start_tile_location = None


def parse_floor1_dsl():
    """Floor 1 map considered a string and returned as a list."""
    if not is_dsl_valid(floor1_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = floor1_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    # Iterate over each line in the DSL.
    for y, dsl_row in enumerate(dsl_lines):
        # Object created to store lines.
        row = []
        # Line is split into abbreviations.
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cells in enumerate(dsl_cells):
            # Look up the abbreviation in the dictionary.
            tile_type = tile_type_dict[dsl_cells]
            # Starting Tile is set.
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)
        # Add the whole row to the first floor map.
        floor1_map.append(row)
