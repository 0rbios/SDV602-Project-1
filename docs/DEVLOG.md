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
