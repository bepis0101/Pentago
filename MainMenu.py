import pygame
import Board
import Bot
import UpdateState

class Button:
    pygame.font.init()
    font = pygame.font.SysFont('arial', 26, True)
    def __init__(self, text, pos, screen):
        self.text = text
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (300, 50))
        self.screen = screen
    def draw(self):
        py_button = pygame.draw.rect(self.screen, 'light blue', self.button, 0, 5)
        pygame.draw.rect(self.screen, 'dark blue', self.button, 5, 5)
        text = self.font.render(self.text, True, 'black')
        self.screen.blit(text, (self.pos[0]+15, self.pos[1]+7))
    

class MainMenu:
    def __init__(self):
        pass
