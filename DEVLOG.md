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
