class board():
    def __init__(self):
        self._boardLayout = {}
        for r in range (6):
            row = "r" + str(r)
            self._boardLayout[row] = {}
            for c in range (7):
                collumn = "c" + str(c)

                self._boardLayout[row][collumn] = "_"


    def PrintBoard(self):
        print("  1 2 3 4 5 6 7  ")
        for row in self._boardLayout.values():
            print("|",row["c0"],row["c1"],row["c2"],row["c3"],row["c4"],row["c5"],row["c6"],"|")

    def PlaceDisk(self, player, collumn):
        pass