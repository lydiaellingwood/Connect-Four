from email.contentmanager import get_and_fixup_unknown_message_content

from board import board
from player import player


def main():
    newBoard = board()
    newBoard.PrintBoard()
    p1 = player("Lydia","0")
    p2 = player("Jack", "1")

    newBoard.PlaceDisk(p1,3)
    # for i in range(7):
    #     newBoard.PlaceDisk(p2,3)
    newBoard.PrintBoard()

main()