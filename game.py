import pygame as pg #Pygame help from https://scuba.cs.uchicago.edu/pygame/index.html
import time

class game():
    def __init__(self,board,p1,p2):
        self._board = board
        self._p1 = p1
        self._p2 = p2
        self._currentPlayer = self._p1
        self._currentColor = "red"


    def SwapPlayer(self):
        if self._currentPlayer == self._p1:
            self._currentPlayer = self._p2
            self._currentColor = "yellow"
        else:
            self._currentPlayer = self._p1
            self._currentColor = "red"

    def RunGame(self):
        pg.init()
        screen = pg.display.set_mode((1920 / 2, 1080 / 2))
        clock = pg.time.Clock()
        running = True
        collumnToPlace = 1
        rowToPlace = 1
        diskPos = pg.Vector2(collumnToPlace * screen.get_width() / 8, rowToPlace * screen.get_height() / 8)
        placedDisks = []

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("darkblue")
            pg.draw.circle(screen, self._currentColor, diskPos, 20)
            for disk in placedDisks:
                pg.draw.circle(screen,disk[0],disk[1],20)

            keys = pg.key.get_pressed()
            if keys[pg.K_a]:
                if collumnToPlace >= 2:
                    collumnToPlace -= 1
                    diskPos.x -= screen.get_width() / 8
                time.sleep(0.15)


            if keys[pg.K_d]:
                if collumnToPlace <= 6:
                    collumnToPlace += 1
                    diskPos.x += screen.get_width() / 8
                time.sleep(0.15)

            if keys[pg.K_SPACE]:
                rowPlaced = self._board.PlaceDisk(self._currentPlayer,collumnToPlace-1)
                if str(type(rowPlaced)) == "<class 'int'>":
                    diskPos.y = (rowPlaced + 2) * screen.get_height()/8
                    placedDisks.append([self._currentColor, diskPos.copy()])
                    diskPos.y = rowToPlace * screen.get_height() / 8
                    self.SwapPlayer()
                    gameOver,wonBy = self._board.CheckForWinner(rowPlaced,collumnToPlace-1)
                    if gameOver:
                        print(self._currentPlayer, "wins with a", wonBy)

                else:
                    pass

                time.sleep(0.5)


            pg.display.flip()
            clock.tick(60)
        pg.quit()