from board import board
from player import player
from game import game

def main():
    verbose = True

    newBoard = board(False)
    if verbose:
        newBoard.PrintBoard()
    p1 = player("Jack","0")
    p2 = player("Lydia", "1")

    newGame = game(newBoard,p1,p2,verbose)
    newGame.RunGame()

    if verbose:
        newBoard.PrintBoard()


main()