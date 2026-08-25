> Commit: User input parsing
> - The UI now hands user input to the parser
> - The parser splits the input by spaces and then checks the first word against a match statement
> - The UI now clears the input when it's submitted

> Commit: Fixed text output issues
> - The text element is now a multiline element so that it can scroll.
> - The box was too wide which is why the word wrapping was acting up

> Commit: Basic game UI layout
> - The game now has the main interface elements
> - This includes the user input, a submit button, the output log and the image display.
> - The image display is able to show multiple images on top of each other and the text output is able to show the backlog of multiple lines of text.
> - Currently the text output has problems with word-wrapping and I haven't tested if it can scroll on overflow.
> - It may need to be changed to a different element in the future.

> Commit: Basic classes and test window
> - Most classes have files and empty classes created
> - This is likely going to gain or lose some classes as I find out what I need
> - There is also a basic test window with nothing in it