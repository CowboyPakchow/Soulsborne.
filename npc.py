# Course: CS 30
# Period: 1
# Date Created: 20/10/14
# Date Modified: 20/10/26
# Name: Michael Nguyen
# Description: NPC class for Soulsborne.

import items


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.Name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Merchant"
        self.gold = 1000
        self.inventory = [items.Estus(), items.Humanity(),
                          items.Greatsword(),
                          items.Broadsword(), items.Great_Potion(),
                          items.Potion(),
                          items.Potion(), items.Great_Potion(),
                          items.Great_Potion(), items.Great_Potion(),
                          items.Great_Potion(),
                          items.Potion(),
                          items.Potion(), items.Great_Potion(), items.Potion()]
