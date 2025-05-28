import pygame as pg #Pygame help from https://scuba.cs.uchicago.edu/pygame/index.html
import time

class game:
    def __init__(self,board,p1,p2,verbose):
        self._board = board #Object of the board class, holds all data for where pieces actually are
        self._p1 = p1 # Object of the player class
        self._p2 = p2 # Object of the player class
        self._currentPlayer = self._p1 #
        self._currentColor = "red"
        self._verbose = verbose

    def SwapPlayer(self): # Swaps which player is placing
        if self._currentPlayer == self._p1:
            self._currentPlayer = self._p2
            self._currentColor = "yellow"
        else:
            self._currentPlayer = self._p1
            self._currentColor = "red"

    def RunGame(self):

        # Pygame setup
        pg.init()
        pg.display.set_caption("Connect Four")
        screen = pg.display.set_mode((1080 / 2, 1080 / 2))
        clock = pg.time.Clock()
        running = True

        collumnToPlace = 4
        rowToPlace = 1
        diskPos = pg.Vector2(collumnToPlace * screen.get_width() / 8, rowToPlace * screen.get_height() / 8) #The current position to place a disk.
        placedDisks = [] # All disks that have been placed by players
        gameOver = False

        while running:

            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("darkblue")

            # Adds instructions to the screen
            instructionsFont = pg.font.Font('freesansbold.ttf', 14) #https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
            instructions = instructionsFont.render('Use L&R arrows / A&D to change columns and SPACE to place your disk', True, "white")
            screen.blit(instructions,(25,25))

            # Adds background circles to the board to help show where the player can place
            for x in range (1,8):
                for y in range (2,8):
                    pg.draw.circle(screen,"darkgray",pg.Vector2(x * screen.get_width() / 8,y * screen.get_width() / 8),22)

            # Draws all the currently placed disks
            for disk in placedDisks:
                pg.draw.circle(screen,disk[0],disk[1],20)

            # End sequence
            if gameOver:
                running = False
                print(self._currentPlayer, "wins with a", wonBy)
                winningFont = pg.font.Font('freesansbold.ttf', 48)
                winningText = winningFont.render(self._currentPlayer.GetName() + " wins!", True, self._currentColor, "darkblue")
                winningTextRect = winningText.get_rect(center = (screen.get_width()/2,screen.get_height()/8))
                screen.blit(winningText, winningTextRect)
                pg.display.flip()
                time.sleep(4)
                break

            # Draws the current location of the disk the player plans to place
            pg.draw.circle(screen, self._currentColor, diskPos, 20)

            # Takes input from keys to move disk to place left or right a column
            keys = pg.key.get_pressed()

            if keys[pg.K_a] or keys[pg.K_LEFT]:
                if collumnToPlace >= 2:
                    collumnToPlace -= 1
                    diskPos.x -= screen.get_width() / 8
                time.sleep(0.15) # Delay to prevent accidental moving

            if keys[pg.K_d] or keys[pg.K_RIGHT]:
                if collumnToPlace <= 6:
                    collumnToPlace += 1
                    diskPos.x += screen.get_width() / 8
                time.sleep(0.15) # Delay to prevent accidental moving

            # Places the current disk, along with placing a disk on the board object
            if keys[pg.K_SPACE]:
                rowPlaced = self._board.PlaceDisk(self._currentPlayer,collumnToPlace-1)
                if str(type(rowPlaced)) == "<class 'int'>": #Checks if placing on the board was sucessful, and also gets the row that the disk fell into
                    # Adds the disk to the list of disks to draw
                    diskPos.y = (rowPlaced + 2) * screen.get_height()/8
                    placedDisks.append([self._currentColor, diskPos.copy()])
                    diskPos.y = rowToPlace * screen.get_height() / 8
                    gameOver,wonBy = self._board.CheckForWinner(rowPlaced,collumnToPlace-1) # Checks if the player has won
                    if not gameOver:
                        self.SwapPlayer()
                        collumnToPlace = 4
                        diskPos.x = screen.get_width() * collumnToPlace / 8

                else: # This will happen if the player did not play in a valid space
                    print("That column is full, try again")

                time.sleep(0.5) # Delay to prevent accidental placing

            pg.display.flip()
            clock.tick(60)

        pg.quit()