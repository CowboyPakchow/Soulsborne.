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
import npc


class MapTile:
    """ The map with X and Y Coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.inventory

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def intro_text2(self):
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
        You must escape by reaching the Champion Tile. (Located in Bottom Floor.)
        You may check through your inventory to see what is on hand.
        There are 4 directions to move in, North, South, East, West.
        Head East to use the map that details the current room you're in.
        Good luck weary traveler, "May the Sapphire Star Guide you."
        Now that's a cool line.
        Thanks! It was from Monster Hunter World!
        oh.
        """


class ChampionsTile(MapTile):
    def intro_text(self):
        """Description for the Champions Tile."""
        return """
        Long ago there was a champion who made it to safety.
        Slaying all in his path, he spared none.
        On and on, he never stopped slaying.
        Until he himself, became a husk of the dungeon.
        What's left of him is only a chalice.
        A chalice that frees the souls.
        """

    def intro_text2(self):
        """Description for Epilogue."""
        return """
        Well I guess that concludes my story.
        Lucky we got out of there right buddy?
        Buddy?..
        Oh right...
        You were only a part of my imagination.
        Back to being alone...

        End.
        """

    def modify_player(self, player):
        print("You are worthy. You may leave.")
        print("\n")
        print("Well, I guess that concludes my story.")
        print("Lucky we got out of there right buddy?")
        print("Buddy?...")
        print("Oh right...")
        print("You were only a part of my imagination.")
        print("Back to being alone...")
        print("\n")
        print("End")
        print("Thanks for playing!")
        player.victory = True
        sys.exit()


class SafeRoomTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 0):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or type 'quit' to quit: ")
            if user_input in ['Quit', 'quit']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("You have no gold for that item!")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Barter Success!!")

    def check_if_trade(self, player):
        while True:
            print("Would you like to Buy, Sell, or Quit?")
            user_input = input()
            if user_input in ['Quit', 'quit']:
                return
            elif user_input in ['Buy', 'buy']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['Sell', 'sell']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def intro_text(self):
        return """
        This is a Safe Room!
        You should be safe in here...probably.
        There is a Merchant on this tile.
        You can trade with him.
        Note that once you buy something it gets taken off the list.
        Ex: 1. Humanity 2. Greatsword -> Buy Humanity
            1. Greatsword
        """


