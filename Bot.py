import Board
import random

class Bot:
    def __init__(self, color):
        self.color = color

    def moveOfBot(self, board):
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        while board.checkFree(x, y) == False:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
        
        if self.color == 1:
            board.setBlack(x, y)
        else:
            board.setWhite(x, y)

        return board