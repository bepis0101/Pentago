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
        side = ""
        screen = state.WIN

        while run:
            clock.tick(FPS)
            
            win_screen = self.board.checkWin()

            if win_screen: 
                print(win_screen)
                run = False

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
                            clicked = False
                            continue
                elif choose_board:
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
                            clicked = False
                            continue
                elif choose_turn:
                    if side != "":
                        if side == "left":
                            self.board.turnLeft(which_board)
                        if side == "right":
                            self.board.turnRight(which_board)
                        choose_ball = True
                        choose_turn = False
                        player_round = False
                        continue
            
            if not player_round:
                self.board = bot.moveOfBot()
                player_round = True

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    clicked = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        side = "left"
                    if event.key == pygame.K_RIGHT:
                        side = "right"
                if event.type == pygame.KEYUP:
                    side = ""


            state.drawWin(self.board)

        pygame.quit()

board = Board.Board()
Game1 = Gameplay(board)
Game1.singlePlayer(Player.Player(board), Bot.Bot(0, board))