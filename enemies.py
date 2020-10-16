# Course: CS 30
# Period: 1
# Date Created: 20/10/09
# Date Modified: 20/10/16
# Name: Michael Nguyen
# Description: Enemies Classes in Soulsborne.


class Enemy():
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

# Floor 1 Enemies


# Slime enemy detailing its hp and damage.
class Slime(Enemy):
    def __init__(self):
        self.name = "Slime"
        self.hp = 10
        self.damage = 5


# Goblin enemy detailing its hp and damage.
class Goblin(Enemy):
    def __init__(self):
        self.name = "Goblin"
        self.hp = 15
        self.damage = 8


# Lizard enemy detialing its hp and damage.
class Lizard(Enemy):
    def __init__(self):
        self.name = "Lizard"
        self.hp = 15
        self.damage = 5


class Skeleton(Enemy):
    def __init__(self):
        self.name = "Skeleton"
        self.hp = 10
        self.damage = 5


# Hollow Knight optional boss detailing its hp and damage.
class Hollow_Knight(Enemy):
    def __init__(self):
        self.name = "Hollow Knight"
        self.description = "The Wandering Knight who since lost his name..."
        self.hp = 25
        self.damage = 13


# King Slime boss detailing its hp and damage.
class King_Slime(Enemy):
    def __init__(self):
        self.name = "King Slime"
        self.description = "This is the King of all Slimes!"
        self.hp = 20
        self.damage = 10

# Floor 2 Enemies


# Skeleton enemy detailing its hp and damage.
class Bonewheel(Enemy):
    def __init__(self):
        self.name = "Bonewheel Skeleton"
        self.hp = 20
        self.damage = 15


# Undead enemy detailing its hp and damage.
class Undead(Enemy):
    def __init__(self):
        self.name = "Undead Zombie"
        self.hp = 5
        self.damage = 30


# Troll enemy detailing its hp and damage.
class Troll(Enemy):
    def __init__(self):
        self.name = "Troll"
        self.hp = 25
        self.damage = 15


# Berserkerlot optional boss detailing its hp and damage.
class Beserkerlot(Enemy):
    def __init__(self):
        self.name = "Pinwheel"
        self.description = "A Knight that has lost all worldly desires..."
        self.hp = 45
        self.damage = 25


# Arturia boss detailing its hp and damage.
class Arturia(Enemy):
    def __init__(self):
        self.name = "King Arturia"
        self.description = "The King is no exception to Absurdity."
        self.hp = 65
        self.damage = 25

# Floor 3 Enemies


# Hunter enemy detailing its hp and damage.
class Hunter(Enemy):
    def __init__(self):
        self.name = "Hunter"
        self.hp = 35
        self.damage = 20


# Skirmisher enemy detailing its hp and damage.
class Skirmisher(Enemy):
    def __init__(self):
        self.name = "Skirmisher"
        self.hp = 40
        self.damage = 25


# Great Wolf enemy detailing its hp and damage.
class Great_Wolf(Enemy):
    def __init__(self):
        self.name = "Great Wolf"
        self.hp = 30
        self.damage = 30


# Gwyn optional boss detailing its hp and damage.
class Gwyn_Upholder_of_Peace(Enemy):
    def __init__(self):
        self.name = "Gwyn, Upholder of Peace"
        self.description = "'You dare to disturb the everlasting peace?!'"
        self.hp = 55
        self.damage = 30


# Soul of Cinder "final" boss detailing its hp and damage.
class Soul_of_Cinder(Enemy):
    def __init__(self):
        self.name = "Soul of Cinder"
        self.description = "The End of your Journey is nigh."
        self.hp = 70
        self.damage = 35

# Secret Floor Enemies


# Vessel enemy detailing its hp and damage.
class Vessel(Enemy):
    def __init__(self):
        self.name = "Vessel"
        self.description = "The Souls of the condemned served as vessels."
        self.hp = 5
        self.damage = 0


# King Manus optional secret boss detailing its hp and damage.
class King_Manus_The_First_Hero(Enemy):
    def __init__(self):
        self.name = "King Manus, The First Hero"
        self.description = "None have survived Judgement."
        self.hp = 99
        self.damage = 50


# The Vessel secret final boss detailing its hp and damage.
class The_Holy_Grail(Enemy):
    def __init__(self):
        self.name = "The Holy Grail"
        self.description = "The Holy Grail upholding the entire balance."
        self.hp = 1
        self.damage = 0
