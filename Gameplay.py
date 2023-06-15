import Board
import Bot
import Player
import pygame
import UpdateState

class Gameplay:
    def __init__(self, board):
        self.board = board
        # self.main_menu = main_menu
    
    def singlePlayer(self, player, bot):
        FPS = 60
        state = UpdateState.State()
        clock = pygame.time.Clock()
        run = True
        clicked = False
        main_menu = False
        player_round = True
        choose_ball = True
        choose_board = False
        choose_turn = False

        while run:
            clock.tick(FPS)
            
            if player_round:
                if choose_ball == True:
                    if clicked:
                        coords = player.getBallInput()
                        x = coords[0]
                        y = coords[1]
                        if self.board.checkFree(x, y) and x != -1 and y != -1:
                            if bot.color == 1:
                                self.board.setWhite(x, y)
                            else:
                                self.board.setBlack(x, y)
                            choose_ball = False
                            choose_board = True
                if choose_board:
                    if clicked:
                        coords = player.getBoardInput()
                        x = coords[0]
                        y = coords[1]
                        if x != -1 and y != -1:
                            if y:
                                which_board = x + 2
                            else:
                                which_board = x
                            choose_board = False
                            choose_turn = True
                if choose_turn:
                    turn = player.getTurn()
                    if turn != -1:
                        if turn:
                            self.board.turnLeft(which_board)
                        else:
                            self.board.turnRight(which_board)
                    choose_ball = True
                    choose_turn = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    clicked = False


            state.drawWin(self.board)

        pygame.quit()

board = Board.Board()
Game1 = Gameplay(board)
Game1.singlePlayer(Player.Player(board), Bot.Bot(0))