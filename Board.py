import copy
class Board:
    rows = 6
    columns = 6
    def __init__(self): ## 6x6 board 
        self.board = [[0 for y in range(self.columns)] for x in range(self.rows)]
    
    def __str__(self): ## for debug
        s = ""
        for i in range(self.rows):
            s += f"{self.board[i]}\n"
        return s
    
    def checkFree(self, x, y):
        return self.board[y][x] == 0

    def setBlack(self, x, y):
        self.board[y][x] = 1

    def setWhite(self, x, y):
        self.board[y][x] = 2

    def turnRight(self, which): ## 3x right --> turn left
        temp = copy.deepcopy(self.board)
        # 0 --> top left board
        # 1 --> top right board
        # 2 --> bottom left board
        # 3 --> bottom right board
        
        if(which == 0):
            for y in range(self.rows//2):
                for x in range(self.columns//2):
                    temp[x][2-y] = self.board[y][x]
        elif(which == 1):
            for x in range(self.rows//2):
                for y in range(self.columns//2):
                    temp[x][5-y] = self.board[y][x+3]
        elif(which == 2):
            for x in range(self.rows//2):
                for y in range(self.columns//2):
                    temp[x+3][2-y] = self.board[y+3][x]
        elif(which == 3):
            for y in range(self.rows//2):
                for x in range(self.columns//2):
                    temp[x+3][5-y] = self.board[y+3][x+3]
        self.board = temp

    def turnLeft(self, which):
        for _ in range(3):
            self.turnRight(which)

    def checkVertical(self):
        for x in range(self.rows):
            for y in range(2):
                check = self.board[y][x]
                for i in range(5):
                    if self.board[y+i][x] != check:
                        check = 0
                        break
                if check != 0:
                    return check
        return 0
    
    def checkHorizontal(self):
        for y in range(self.columns):
            for x in range(2):
                check = self.board[y][x]
                for i in range(5):
                    if self.board[y][x+i] != check:
                        check = 0
                        break
                if check != 0:
                    return check
        return 0
    
    def checkDiagonal(self):
        for y in range(2):
            for x in range(2):
                check = self.board[y][x]
                for i in range(5):
                    if self.board[y+i][x+i] != check:
                        check = 0
                        break
                if check != 0:
                    return check
            for x in range(4, 6):
                check = self.board[y][x]
                for i in range(5):
                    if self.board[y+i][x-i] != check:
                        check = 0
                        break
                if check != 0:
                    return check
        return 0
    def checkWin(self):
        if self.checkVertical() != 0:
            return self.checkVertical()
        elif self.checkHorizontal() != 0:
            return self.checkHorizontal()
        elif self.checkDiagonal() != 0:
            return self.checkDiagonal()
        else:
            return 0
        
    def count(self):
        count = 0
        for y in range(6):
            for x in range(6):
                if self.board[y][x] != 0:
                    count += 1
        return count