import pygame
import Board

class Player:
    def __init__(self, board):
        self.board = board
    def getBallInput(self):
        mx, my = pygame.mouse.get_pos()
        for y in range(6):
            for x in range(6):
                if mx >= 50+x*100 and mx < 150+x*100:
                    if my >= 50+y*100 and my < 150+y*100:
                        coords = (x, y)
                        return coords
        coords = (-1, -1)
        return coords
    
    
    def getBoardInput(self):
        mx, my = pygame.mouse.get_pos()
        for y in range(2):
            for x in range(2):
                if mx >= x*350 and mx < (x*350)+350:
                    if my >= y*350 and my < (y*350)+350:
                        coords = (x, y)
                        return coords
        coords = (-1, -1)
        return coords