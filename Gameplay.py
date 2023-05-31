import Board
import Bot
import pygame
import UpdateState

class Gameplay:
    def __init__(self, board, main_menu):
        self.board = board
        self.main_menu = main_menu
    
    def singlePlayer(self, player):
        clock = pygame.time.Clock()
        run = True
        clicked = False
        main_menu = True

        while run:
            clock.tick(self.FPS)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    clicked = False


            self.draw_game.drawWin()

        pygame.quit()