class board():
    def __init__(self):
        self._boardLayout = []
        for r in range (6):
            row = r
            self._boardLayout.append([])
            for c in range (7):
                self._boardLayout[row].append("_")


    def PrintBoard(self):
        print("  0 1 2 3 4 5 6  ")
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


    def CheckForWinner(self,lastRow,lastCollumn):
        for collumn in range(lastCollumn,lastCollumn - 4,-1):
            if 0 <= collumn <= 3:
                self.CheckRow(lastRow,collumn)

        for row in range(lastRow,lastRow - 4,-1):
            if 0 <= row <= 2:
                self.CheckCollumn(row,lastCollumn)

        for i in range(4):
            row = lastRow - i
            collumn = lastCollumn + i
            if 0 <= row <= 2 and 3 <= collumn <= 6:
                self.CheckPosDiagonal(row,collumn)

        for i in range (4):
            row = lastRow - i
            collumn = lastCollumn - i
            if 0 <= row <= 2 and 0 <= collumn <= 2:
                self.CheckNegDiagonal(row,collumn)

    def CheckRow(self,row,inCollumn):
        spaces = []
        print(row,inCollumn)
        for collumn in range(inCollumn,inCollumn + 4):
            spaces.append(self._boardLayout[row][collumn])
        print(spaces)
        if len(set(spaces)) > 1:
            return False
        else:
            return True

    def CheckCollumn(self,inRow,collumn):
        print(inRow, collumn)
        spaces = []
        for row in range(inRow,inRow + 4):
            spaces.append(self._boardLayout[row][collumn])
        print(spaces)
        if len(set(spaces)) > 1:
            return False
        else:
            return True

    def CheckPosDiagonal(self,row,collumn):
        pass

    def CheckNegDiagonal(self,row,collumn):
        pass