import pygame
import Window
import Board

class Button:
    pygame.font.init()
    font = pygame.font.SysFont('arial', 26, True)
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (300, 50))
        
    
    def draw(self, screen):
        pygame.draw.rect(screen, 'light blue', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark blue', self.button, 5, 5)
        text = self.font.render(self.text, True, 'black')
        screen.blit(text, (self.pos[0]+100, self.pos[1]))
    

class MainMenu:
    def __init__(self, screen):
        pass
    #     self.screen = screen
    #     self.exit_button = 
    # def display(self):


        

# screen = pygame.display.set_mode((700, 700))
# pygame.display.set_caption("Button test")
# button1 = Button("QUIT", (200, 325))

# run = True
# while run:
#     screen.fill('light blue')
#     button1.draw(screen)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     pygame.display.update()
