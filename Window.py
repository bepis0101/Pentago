import pygame
import os

class Window:
    HEIGHT = 700
    WIDTH  = 700
    WHITE = (255, 255, 255)
    BG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background.png')), (600, 600))
    BOARD_PNG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'balls.png')), (300, 300))
    
    def __init__(self, board):
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pentago")
        self.board = board
    

