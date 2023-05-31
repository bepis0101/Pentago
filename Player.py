#import MainMenu
import pygame
import Board
import Bot
import UpdateState


class UserInput:
    def __init__(self):
        pass
    # TODO

        
board = Board.Board()
board.setBlack(5, 1)
board.setWhite(3, 2)
window = UpdateState.Window(board)
game = UserInput(window)
game.main()