class GoldTile(MapTile):
    """Position that offers gold to the player."""
    def __init__(self, x, y):
        self.gold = random.randint(20, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+ {} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            Well this tile seems useless now.
            Let's move on.
            """
        else: 
            return """
            LOOK IT'S GOLD!
            Imagine being the loser that dropped this!
            You pick up the gold.
            """


class BoringTile(MapTile):
    """Position that is literally useless."""
    def intro_text(self):
        return """
        There is nothing here to be seen.
        Move along.
        Seriously there is nothing here.
        It's a blank tile, so you can leave now.
        Shoo.
        """


class RightPath(MapTile):
    """Position that descrILes Right Path of Dungeoon."""
    def intro_text(self):
        """Description for Right Path Tile."""
        return """
        You are about to take the Right Path.
        This path is relatively easy and should be the one you take first.
        Of course you don't have to.
        But there's no telling what'll happen to you.
        """


class LeftPath(MapTile):
    """Position that descrILes Left Path of Dungeon"""
    def intro_text(self):
            """Description for the Left Path Tile."""
            return """
            You are about to take the Left Path.
            We recommend taking this path after the Right Path.
            But this game is an experience for anyone so we won't stop you.
            Don't blame us if it becomes too hard.
            Once again, who is us?
            Shut it.
            ok.
            (Recommended After Right Path.)
"""


class TopPath(MapTile):
    """Position that descrILes Top Path of Dungeon."""
    def intro_text(self):
        """Description for the Top Path Tile."""
        return """
        You are about to take the Top Path.
        Are people even reading these things?
        Do I even need to say anything anymore?
        Does our words even matter?
        Perhaps I'm just losing my mind at this point...
        I mean who'd come down here right?
        (Recommended after Left Path and Right Path.)
        """


class BottomPath(MapTile):
    """Position that descrILes Bottom Path of Dungeon."""
    def intro_text(self):
        """Description for the Bottom Path tile"""
        return """
        It's only me now.
        Everyone's gone.
        It's only me.
        It's only me.
        It's only me.
        Weary traveler if you ever make it thus far.
        Don't ever go down to the bottom path.
        Any other will do.
        Just.
        NEVER.
        GO.
        DOWN.
        (Recommended after ALL OTHER paths have been taken.)
        """


class ViewMapTile(MapTile):
    """Position that prints the map of the Starting Room."""
    def intro_text(self):
        """Description for the ViewMaptile"""
        return """
        There is a map on the floor.
        The map displays...
        """

    def print_map(self):
        """Prints a map of the entire floor (You are on Map Tile)"""
        self.floor_printable = """
                            +-------+
                            | Blank |
            +-------+-------+-------+-------+-------+
            | Blank | Blank |  Top  | Blank | Blank |
            +-------+-------+-------+-------+-------+
            | Blank | Items | Items | Items | Blank |
    +-------+-------+-------+-------+-------+-------+-------+
    | Blank | Left  | SafeR | Start |  Map  | Right | Blank |
    +-------+-------+-------+-------+-------+-------+-------+
            | Blank | Gold  | Gold  | Gold  | Blank |
            +-------+-------+-------+-------+-------+
            | Blank | Blank |  Bot  | Blank | Blank |
            +-------+-------+-------+-------+-------+
                            | Blank |
                            +-------+

        We recommend you go right first as it is the easier experience.
        Of course you don't need to listen.
        You'll just be making your life a lot harder.
        We really mean that.
        ...Who's we? Isn't it just you???
        """
        print(self.floor_printable)


class RightMap(MapTile):
    """Position that prints map of Right Path."""
    def intro_text(self):
        """Description for RightMap Tile"""
        return """
        There is a map in the room.
        The map displays...
        """

    def print_map(self):
        """Prints map of the Entire Right Path. (You are on Map Tile)"""
        self.floor_printable = """

                                +-------+-------+-------+-------+-------+
                                | Warn  | Blank | Safe  |  Boss | BLoot |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| Gold  | Items | Blank | Enemy | Gold  |
+-------+-------+-------+-------+-------+
| Enemy | Items | Blank | Enemy | Items |
+-------+-------+-------+-------+-------+
| Enemy | Enemy | Enemy | Items | Items |
+-------+-------+-------+-------+-------+
| Blank | Enemy | Items | Enemy | Blank |
+-------+-------+-------+-------+-------+
| Blank | Items |  Map  | Items | Enemy |
+-------+-------+-------+-------+-------+
                | Blank |
                +-------+
                | Blank |
+-------+-------+-------+-------+-------+-------+
| Enemy | Items | Blank | Blank |  Opt  | OLoot |
+-------+-------+-------+-------+-------+-------+
| Enemy | Blank | Items | Enemy | Blank |
+-------+-------+-------+-------+-------+
|  Map  | Enemy | Enemy | Enemy | Blank |
+-------+-------+-------+-------+-------+
| Enemy | Gold  | Enemy | Gold  | Items |
+-------+-------+-------+-------+-------+
| Items | Items | Enemy | Blank | Blank |
+-------+-------+-------+-------+-------+

        T-This is a big Room isn't it?
        Well yeah it's a dungeon what did you expect?
        This was supposed to be the easier route right?
        Yeah it is, why're you so skeptical?
        I'm literally talking to myself to comfort myself!
        Yeah you're just weird man, anyways...
        This is the layout to the Right Path. Good Luck!
"""
        print(self.floor_printable)


class LeftMap(MapTile):
    """Position that prints map of Left Path."""
    def intro_text(self):
        """Description of LeftMap Tile."""
        return """
        Another map who would've guessed.
        Let's see what we're in for.
        """

    def print_map(self):
        """Prints map of Entire Left Path."""
        self.floor_printable = """

+-------+-------+-------+-------+-------+
| Enemy | Items | Gold  | Items | Enemy |
+-------+-------+-------+-------+-------+
| Blank | Items | Enemy | Blank | Enemy |
+-------+-------+-------+-------+-------+
| Enemy | Items | Items | Enemy |  Map  |
+-------+-------+-------+-------+-------+
| Items | Enemy | Blank | Items | Enemy |
+-------+-------+-------+-------+-------+
|  Opt  | Items | Enemy | Blank | Enemy |
+-------+-------+-------+-------+-------+
| Loot  |       | Gold  |
+-------+       +-------+
                | Blank |
+-------+-------+-------+-------+-------+
| Enemy | Items |  Map  | Items | Enemy |
+-------+-------+-------+-------+-------+
| Blank | Enemy | Items | Enemy | Blank |
+-------+-------+-------+-------+-------+
| Enemy | Items | Enemy | Items | Blank |
+-------+-------+-------+-------+-------+
| Blank | Enemy | Enemy | Items | Blank |
+-------+-------+-------+-------+-------+
| Enemy | Blank | Blank | Items | Items |
+-------+-------+-------+-------+-------+
| Blank |
+-------+
| Warn  |
+-------+
| Blank |
+-------+
| Safe  |
+-------+
| Enemy |
+-------+
| Boss  |
+-------+
| Loot  |
+-------+

        These maps are really weird.
        Well these are representative of the entire floor.
        So the entire floor is kinda weird then.
        Yeah pretty much.
"""
        print(self.floor_printable)


class TopMap(MapTile):
    """Position that prints map of Top Path."""
    def intro_text(self):
        """Description of TopMap Tile."""
        return """
        Who's even leaving these maps?
        Some adventurers from long ago.
        Did they ever make it out?
        HAHAHAHAHA! You're a funny guy.
        """

    def print_map(self):
        """Prints map of Entire Top Path."""
        self.floor_printable = """

                        +-------+               +-------+-------+-------+-------+-------+-------+
                        | Blank |               | Loot  |  Opt  | Blank | Items | Enemy | Enemy |
                        +-------+-------+       +-------+-------+-------+-------+-------+-------+
                        | Enemy | Items |               | Enemy | Gold  | Blank | Items | Items |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| Loot  | Boss  | Enemy | Items | Safe  | Warn  | Blank | Gold  | Enemy | Items | Items | Enemy |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
                        | Enemy | Items |               | Blank | Enemy | Enemy | Items | Blank |
                        +-------+-------+               +-------+-------+-------+-------+-------+
                        | Blank |                       | Enemy | Enemy |  Map  | Blank | Enemy |
                        +-------+                       +-------+-------+-------+-------+-------+

        So what happens if we end up defeating all four bosses?
        Well, you get to leave that's what.
        Wait really?
        Yeah.
        LET'S GET TO IT!
        ...
"""
        print(self.floor_printable)


class BotMap(MapTile):
    """Position that prints map of Bottom Path."""
    def intro_text(self):
        """Description of BotMap Tile."""
        return """
        How did people ever show up in these places anyways?
        Hm..I guess they just showed up.
        What? Wouldn't someone had to have thrown them in here or something.
        Probably, but I wouldn't know.
        Why not?
        I'm a figment of your imagination.
        Oh right.
        """

    def print_map(self):
        """Prints map of Entire Top Path."""
        self.floor_printable = """


+-------+-------+-------+-------+-------+                       +-------+
| Enemy | Blank |  Map  | Enemy | Items |                       | Blank |
+-------+-------+-------+-------+-------+               +-------+-------+
| Blank | Items | Enemy | Enemy | Enemy |               | Items | Enemy |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| Enemy | Blank | Items | Blank | Enemy | Blank | Warn  | Safe  | Boss  | Boss  | Boss  | ALoot | Boss  | Champ |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| Blank | Blank | Enemy | Enemy | Blank |               | Items | Enemy |
+-------+-------+-------+-------+-------+               +-------+-------+
| Blank | Blank | Blank | Blank | Enemy |                       | Blank |
+-------+-------+-------+-------+-------+                       +-------+

        Man I'm already tired..
        Seriously?
        Yeah...
        Well boohoo, sucks to be you, let's keep going.
        Man you're mean...
        Then stop thinking negative.
        Hm...maybe...
"""
        print(self.floor_printable)


class ItemTileR(MapTile):
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


class ItemTileT(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Estus()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        Alright! an item tile!
        Let's see here...
        An estus flask? Well that seems familiar...
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


class ItemTileL(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Great_Potion()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        An items tile, let's get this out onto a tray.
        Nice!
        A great potion.
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


class ItemTileB(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Humanity()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        Another item tile huh.
        Let's see what's in stock.
        It's..it's...humanity?
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


class SpecialLootR(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Hollow_Shield(), items.Hollow_Blade()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        The Knight's items.
        These are mine now.
        Hollow Shield and Blade are on this tile.
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


class SpecialLootL(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Galahad_Shield(), items.Secace()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        These weapons seem very familiar..
        Secace?
        Galahad's Shield?
        Hm...
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


class SpecialLootT(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Guardians_Safeguard()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        Guardian Loot...
        Very...chic?
        Guardian's Safeguard is on this tile.
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


class ArtoriasLoot(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Humanity(), items.Abysswalker(),
                          items.Abysswalker_Arm()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        What is this?
        It's an Armguard and a Sword.
        It radiates only darkness.
        Nothing more.
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


class BossWarning(MapTile):
    """Position that descrILes incoming boss tile."""
    def intro_text(self):
        """Description of Boss Warning Tile"""
        return """
        There's a chilling presence down your spine 4 tiles away from you...
        I wonder what it could be?
        Treasure? Glory?
        A game over?
        """


class BossTileR(MapTile):
    def __init__(self, x, y):
        self.a = 0
        self.d = 0
        self.enemy = enemies.King_Slime()
        alive_start = """
        You encounter the King Slime!
        It doesn't seem like a big threat.
        You can probably defeat it.
        """
        alive_attack = "King Slime attacks!"
        self.alive_text = [alive_start, alive_attack]
        dead_start = """
        You've defeated King Slime!
        That wasn't too bad was it?
        Ehh, not really yeah!
        Good! It gets worse.
        Oh.
        You can claim your loot.
        Just head East.
        """
        dead_return = "King Slime has been defeated."
        self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Intro message changes as the player attacks the enemy.
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        """
        Checks the enemy's current strength so it can respond to the player.
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
                print("The {} causes lethal damage. You perish in battle...".
                      format(self.enemy.name))
                sys.exit()


class BossLootR(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Slime_Barrier()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        What's this sticky stuff?
        Uh..Slime condensation. Also don't say stuff like that.
        Why not?
        Man you sure are innocent aren't you.
        There is a Slime Barrier in that goop.
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


class BossLootL(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Excalibrate()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        It's Arturia's blade!
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


class BossLootT(MapTile):
    """Position that contains items."""
    def __init__(self, x, y):
        """Items that are currently on the tile."""
        # Index for switching messages.
        self.i = 0
        self.name = "Items"
        self.inventory = [items.Cinderhulk()]

        super().__init__(x, y)

    def intro_text(self):
        """Description for the items tile."""
        # Description of the items tile.
        self.start_items = """
        Alright! an item tile!
        Let's see here...
        An estus flask? Well that seems familiar...
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


class BossTileL(MapTile):
    def __init__(self, x, y):
        self.a = 0
        self.d = 0
        self.enemy = enemies.Arturia()
        alive_start = """
        You encounter the King!
        Or is it the Queen?
        Well canonically...
        No. We're not getting into that.
        Aw.
        """
        alive_attack = "Arturia Swings their blade!"
        self.alive_text = [alive_start, alive_attack]
        dead_start = """
        You've defeated the... You've defeated Arturia!
        You really had to double take for that huh.
        Yes.
        """
        dead_return = "Arturia has been defeated."
        self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Intro message changes as the player attacks the enemy.
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
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
                print("The {} causes lethal damage. You perish in battle...".
                      format(self.enemy.name))
                sys.exit()


class BossTileT(MapTile):
    def __init__(self, x, y):
        self.a = 0
        self.d = 0
        self.enemy = enemies.Soul_of_Cinder()
        alive_start = """
        That guy is on fire.
        Yes he is.
        Also the name sounds familiar.
        What a coincidence.
        Where have I seen him before?
        No clue.
        """
        alive_attack = "Soul of Cinder slashes his fiery blade!"
        self.alive_text = [alive_start, alive_attack]
        dead_start = """
        You've defeated the man on fire!
        Wait, no I meant the Soul of Cinder.
        Congratulations.
        """
        dead_return = "Soul of Cinder has been extinguished..."
        self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Intro message changes as the player attacks the enemy.
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
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
                print("The {} causes lethal damage. You perish in battle...".
                      format(self.enemy.name))
                sys.exit()


class BossTileB(MapTile):
    def __init__(self, x, y):
        self.a = 0
        self.d = 0
        self.enemy = enemies.Manus_The_First_Hero()
        alive_start = """
        Frozen in terror
        I am unable to move
        This may be the end.
        """
        alive_attack = "Manus frenzies!"
        self.alive_text = [alive_start, alive_attack]
        dead_start = """
        Wait I seriously beat that thing?!
        Huh, I really didn't think you could.
        Congratulations!
        """
        dead_return = "The Fear disperses..."
        self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Intro message changes as the player attacks the enemy.
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
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
                print("The {} causes lethal damage. You perish in battle...".
                      format(self.enemy.name))
                sys.exit()


class OptionalTileR(MapTile):
    def __init__(self, x, y):
        self.a = 0
        self.d = 0
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
        You've defeated one of the Optional Bosses!
        Give yourself a pat on the back.
        Don't actually.
        But if you want to go ahead.
        Claim your prize by heading east.
        """
        dead_return = "Congratulations..."
        self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Intro message changes as the player attacks the enemy.
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        """
        Checks the enemy's current strength so it can respond to the player.
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
                print("The {} causes lethal damage. You perish in battle...".
                      format(self.enemy.name))
                sys.exit()


class OptionalTileL(MapTile):
    def __init__(self, x, y):
        self.a = 0
        self.d = 0
        # Optional Boss 100% spawns on this tile. (Hollow Knight)
        self.enemy = enemies.Beserkerlot()
        alive_start = """
        You encounter the Beserkerlot!
        A Mad Knight driven by insane loyalty.
        """
        alive_attack = "Berserklot rages!"
        self.alive_text = [alive_start, alive_attack]
        dead_start = """
        I feel bad for that knight.
        Going the majority of your life in a beserk state.
        Not being able to think for yourself.
        It's quite sad.
        You've defeated one of the Optional Bosses!
        Claim your prize by heading south.
        """
        dead_return = "Congratulations..."
        self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Intro message changes as the player attacks the enemy.
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        """
        Checks the enemy's current strength so it can respond to the player.
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
                print("The {} causes lethal damage. You perish in battle...".
                      format(self.enemy.name))
                sys.exit()


class OptionalTileT(MapTile):
    def __init__(self, x, y):
        self.a = 0
        self.d = 0
        # Optional Boss 100% spawns on this tile. (Hollow Knight)
        self.enemy = enemies.Gwyn_Upholder_of_Peace()
        alive_start = """
        It's the Guardian Knight.
        He spares none.
        Goodluck.
        """
        alive_attack = "Judgement Passes!"
        self.alive_text = [alive_start, alive_attack]
        dead_start = """
        You've interrupted the peace.
        For what?
        Loot?
        That's fair.
        You've defeated one of the Optional Bosses!
        Claim your prize by heading west.
        """
        dead_return = "Congratulations..."
        self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Intro message changes as the player attacks the enemy.
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        """
        Checks the enemy's current strength so it can respond to the player.
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
                print("The {} causes lethal damage. You perish in battle...".
                      format(self.enemy.name))
                sys.exit()


class EnemyTileR(MapTile):
    """Enemy position and messages"""
    def __init__(self, x, y):
        """Creates a random position for each enemy"""
        # Indices of j and k to switch out alive and dead messages.
        self.a = 0
        self.d = 0
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
            Man, I feel kinda bad...
            Don't be it's just a video game mob!
            What are you talking about?
            """
            dead_return = "Slime condensate floats on the ground..."
            self.dead_text = [dead_start, dead_return]

        # Goblin encounters are about 20%.
        elif r < 0.50 and r >= 0.30:
            self.enemy = enemies.Goblin()
            alive_start = """
            You encounter a Goblin!
            Are there any good goblins?
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
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        """
        Checks enemy current strength to respond to player's hp value.
        """
        if self.enemy.is_alive():
            # Game will continue to run as long as the player has hp.
            if player.hp > self.enemy.damage:
                player.hp -= self.enemy.damage
                print("The {} does {} damage. You are injured, {} HP remains.".
                      format(self.enemy.name, self.enemy.damage,
                             player.hp))
            # If the player runs out of hp, the game ends.
            elif player.hp <= self.enemy.damage:
                print("The {} causes lethal damage. You perish in battle...".
                      format(self.enemy.name))
                sys.exit()


class EnemyTileL(MapTile):
    """Enemy position and messages"""
    def __init__(self, x, y):
        """Creates a random position for each enemy"""
        # Indices of j and k to switch out alive and dead messages.
        self.a = 0
        self.d = 0
        # Generates a random number that spawns a certain enemy.
        r = random.random()
        # Bonehheel encounters are about 50%.
        if r < 0.30:
            self.enemy = enemies.Bonewheel()
            alive_start = """
            You encounter a Bonewheel Skeleton!
            "So it's a skeleton that's in a Wheel."
            "Yes."
            "It also rolls around and attacks you like that."
            "Yes."
            "That's kinda cool."
            """
            alive_attack = "The Bonehweel rolls at you!."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The Skeleton and its wheel falls apart.
            RIP Skeleton.
            """
            dead_return = "Bones and a Wheel are left on the ground."
            self.dead_text = [dead_start, dead_return]

        # Undead encounters are about 20%.
        elif r < 0.50 and r >= 0.30:
            self.enemy = enemies.Undead()
            alive_start = """
            You encounter an Undead!
            It doesn't smell very nice.
            """
            alive_attack = "The Undead attacks!"
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The Undead..dies? Yeah it dies.
            Wait can Undeads even die?
            "Beats me"
            """
            dead_return = "The Undead has been defeated."
            self.dead_text = [dead_start, dead_return]

        # Sun Knight encounters are about 20%.
        elif r < 0.80 and r >= 0.60:
            self.enemy = enemies.Sun_Knight()
            alive_start = """
            You encounter a Sun Knight!
            At least, I think it is.
            He's really bright, can't really see anything at all.
            """
            alive_attack = "Sun Knight shoots a Beam of Light!"
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The Sun Knight fades into darkness.
            "I guess you can say his light has been darkened. Heh."
            "stop."
            """
            dead_return = "The Sun Knight has been defeated."
            self.dead_text = [dead_start, dead_return]

        else:
            self.enemy = enemies.Lancer()
            alive_start = """
            You encounter Lancer.
            Why's he in a blue bodysuit?
            """
            alive_attack = "Lancer throws his Lance!"
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            LANCER HAS BEEN KILLED!
            YOU MONSTER!
            Well not really.
            Luckily he doesn't have guts.
            """
            dead_return = "Lancer died."
            self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message depending on enemy hp."""
        if self.enemy.is_alive():
            # After the player attacks, message switches.
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        """
        Checks enemy current strength to respond to player's hp value.
        """
        if self.enemy.is_alive():
            # Game will continue to run as long as the player has hp.
            if player.hp > self.enemy.damage:
                player.hp -= self.enemy.damage
                print("The {} does {} damage. You are injured, {} HP remains.".
                      format(self.enemy.name, self.enemy.damage,
                             player.hp))
            # If the player runs out of hp, the game ends.
            elif player.hp <= self.enemy.damage:
                print("The {} causes lethal damage. You perish in battle...".
                      format(self.enemy.name))
                sys.exit()


class EnemyTileT(MapTile):
    """Enemy position and messages"""
    def __init__(self, x, y):
        """Creates a random position for each enemy"""
        # Indices of j and k to switch out alive and dead messages.
        self.a = 0
        self.d = 0
        # Generates a random number that spawns a certain enemy.
        r = random.random()
        # Hunter encounters are about 50%.
        if r < 0.30:
            self.enemy = enemies.Hunter()
            alive_start = """
            You encounter a Hunter!
            "A hunter always watches where he steps."
            "That's a quote from somewhere isn't it."
            "no."
            """
            alive_attack = "The Slime attacks."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The Hunter has been Hunted.
            "That's funny."
            """
            dead_return = "The Hunter has been defeated."
            self.dead_text = [dead_start, dead_return]

        # Skrimisher encounters are about 20%.
        elif r < 0.50 and r >= 0.30:
            self.enemy = enemies.Skirmisher()
            alive_start = """
            You encounter a Skirmisher!
            "That guy's got a long stick."
            "It's a pike."
            "Oh....So a long POINTY stick."
            "..."
            """
            alive_attack = "The Skirmisher pokes you!"
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The Skimirsher just dies.
            """
            dead_return = "The Skirmisher has been defeated."
            self.dead_text = [dead_start, dead_return]

        # Great Wolf encounters are about 20%.
        elif r < 0.80 and r >= 0.60:
            self.enemy = enemies.Great_Wolf()
            alive_start = """
            A Great Wolf blocks your path.
            "Oh no what shall we do?"
            "Fight it. Duh."
            """
            alive_attack = "The Great Wolf howls.!"
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The Wolf howls in agony.
            "You're kind of a monster you know."
            "I had no other option!"
            "Yeah...."
            """
            dead_return = "The Great Wolf has been defeated."
            self.dead_text = [dead_start, dead_return]

        else:
            self.enemy = enemies.Giant()
            alive_start = """
            That's a giant.
            It's quite large.
            This room is quite cramped.
            """
            alive_attack = "The Giant throws a rock."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            The Giant disappears.
            Lucky you, you aren't cramped anymore.
            """
            dead_return = "The Giant has been defeated."
            self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message depending on enemy hp."""
        if self.enemy.is_alive():
            # After the player attacks, message switches.
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        """
        Checks enemy current strength to respond to player's hp value.
        """
        if self.enemy.is_alive():
            # Game will continue to run as long as the player has hp.
            if player.hp > self.enemy.damage:
                player.hp -= self.enemy.damage
                print("The {} does {} damage. You are injured, {} HP remains.".
                      format(self.enemy.name, self.enemy.damage,
                             player.hp))
            # If the player runs out of hp, the game ends.
            elif player.hp <= self.enemy.damage:
                print("The {} causes lethal damage. You perish in battle...".
                      format(self.enemy.name))
                sys.exit()


class EnemyTileB(MapTile):
    def __init__(self, x, y):
        self.a = 0
        self.d = 0
        # 100% Spawn rate for Vessel.
        self.enemy = enemies.Vessel()
        alive_start = """
        What...What are these?
        These are the souls of the condemned.
        Each passerby who has since passed.
        """
        alive_attack = "The Vessels Wail."
        self.alive_text = [alive_start, alive_attack]
        dead_start = """
        They curse...
        """
        dead_return = "Curse..."
        self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Intro message changes as the player attacks the enemy.
            if self.a == 0:
                self.a += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # Intro message changes when the player returns to the tile.
        # When there is a dead enemy, dead text plays.
        else:
            if self.d == 0:
                self.d += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]


floor_map = []


def tile_at(x, y):
    """Locates a certain tile at a coordinate."""
    if x < 0 or y < 0:
        return None
    try:
        return floor_map[y][x]
    except IndexError:
        return None


# Floor 1's map in abbreviations.
floor_dsl = """
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |BW|BT|SF|BR|LR|
|  |  |  |  |  |BT|  |  |SU|OT|BT|IT|ET|ET|  |  |  |  |GT|IR|BT|ER|GT|
|  |  |  |  |  |ET|IT|  |  |ET|GT|BT|IT|IT|  |  |  |  |ER|IR|BT|ER|IR|
|  |  |LT|BU|ET|IT|SF|BW|BT|GT|ET|IT|IT|ET|  |  |  |  |ER|ER|ER|IR|IR|
|  |  |  |  |  |ET|IT|  |  |BT|ET|ET|IT|BT|  |  |  |  |BT|ER|IR|ER|BT|
|  |  |  |  |  |BT|  |  |  |ET|ET|TM|BT|ET|  |  |  |  |BT|IR|RM|IR|ER|
|  |  |  |  |  |  |  |  |  |  |  |BT|  |  |  |  |  |  |  |  |BT|
|  |  |  |  |  |  |  |  |  |  |  |BT|  |  |  |  |  |  |  |  |BT|
|EL|IL|GT|IL|EL|  |  |  |  |BT|BT|TP|BT|BT|  |  |  |  |ER|IR|BT|BT|OR|SR|
|BT|IL|EL|BT|EL|  |  |  |  |BT|IT|IT|IT|BT|  |  |  |  |ER|BT|IR|ER|BT|
|EL|IL|IL|EL|LM|BT|BT|BT|BT|LP|SF|ST|MT|RP|BT|BT|BT|BT|RM|ER|ER|ER|BT|
|IL|EL|BT|IL|EL|  |  |  |  |BT|GT|GT|GT|BT|  |  |  |  |ER|GT|ER|GT|IR|
|OL|IL|EL|SF|EL|  |  |  |  |BT|BT|BP|BT|BT|  |  |  |  |IR|IR|ER|BT|BT|
|SL|  |GT|  |  |  |  |  |  |  |  |BT|
|  |  |BT|  |  |  |  |  |  |  |  |BT|
|EL|IT|LM|IL|EL|  |  |  |  |EB|BT|BM|EB|IB|  |  |  |BT|
|BT|EL|IT|EL|BT|  |  |  |  |BT|IB|EB|EB|EB|  |  |IB|EB|
|EL|IT|EL|IL|BT|  |  |  |  |EB|BT|IB|BT|EB|BT|BW|SF|BR|BL|AL|BU|BB|CH|
|BT|EL|EL|IL|BT|  |  |  |  |BT|BT|EB|EB|BT|  |  |IB|EB|
|EL|BT|BT|IL|IT|  |  |  |  |EB|IB|BT|BT|EB|  |  |  |BT|
|BT|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|BW|
|BT|
|SF|
|EL|
|BL|
|LL|
"""
# make different map tiles that display multiple maps and areas


def is_dsl_valid(dsl):
    """
    Check if game has only 1 Start, 1 Map Tile and one of each Path Tiles.
    """
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|MT|") == 0:
        return False
    if dsl.count("|RP|") == 0:
        return False
    if dsl.count("|LP|") == 0:
        return False
    if dsl.count("|TP|") == 0:
        return False
    if dsl.count("|BP|") == 0:
        return False
    if dsl.count("|RM|") == 0:
        return False
    if dsl.count("|TM|") == 0:
        return False
    if dsl.count("|BM|") == 0:
        return False
    if dsl.count("|LM|") == 0:
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
                  "CH": ChampionsTile,
                  "IR": ItemTileR,
                  "IT": ItemTileT,
                  "IL": ItemTileL,
                  "IB": ItemTileB,
                  "ER": EnemyTileR,
                  "ET": EnemyTileT,
                  "EB": EnemyTileB,
                  "EL": EnemyTileL,
                  "BT": BoringTile,
                  "MT": ViewMapTile,
                  "GT": GoldTile,
                  "BR": BossTileR,
                  "BL": BossTileL,
                  "BU": BossTileT,
                  "BB": BossTileB,
                  "OR": OptionalTileR,
                  "OL": OptionalTileL,
                  "OT": OptionalTileT,
                  "SL": SpecialLootL,
                  "SR": SpecialLootR,
                  "SU": SpecialLootT,
                  "AL": ArtoriasLoot,
                  "LL": BossLootL,
                  "LR": BossLootR,
                  "LT": BossLootT,
                  "SF": SafeRoomTile,
                  "RP": RightPath,
                  "LP": LeftPath,
                  "TP": TopPath,
                  "BP": BottomPath,
                  "BW": BossWarning,
                  "RM": RightMap,
                  "LM": LeftMap,
                  "TM": TopMap,
                  "BM": BotMap,
                  " ": None,
                  "  ": None}
# Initializes the Starting Tile.
start_tile_location = None


def parse_floor_dsl():
    """Floor 1 map considered a string and returned as a list."""
    dsl_lines = floor_dsl.splitlines()
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
        floor_map.append(row)
