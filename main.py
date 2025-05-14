from board import board
from player import player
from game import game

def main():

    newBoard = board(False)
    newBoard.PrintBoard()
    p1 = player("Lydia","0")
    p2 = player("Jack", "1")

    newGame = game(newBoard,p1,p2)
    newGame.RunGame()

    newBoard.PrintBoard()



main()