import Board
import random

class Bot:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def moveOfBot(self):
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        while self.board.checkFree(x, y) == False:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
        
        if self.color == 1:
            self.board.setBlack(x, y)
        else:
            self.board.setWhite(x, y)
        
        if self.board.count() >= 4:
            which_board = random.randint(0, 3)
        else:
            if y > 2:
                which_board = x//3 + 2
            else:
                which_board = x//3

        side = random.randint(0, 1)
        if side:
            self.board.turnLeft(which_board)
        else:
            self.board.turnLeft(which_board)

        return self.board