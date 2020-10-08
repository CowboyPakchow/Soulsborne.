# Course: CS 30
# Period: 1
# Date Created: 20/09/21
# Date Modified: 20/10/06
# Name: Michael Nguyen
# Description: SimpleMenu updated for Continuous Gameplay.



print("Valid actions for current location:")
print("Type in 'quit' to quit out of the game.")

# Looping and printing list of directions.
print("Which direction would you like to move in?: ")
directions = ['* North', '* South', '* East', '* West']
for pole in directions:
    print(pole)

# Looping and printing list of actions.
print("\nYour move, what is your action?: ")
actions = ['* Attack', '* Defend', '* Heal', '* Wander', '* Quit']
for action in actions:
    print(action)

# Various actions the player can take. Actions are looped.
# Added an option to quit the game using an active flag.
active = True
while active:
    prompt = input("\nAction: ").lower().strip()

    if prompt == 'quit':
        active = False

    if prompt == 'north':
        print("You move North.")
    elif prompt == 'south':
        print("You move South.")
    elif prompt == 'east':
        print("You move East.")
    elif prompt == 'west':
        print("You move West.")
    elif prompt == 'attack':
        print("You attack the enemy.")
    elif prompt == 'defend':
        print("You stand your ground and defend.")
    elif prompt == 'heal':
        print("You heal the damage taken.")
    elif prompt == 'wander':
        print("You wander and explore around.")
    elif prompt == 'quit':
        print("You have quit the game.")
    else:
        print("That is an invalid action.")
