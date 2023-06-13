import MainMenu
import pygame
import Board
import Bot
import UpdateState


class Player:
    def __init__(self, board):
        self.board = board
    def getBallInput(self):
        mx, my = pygame.mouse.get_pos()
        for y in range(6):
            for x in range(6):
                if mx >= 50+x*100 and mx < 150+x*100:
                    if my >= 50+y*100 and my < 150+y*100:
                        return x, y
        return -1, -1
    
    def getBoardInput(self):
        mx, my = pygame.mouse.get_pos()
        for y in range(2):
            for x in range(2):
                if mx >= x*350 and mx < (x*350)+350:
                    if my >= y*350 and my < (y*350)+350:
                        return x, y
        return -1, -1
    
    def turn(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return 1
        if keys[pygame.K_RIGHT]:
            return 0
        else:
            return -1