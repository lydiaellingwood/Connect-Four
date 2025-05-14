import pygame as pg #Pygame help from https://scuba.cs.uchicago.edu/pygame/index.html

class game():
    def __init__(self,board,p1,p2):
        self.board = board
        self._p1 = p1
        self._p2 = p2
        self._currentPlayer = self._p1


    def SwapPlayer(self):
        if self._currentPlayer == self._p1:
            self._currentPlayer = self._p2
        else:
            self._currentPlayer = self._p1

    def RunGame(self):
        pg.init()
        screen = pg.display.set_mode((1280, 720))
        clock = pg.time.Clock()
        running = True
        collumnToPlace = 1
        rowToPlace = 1
        diskPos = pg.Vector2(collumnToPlace * screen.get_width() / 7, rowToPlace * screen.get_height() / 7)

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("darkblue")

            pg.draw.circle(screen, "red", diskPos, 40)

            keys = pg.key.get_pressed()
            if keys[pg.K_a]:
                if collumnToPlace >= 2:
                    collumnToPlace -= 1
                    diskPos.x -= screen.get_width() / 7


            if keys[pg.K_d]:
                if collumnToPlace <= 6:
                    collumnToPlace += 1
                    diskPos.x += screen.get_width() / 7

            if keys[pg.K_SPACE]:
                self._board.PlaceDisk(self._currentPlayer,collumnToPlace)


            pg.display.flip()
            clock.tick(20)
        pg.quit()