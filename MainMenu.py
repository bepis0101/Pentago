import pygame
import Window

class Button:
    pygame.font.init()
    font = pygame.font.SysFont('arial', 26, True)
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.button = pygame.Rect((self.pos[0], self.pos[1]), (300, 50))
        self.clicked = False
        
    
    def draw(self, screen):
        pos = pygame.mouse.get_pos()        
        action = False     
        if self.button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                action = True
        
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        pygame.draw.rect(screen, 'light blue', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark blue', self.button, 5, 5)
        text = self.font.render(self.text, True, 'black')
        screen.blit(text, (self.pos[0]+20, self.pos[1]+12))
        return action

class MainMenu:
    def __init__(self, screen):
        x, y = screen.get_size()
        self.exit_button = Button("EXIT", (x//2-150, y//2+75))
        self.multi_button = Button("MULTIPLAYER", (x//2-150, y//2))
        self.single_button = Button("SINGLEPLAYER", (x//2-150, y//2-75))
