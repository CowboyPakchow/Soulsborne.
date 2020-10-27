# RPG: Soulsborne Changelog

**vPrerelease**
- Game is currently in a prerelease state.
- Added a README File
- Added a Changelog
- Added main.py file that lists current monsters, special monsters and weapons that are planned for the game (numerical list)
- Added Pseudocode.py that describes plans for creating the game
- Removed Pseudocode.py (Different repository)
- Updated main.py and README files
- Updated main.py file by adding Dictionaries for characters, locations and inventory
- Added a SimpleMenu
- Modified SimpleMenu to add quit option
   - Deleted Nested Dictionary to shorten code with only Loops
- Added a list of enemies to Soulsborne.
- Added a randomized map for each floor.
- Added player character inventory with starting items in it.
- Added a character file that will list Hero's attributes (not yet implemented)
- Moved nested dictionary functions from main to dictionary file.
- Imported playerinventory, SimpleMenu and map to main file.


**v1.0**
- Game is in a playable state.
- Removed Armour.py and Weapons.py in place of everything in items.py
- Removed character.py in place of player.py
- Removed SimpleMenu.py in place of a better menu system.
- Removed map.py in place of floor 1 map.
- Modified certain enemy hp and damage values.
- Modified Weapon names.
- Modified Weapon damages.
- Currently only 1 basic shield is available.
- Item tiles only contain potions as of now.

**v1.01** 
- Enemies Hp and Attack altered for slightly easier experience in early game.
  - That being said, enemy in harder rooms are slightly harder.
- Different rooms have different enemies.
- Fixed a bug that did not allow the player to attack in optional boss rooms.
- Fixed a bug that did not display the correct tiles on the map.
- Raise Player HP cap to 60.
- Buffed some Weapons and armour. 

**v1.1**
- Map Overhaul has been implemented.
- Bosses for each Boss tile have been implemented.
- Optional Bosses for each Optional tile have been implemented.
- Loot for Bosses & Optional Bosses have been implemented.
- New Weapons and Armour from Loot.
- Ending to Game has been implemented.

**v1.2**
- Merchant added to Safe Rooms.
- Gold Tiles have been implemented.




**Upcoming/Planned**
- ~~Currently Boss of the first floor planned for version 1.1~~ *X*
  - ~~Game ends after reaching Boss Tile.~~ *X*
- ~~Merchants that appear in Safe Rooms are planned for version 1.2~~ **✓**
- ~~Floor 2 possibly planned for version 1.2~~ *X*
- ~~Gold Tiles are planned for 1.2~~ **✓**
- ~~More armour items are planned for 1.1~~ **✓**
- ~~More weapons are planned for 1.1~~ **✓**
- ~~Complete overhaul of the map for 1.1~~ **✓**
- ~~Ending to the game planned for **1.1** or 1.2~~ **✓**
- ~~More Bosses & Optional bosses for 1.1~~ **✓**
- ~~Loot for Bosses & Optional Bosses for 1.1~~ **✓**
- Alpha Testing Underway.
- Beta Testing Soon.

**Bugs**
- ~~Unable to sell to Merchant with >100 Value items~~ **Fixed** Increased Merchant gold.
- ~~Map and actual tiles not matched~~ **Fixed** Added | | to act as empty spaces.
- ~~Items not displaying any value or desc.~~ **Fixed** Added () for inventory items.
- ~~Error with Gold Tiles.~~ **Fixed** Some tiles listed as GL and not GT
- ~~Bug where merchant inventory did not update after buying item~~ **Fixed**