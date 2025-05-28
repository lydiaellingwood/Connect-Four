from board import board
from player import player
from game import game

def main():
    verbose = False # for testing

    newBoard = board(verbose)
    if verbose:
        newBoard.PrintBoard()
    p1 = player("Red","0")
    p2 = player("Yellow", "1")

    newGame = game(newBoard,p1,p2,verbose)
    newGame.RunGame()

    if verbose:
        newBoard.PrintBoard()

main()