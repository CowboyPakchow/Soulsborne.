# Course: CS 30
# Period: 1
# Date Created: 20/10/14
# Date Modified: 20/10/26
# Name: Michael Nguyen
# Description: Items class for Soulsborne.


class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return "{} (+ {} Damage)".format(self.name, self.damage)


# Right Path Weapons.
class Rapier(Weapon):
    def __init__(self):
        self.name = "Rapier"
        self.description = "A Slender Sword."
        self.damage = 10
        self.value = 10


class Broadsword(Weapon):
    def __init__(self):
        self.name = "Broadsword"
        self.description = "Slightly better than the Rapier?..."
        self.damage = 15
        self.value = 15


class Greatsword(Weapon):
    def __init__(self):
        self.name = "Greatsword"
        self.description = "A Large Sword, quite powerful in fact."
        self.damage = 20
        self.value = 20


class Hollow_Blade(Weapon):
    def __init__(self):
        self.name = "Hollow Blade"
        self.description = "A sword given to all the Knights of Arturia."
        self.damage = 25
        self.value = 30


# Left Path Weapons.
class Zombie_Arm(Weapon):
    def __init__(self):
        self.name = "Zombie Arm"
        self.description = "What? Why? Why would you use this thing?"
        self.damage = 5
        self.value = 1


class Secace(Weapon):
    def __init__(self):
        self.name = "Secace"
        self.description = "A mad knight's sword from a distant land..."
        self.damage = 35
        self.value = 60


class Excalibrate(Weapon):
    def __init__(self):
        self.name = "Excalibrate"
        self.description = "From the challenges of The Dungeonmaster..."
        self.damage = 45
        self.value = 90


# Top Path Weapons
class Cinderhulk(Weapon):
    def __init__(self):
        self.name = "Cinderhulk"
        self.description = "The Flame has never been extinguished."
        self.damage = 65
        self.value = 120


# Bottom Path Weapons.
class Abysswalker(Weapon):
    def __init__(self):
        self.name = "Abysswalker"
        self.description = "From beyond and back."
        self.damage = 80
        self.value = 170


class Armour:
    def __init__(self):
        raise NotImplementedError("Do not create raw Protection objects.")

    def __str__(self):
        return "{} (- {} Damage)".format(self.name, self.protection)


# Right Path Armour.
class Basic_Shield(Armour):
    def __init__(self):
        self.name = "Basic Shield"
        self.description = "A basic shield for blocking, nothing special."
        self.protection = 15
        self.value = 10


class Hollow_Shield(Armour):
    def __init__(self):
        self.name = "Hollow Shield"
        self.description = "A shield given out to the knights of Arturia."
        self.protection = 25
        self.value = 25


class Slime_Barrier(Armour):
    def __init__(self):
        self.name = "Slime Barrier"
        self.description = "A Protective Coating."
        self.protection = 35
        self.value = 50


# Left Path Armour.
class Galahad_Shield(Armour):
    def __init__(self):
        self.name = "Galahad's Shield"
        self.description = "A pure shield."
        self.protection = 50
        self.value = 100


# Top Path Armour.
class Guardians_Safeguard(Armour):
    def __init__(self):
        self.name = "Guardian's Safeguard"
        self.description = "The Guardian's Will"
        self.protection = 70
        self.value = 150


# Bottom Path Armour.
class Abysswalker_Arm(Armour):
    def __init__(self):
        self.name = "Abysswalker's Arm"
        self.description = "The Left Arm Armour of Artorias, the ancient."
        self.protection = 90
        self.value = 200


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
        self.value = 20


class Great_Potion(Consumable):
    def __init__(self):
        self.name = "Great Potion"
        self.description = "Greater healing from this potion."
        self.healing = 15
        self.value = 40


class Estus(Consumable):
    def __init__(self):
        self.name = "Estus Flask"
        self.description = "Healing potion...seems familiar..."
        self.healing = 25
        self.value = 60


class Humanity(Consumable):
    def __init__(self):
        self.name = "Humanity"
        self.description = "Restores full hp...is this a soul of a life?!"
        self.healing = 99
        self.value = 250
