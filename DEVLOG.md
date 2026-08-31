> Commit: GUI display
>
> - Changed the GUI class so that it clears and redraws the scene whenever a command is parsed
> - The GUI class now has a reference to the game to get image paths
> - Enemy sprites are now centered on the screen, this may not work for all of them so I may need to add a position value in the enemy class
> - Apparently I miss-spelled most of the sprite paths
> - I also can't tell east from west apparently

> Commit: Combat Tweaks
>
> - Resets the player's strength when enemy is defeated
> - The player now starts with the correct stats
> - Enemies should now be able to attack in retailation to player actions
> - Damage calculation should be correct
> - This code probably isn't ideal, but it works without issues and shouldn't be a problem later

> Commit: Combat
>
> - I have made a combat class that takes a player and enemy, this currently has a function to show the current battle state and an enemy defeated function
> - the combat class will be created when the player enters a room with a living enemy
> - The game class will be the ones responsible for managing the game state
> - The game class has a function that checks if there is a valid combat scenario and makes the current game state either combat or the room depending on the result
> - The attack command now does a dummy output
> - Put in the first enemy of the game as a test
> - Currently combat is one sided and doesn't handle modifiers but it works enough

> Commit: Item spawning and usage
>
> - The use command uses an adjusted version of the drop code
> - I'm changing the use and equip commands to both just find the item in the inventory and call a use command on the item. Each item will handle its own interaction and return the relevant string to the input handler.
> - Added in all of the items to the map. I'll add keys to doors once I get item usage working.
> - Items use a dictionary so that they can be referenced by name.
> - Multiple of one item can be added to the world.
> - I have also created a list of buffs. This is only 2 items currently
> - It might be better to remove the name value from the items and use their dictionary keys instead
> - I have realised that it would be better to create the items directly in the room's item list rather than as seperate objects loaded in
> - Buffs are responsible for changing status. Consumables just call theis method
> - The status now stores stats in a dictionary for easier access by buffs
> - Weapons and shield now take a status value when created and change the status's weapon or shield when used
> - Weapon and shield now display in the status report, their name string has to handled before the string is printed to handle None values

> Commit: Map layout
>
> - Set up basically the entire game world in game.py
> - The rooms use a dictionary with the room name as the key, so it may be better to remove the name value from the room in future
> - Doors are kept in a list, I could probably use this instead of putting doors in rooms, alternatively, for now I am going to make an automated process to load the doors from the two lists
> - Initially, the doors would attach and appear correctly but the directions could not be moved in, this is the result of the user input being lowercased but the door direction being the original capitalised string. I am temporarily fixing this by capitalising the user input instead of making it lowercase
> - I have found that ther movement code has an issue where it doesn't keep looking for doors if the first one with a matching string is pointing to the current room. I have fixed this by swapping the return statement with a continue statement

> Commit: Sen switching
>
> - The player can call the sen command with a valid element after
> - If the player doesn't give a valid element the game will list the valid ones
> - The game class stores a list of sen elements and then adds the advantages once all elements have been created
> - I initially forgot to write the name of the sen element instead of just the object
> - The player now starts with their sen set to fire

> Commit: Status Viewing
>
> - status.py now contains a status class which tracks the player's health, current sen, and strength
> - The player class now has a status class
> - Sending the status command will show all of the values in the player's status class

> Commit: Inventory Management
>
> - The pickup command now calls the invenrory's add item function
> - Calling the inventory command lists each item in the inventory's items, similarly to search
> - Rooms can also add and remove items. Probably not ideal but it works.
> - Dropping an item checks for the item the same way I have the last 5 times and then adds it to the current room and removes it from the inventory, basically the reverse of picking up
> - I am also now indenting any list item (things starting with -)

> Commit: Picking up items
>
> - GUI text input now focuses on start
> - When the player picks up an item, the game combines any word after pickup with spaces between
> - It then takes this and compares it to each item in the room until one matches
> - This does mean that if the player inputs to pick up a correct item but then adds a second word, it will fail

> Commit: Searching for items
>
> - This basically uses the same code as the door search
> - I also decided to make enter also work for GUI input

> Commit: Door finding and fixed movement
>
> - Changed UI scaling again, FreeSimpleGUI seems to have issues with different screen sizes
> - Added missing items value on inventory call in door class
> - Added some basic inventory item adding/removing functions. Not sure if these are really super necessary since they're only one line.
> - I have come to the conclusion that the "use", "equip" and "unlock" actions all do the same thing but require specific types of item to work. They could probably be merged into one action which works on all pickups.
> - Made a second room to properly test movement and other functions which need two rooms
> - You can now list the doors in a room. This iterates over all doors attached to the room and checks for the direction which isn't the current room
> - Turns out my movement function didn't work so now it handles the output message entirely through the parser and the logic is on the room.
> - It either returns the room object or None. The parser then figures out what to do from there and updates the current room

> Commit: Unlocking doors
>
> - Doors now store a lock state
> - Doors have a function to unlock themselves
> - When the input parser recieves the unlock command, it goes through each door in the room and checks if it has the given direction as an option. It then checks if the room that direction goes to is the current room to avoid any weirdness
> - Resized window to fit different screen

> Commit: I/O tweaks
>
> - Output messages are now returned up the process tree to the GUI output box
> - Invalid commands now return a message
> - User input is now stripped before parsing
> - Help command now returns a list of commands and their functions

> Commit: Player movement
>
> - Doors now take both a direction name and direction room
> - When the player moves in a direction, the name they give is passed to the room which checks if a door has that direction
> - There might be some issues with moving in the same direction twice through different rooms

> Commit: User input parsing
>
> - The UI now hands user input to the parser
> - The parser splits the input by spaces and then checks the first word against a match statement
> - The UI now clears the input when it's submitted

> Commit: Fixed text output issues
>
> - The text element is now a multiline element so that it can scroll.
> - The box was too wide which is why the word wrapping was acting up

> Commit: Basic game UI layout
>
> - The game now has the main interface elements
> - This includes the user input, a submit button, the output log and the image display.
> - The image display is able to show multiple images on top of each other and the text output is able to show the backlog of multiple lines of text.
> - Currently the text output has problems with word-wrapping and I haven't tested if it can scroll on overflow.
> - It may need to be changed to a different element in the future.

> Commit: Basic classes and test window
>
> - Most classes have files and empty classes created
> - This is likely going to gain or lose some classes as I find out what I need
> - There is also a basic test window with nothing in it
