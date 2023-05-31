import MainMenu
import pygame
import Board
import Bot
import UpdateState


class Player:
    def __init__(self, board):
        self.board = board
    def getInput(self):
        mx, my = pygame.mouse.get_pos()
        for y in range(6):
            for x in range(6):
                if mx >= 50+x*100 and mx < 150+x*100:
                    if my >= 50+y*100 and my < 150+y*100:
                        return x, y
        return 0, 0
    

        

        
board = Board.Board()
board.setBlack(5, 1)
board.setWhite(3, 2)
window = UpdateState.Window(board)
game = Player(window)
game.main()