from game import Game
from input_parser import Parser
from gui import GUI

if __name__ == '__main__':
   game = Game()
   parser = Parser(game)
   gui = GUI(game)
   gui.run_game(parser, gui.window)
