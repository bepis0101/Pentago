import Window
import pygame

class State(Window.Window):
    def drawWin(self):
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
                if self.board.board[y][x] == 1:
                    self.WIN.blit(self.BLACK_BALL, (pos_x, pos_y))
                if self.board.board[y][x] == 2:
                    self.WIN.blit(self.WHITE_BALL, (pos_x, pos_y))

        pygame.display.update()
