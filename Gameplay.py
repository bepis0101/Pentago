import Board
import Bot
import Player
import pygame
import UpdateState
import MainMenu
import random

class Gameplay:
    def __init__(self, board):
        self.board = board

    def main(self):
        self.board = Board.Board()
        bot_color = random.randint(0, 1)
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Pentago")
        menu = MainMenu.MainMenu(screen)
        run = True
        while run:
            screen.fill('light blue')
            if menu.single_button.draw(screen):
                self.singlePlayer(Player.Player(self.board), Bot.Bot(bot_color, self.board))
            if menu.multi_button.draw(screen):
                self.multiPlayer(Player.Player(self.board), Player.Player(self.board))
            if menu.exit_button.draw(screen):
                run = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
                    

    def drawText(self, screen, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def winScreen(self, win_screen):
        if win_screen:
            pygame.font.init()
            font = pygame.font.SysFont('arial', 40, True)
            menu = False
            run_winscreen = True
            screen = pygame.display.set_mode((700, 700))
            S = "MATCH WON BY "
            if win_screen == 1:
                S += "Black "
            else:
                S += "White "
            pygame.display.set_caption(S)
            while run_winscreen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run_winscreen = False
                    if event.type == pygame.KEYDOWN:
                        menu = True
                    if event.type == pygame.KEYUP and menu:
                        win_screen = 0
                        run_winscreen = False
                        self.main()
            
                self.drawText(screen, S, font, (255, 255, 255), 120, 300)
                self.drawText(screen, "PRESS ANY KEY TO CONTINUE", font, (255, 255, 255), 120, 350)
                pygame.display.update()

    def singlePlayer(self, player, bot):
        FPS = 60
        state = UpdateState.State()
        clock = pygame.time.Clock()
        clicked = False
        run_maingame = True
        win_screen = 0
        
        if bot.color:
            player_round = False
        else:
            player_round = True

        choose_ball = True
        choose_board = False
        choose_turn = False
        side = ""


        while run_maingame:
            clock.tick(FPS)
            
            win_screen = self.board.checkWin()

            if win_screen and choose_ball == True: 
                run_maingame = False
                self.winScreen(win_screen)

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
                    run_maingame = False
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
    def multiPlayer(self, player1, player2):
        FPS = 60
        state = UpdateState.State()
        clock = pygame.time.Clock()
        clicked = False
        run_maingame = True
        player_round = True

        choose_ball = True
        choose_board = False
        choose_turn = False
        side = ""

        while run_maingame:
            clock.tick(FPS)
            
            win_screen = self.board.checkWin()

            if win_screen and choose_ball == True: 
                run_maingame = False
                self.winScreen(win_screen)

            if player_round:
                if choose_ball == True:
                    if clicked:
                        coords = player1.getBallInput()
                        x = coords[0]
                        y = coords[1]
                        if self.board.checkFree(x, y) and x != -1 and y != -1:
                            self.board.setWhite(x, y)
                            choose_ball = False
                            choose_board = True
                            clicked = False
                            continue
                elif choose_board:
                    if clicked:
                        coords = player1.getBoardInput()
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
                if choose_ball == True:
                    if clicked:
                        coords = player2.getBallInput()
                        x = coords[0]
                        y = coords[1]
                        if self.board.checkFree(x, y) and x != -1 and y != -1:
                            self.board.setBlack(x, y)
                            choose_ball = False
                            choose_board = True
                            clicked = False
                            continue
                elif choose_board:
                    if clicked:
                        coords = player2.getBoardInput()
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
                        player_round = True
                        continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_maingame = False
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

Game1 = Gameplay(Board.Board())
Game1.main()