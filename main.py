from board import board
from player import player


def main():
    newBoard = board()
    newBoard.PrintBoard()
    p1 = player("Lydia","0")
    p2 = player("Jack", "1")

    for i in range(4):
         newBoard.PlaceDisk(p2,3)
    newBoard.PrintBoard()
    newBoard.CheckForWinner(5,3)

main()