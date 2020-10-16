# Creating a dictionary of the Hero's items in their inventory.
print("Hero's Inventory:")
print("\n")
inventory = {"Hero": {"Long Sword": 
                      {"damage": 10, 
                      "protection": 0,
                      "description": "A standard sword."},
                      "Basic Shield": 
                      {"damage": 0, 
                      "protection": 10,
                      "description": "A shield for blocking."},
                      "Gold Coins": 
                      {"damage": 0, 
                      "protection": 0,
                      "description": "Currency for bartering."},
                      "Potion":
                      {"damage": 0,
                      "protection": 0,
                      "description": "Item for healing.",
                      "Healing": 10}} 
                      }


def player_inventory(player, inventory):
    """Defining and running Hero Inventory."""
    armour = []
    weapons = []
    items = []
    for item in inventory[player]:
        damage = inventory[player][item]["damage"]
        protection = inventory[player][item]["protection"]
        description = inventory[player][item]["description"]
        Healing = inventory[player][item]["Healing"]
        print(f"{player}'s {item} - {description}")
        print(f"* Damage: {damage}")
        print(f"* Protection: {protection}")
        print(f"* Healing: {Healing}")
        if protection != 0 and damage == 0:
            armour.append(item)
        elif damage != 0 and protection == 0:
            weapons.append(item)
        elif damage == 0 and protection == 0:
            items.append(item)
    return armour, weapons, items

player_inventory("Hero", inventory)
