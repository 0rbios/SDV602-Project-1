from game import Game
from input_parser import Parser
from gui import GUI
from headless import headless_path

# Tells the game wether to use the GUI or run an automated test
HEADLESS = False

# Checks the given index of the headless path array and runs the corresponding command
def action(action_index):
	if parser.game.combat:
		print(f"\n::attack::")
		print(f"> {parser.parse_input("attack")}")
		action(action_index)
	else:
		if action_index == len(headless_path):
			print("Headless run completed")
			return
		print(f"\n::{headless_path[action_index]}::")
		print(f"> {parser.parse_input(headless_path[action_index])}")
		action(action_index + 1)

if __name__ == '__main__':
	game = Game()
	parser = Parser(game)
   
	if not HEADLESS:
		gui = GUI(game)
		gui.run_game(parser, gui.window)

	if HEADLESS:
		action(0)