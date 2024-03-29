import Window
import pygame
import os

class State(Window.Window):
    WHITE_BALL = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ball_blue.png')), (100, 100))
    BLACK_BALL = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ball_black.png')), (100, 100))
    def __init__(self):
        super().__init__()
    def drawWin(self, board):
        self.WIN.fill(self.WHITE)
        self.WIN.blit(self.BG, (50, 50)) 
        self.WIN.blit(self.BOARD_PNG, (50, 50))
        self.WIN.blit(self.BOARD_PNG, (350, 50))
        self.WIN.blit(self.BOARD_PNG, (350, 350))
        self.WIN.blit(self.BOARD_PNG, (50, 350))
        for y in range(6):
            for x in range(6):
                pos_x = 50+x*100 
                pos_y = 50+y*100 
                if board.board[y][x] == 1:
                    self.WIN.blit(self.BLACK_BALL, (pos_x, pos_y))
                if board.board[y][x] == 2:
                    self.WIN.blit(self.WHITE_BALL, (pos_x, pos_y))

        pygame.display.update()
