from board import board
from player import player
import pygame as pg #Pygame help from https://scuba.cs.uchicago.edu/pygame/index.html

def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    running = True
    collumnToPlace = 1
    rowToPlace = 1
    diskPos = pg.Vector2(collumnToPlace * screen.get_width()/7,rowToPlace * screen.get_height()/7)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("darkblue")

        pg.draw.circle(screen,"red",diskPos,40)

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            if collumnToPlace >= 2:
                collumnToPlace -= 1
                diskPos.x -= screen.get_width()/8

        if keys[pg.K_d]:
            if collumnToPlace <= 6:
                collumnToPlace += 1
                diskPos.x += screen.get_width()/8

        if keys[pg.K_SPACE]:
            pass

        pg.display.flip()
        clock.tick(20)
    pg.quit()

    newBoard = board(False)
    newBoard.PrintBoard()
    p1 = player("Lydia","0")
    p2 = player("Jack", "1")

    for i in range(4):
         newBoard.PlaceDisk(p2,3)
    newBoard.PrintBoard()
    newBoard.CheckForWinner(5,3)

main()