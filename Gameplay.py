import Board
import Bot
import pygame
import UdpateState

class Gameplay:
    def __init__(self, board, main_menu):
        self.board = board
        self.main_menu = main_menu
    def main(self):
        clock = pygame.time.Clock()
        run = True
        main_menu = True
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw_game.drawWin()

        pygame.quit()