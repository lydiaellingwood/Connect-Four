class board():
    def __init__(self,testMode):
        self._boardLayout = []
        for r in range (6):
            row = r
            self._boardLayout.append([])
            for c in range (7):
                self._boardLayout[row].append("_")
        self._testMode = testMode


    def PrintBoard(self):
        print("\n    0 1 2 3 4 5 6  ")
        numOfRow = 0
        for row in self._boardLayout:
            print(numOfRow,"|",row[0],row[1],row[2],row[3],row[4],row[5],row[6],"|")
            numOfRow += 1
        print()

    def PlaceDisk(self, player, collumn):
        placedRow = 0
        for row in range (5,-1,-1):
            if self._boardLayout[row][collumn] == "_":
                self._boardLayout[row][collumn] = player.GetSymbol()
                spaceFound = True
                placedRow = row
                break

            else:
                spaceFound = False  # will return false if there was no empty space in a collumn

        if spaceFound:
            return placedRow

        else:
            print("That collumn is full, try again")
            return False


    def CheckForWinner(self,lastRow,lastCollumn):
        gameOver = False
        wonBy = ""
        for collumn in range(lastCollumn,lastCollumn - 4,-1):
            if gameOver:
                break
            elif 0 <= collumn <= 3:
                if self.CheckRow(lastRow,collumn):
                    gameOver = True
                    wonBy = "row from (" + str(collumn) + "," + str(lastRow) + ") to (" + str(collumn + 3) + "," + str(lastRow) + ")."
                    break

        for row in range(lastRow,lastRow - 4,-1):
            if gameOver:
                break
            elif 0 <= row <= 2:
                if self.CheckCollumn(row,lastCollumn):
                    gameOver = True
                    wonBy = "collumn from (" + str(lastCollumn) + "," + str(lastRow) + ") to (" + str(lastCollumn) + "," + str(lastRow + 3) + ")."


        for i in range(4):
            row = lastRow - i
            collumn = lastCollumn + i

            if gameOver:
                break
            elif 0 <= row <= 2 and 3 <= collumn <= 6:
                if self.CheckPosDiagonal(row,collumn):
                    gameOver = True
                    wonBy = "diagonal from (" + str(collumn) + "," + str(lastRow) + ") to (" + str(collumn - 3) + "," + str(lastRow + 3) + ")."

        for i in range (4):
            row = lastRow - i
            collumn = lastCollumn - i

            if gameOver:
                break
            elif 0 <= row <= 2 and 0 <= collumn <= 2:
                if self.CheckNegDiagonal(row,collumn):
                    gameOver = True
                    wonBy = "diagonal from (" + str(collumn) + "," + str(lastRow) + ") to (" + str(collumn + 3) + "," + str(lastRow + 3) + ")."

        return gameOver,wonBy



    def CheckRow(self,row,inCollumn):
        spaces = []
        # print(row,inCollumn)
        for collumn in range(inCollumn,inCollumn + 4):
            spaces.append(self._boardLayout[row][collumn])
        # print(spaces)
        if len(set(spaces)) > 1:
            return False
        else:
            return True


    def CheckCollumn(self,inRow,collumn):
        # print(inRow, collumn)
        spaces = []
        for row in range(inRow,inRow + 4):
            spaces.append(self._boardLayout[row][collumn])
        # print(spaces)
        if len(set(spaces)) > 1:
            return False
        else:
            return True

    def CheckPosDiagonal(self,row,collumn):
        # print(row,collumn)
        spaces = []
        for i in range(4):
            spaces.append(self._boardLayout[row+i][collumn-i])
        # print(spaces)
        if len(set(spaces)) > 1:
            return False
        else:
            return True

    def CheckNegDiagonal(self,row,collumn):
        spaces = []
        for i in range(4):
            spaces.append(self._boardLayout[row + i][collumn + i])
        # print(spaces)
        if len(set(spaces)) > 1:
            return False
        else:
            return True