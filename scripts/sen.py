from game import Game
from gui import GUI
from input_parser import Parser

if __name__ == '__main__':
   game = Game()
   parser = Parser()
   gui = GUI()
   gui.run_game(parser, gui.window)
