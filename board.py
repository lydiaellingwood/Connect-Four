class board():
    def __init__(self):
        self._boardLayout = []
        for r in range (6):
            row = r
            self._boardLayout.append([])
            for c in range (7):
                self._boardLayout[row].append("_")


    def PrintBoard(self):
        print("  1 2 3 4 5 6 7  ")
        for row in self._boardLayout:
            print("|",row[0],row[1],row[2],row[3],row[4],row[5],row[6],"|")

    def PlaceDisk(self, player, collumn):
        for row in range (5,-1,-1):
            if self._boardLayout[row][collumn] == "_":
                self._boardLayout[row][collumn] = player.GetSymbol()
                spaceFound = True
                break

            else:
                spaceFound = False  # will return false if there was no empty space in a collumn

        if spaceFound:
            return True

        else:
            print("That collumn is full, try again")
            return False


    def CheckForWinner(self):
        for row in self._boardLayout:
            for collumn in row:

                if collumn <= 3:
                    self.CheckRow(row,collumn)

                if row <= 2:
                    self.CheckCollumn(row,collumn)

                if row >=3 and collumn <=2:
                    self.CheckPosDiagonal(row,collumn)

                if row <=3 and collumn <=2:
                    self.CheckNegDiagonal(row,collumn)

    def CheckRow(self,row,collumn):
        pass

    def CheckCollumn(self,row,collumn):
        pass

    def CheckPosDiagonal(self,row,collumn):
        pass

    def CheckNegDiagonal(self,row,collumn):
        pass