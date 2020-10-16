# Course: CS 30
# Period: 1
# Date Created: 20/10/14
# Date Modified: 20/10/16
# Name: Michael Nguyen
# Description: Items class for Soulsborne.


class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return "{} (+ {} Damage)".format(self.name, self.damage)


# Floor 1 Weapons
class Rapier(Weapon):
    def __init__(self):
        self.name = "Rapier"
        self.description = "A Slender Sword."
        self.damage = 10


class Broadsword(Weapon):
    def __init__(self):
        self.name = "Broadsword"
        self.description = "Slightly better than the Rapier?..."
        self.damage = 12


class Greatsword(Weapon):
    def __init__(self):
        self.name = "Greatsword"
        self.description = "A Large Sword, quite powerful in fact."
        self.damage = 15


class Hollow_Blade(Weapon):
    def __init__(self):
        self.name = "Hollow Blade"
        self.description = "A sword given to all the Knights of Arturia."
        self.damage = 20


# Floor 2 weapons
class Zombie_Arm(Weapon):
    def __init__(self):
        self.name = "Zombie Arm"
        self.description = "What? Why? Why would you use this thing?"
        self.damage = 5


class Secace(Weapon):
    def __init__(self):
        self.name = "Secace"
        self.description = "A mad knight's sword from a distant land..."
        self.damage = 27


class Excalibrate(Weapon):
    def __init__(self):
        self.name = "Excalibrate"
        self.description = "From the challenges of The Dungeonmaster..."
        self.damage = 30


# Secret Floor Weapon
class Abysswalker(Weapon):
    def __init__(self):
        self.name = "Abysswalker"
        self.description = "From beyond and back."
        self.damage = 45


class Armour:
    def __init__(self):
        raise NotImplementedError("Do not create raw Protection objects.")

    def __str__(self):
        return "{} (- {} Damage)".format(self.name, self.protection)


class Basic_Shield(Armour):
    def __init__(self):
        self.name = "Basic Shield"
        self.description = "A basic shield for blocking, nothing special."
        self.protection = 10


class Hollow_Shield(Armour):
    def __init__(self):
        self.name = "Hollow Shield"
        self.description = "A shield given out to the knights of Arturia."
        self.protection = 15


class Skeleton_Skull(Armour):
    def __init__(self):
        self.name = "Skeleton Skull"
        self.description = "You really like picking up dead things huh."
        self.protection = 1


class Galahad_Shield(Armour):
    def __init__(self):
        self.name = "Galahad's Shield"
        self.description = "A pure shield."
        self.protection = 30


class Abysswalker_Arm(Armour):
    def __init__(self):
        self.name = "Abysswalker's Arm"
        self.description = "The Left Arm Armour of Artorias, "


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+ {} HP)".format(self.name, self.healing)


class Potion(Consumable):
    def __init__(self):
        self.name = "Potion"
        self.description = "Potion for healing purposes."
        self.healing = 10


class Great_Potion(Consumable):
    def __init__(self):
        self.name = "Great Potion"
        self.description = "Greater healing from this potion."
        self.healing = 15


class Estus(Consumable):
    def __init__(self):
        self.name = "Estus Flask"
        self.description = "Healing potion...seems familiar..."
        self.healing = 20


class Humanity(Consumable):
    def __init__(self):
        self.name = "Humanity"
        self.description = "Restores full hp...is this a soul of a life?!"
        self.healing = 99


class Currency:
    def __init__(self):
        raise NotImplementedError("Do no create raw Currency objects/")


class Gold_Coins(Currency):
    def __init__(self):
        self.name = "Gold Coins"
        self.description = "Coins for bartering"
        self.money = 10
