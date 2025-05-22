class board():
    def __init__(self,verbose):
        self._boardLayout = []
        for r in range (6):
            row = r
            self._boardLayout.append([])
            for c in range (7):
                self._boardLayout[row].append("_")
        self._verbose = verbose


    def PrintBoard(self): #Prints out the board object, mostly used in testing
        print("\n    0 1 2 3 4 5 6  ")
        numOfRow = 0
        for row in self._boardLayout:
            print(numOfRow,"|",row[0],row[1],row[2],row[3],row[4],row[5],row[6],"|")
            numOfRow += 1
        print()

    def PlaceDisk(self, player, collumn): #Places a disk on the board object, does not controll graphics
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
            return False


    def CheckForWinner(self,lastRow,lastCollumn): # Checks if any player has won
        gameOver = False
        wonBy = ""

        # Checks all rows of four pieces that go through the last piece placed
        for collumn in range(lastCollumn,lastCollumn - 4,-1):
            if gameOver:
                break
            elif 0 <= collumn <= 3:
                if self.CheckRow(lastRow,collumn):
                    gameOver = True
                    wonBy = "row from (" + str(collumn) + "," + str(lastRow) + ") to (" + str(collumn + 3) + "," + str(lastRow) + ")."
                    break

        # Checks collumns of four pieces that go through the last piece placed
        for row in range(lastRow,lastRow - 4,-1):
            if gameOver:
                break
            elif 0 <= row <= 2:
                if self.CheckCollumn(row,lastCollumn):
                    gameOver = True
                    wonBy = "collumn from (" + str(lastCollumn) + "," + str(lastRow) + ") to (" + str(lastCollumn) + "," + str(lastRow + 3) + ")."

        # Checks all diagonals going this way: / that connect to the last piece placed
        for i in range(4):
            row = lastRow - i
            collumn = lastCollumn + i

            if gameOver:
                break
            elif 0 <= row <= 2 and 3 <= collumn <= 6:
                if self.CheckPosDiagonal(row,collumn):
                    gameOver = True
                    wonBy = "diagonal from (" + str(collumn) + "," + str(row) + ") to (" + str(collumn - 3) + "," + str(row + 3) + ")."

        # Checks all diagonals going this way \ that connect to the last piece placed
        for i in range (4):
            row = lastRow - i
            collumn = lastCollumn - i

            if gameOver:
                break
            elif 0 <= row <= 2 and 0 <= collumn <= 2:
                if self.CheckNegDiagonal(row,collumn):
                    gameOver = True
                    wonBy = "diagonal from (" + str(collumn) + "," + str(row) + ") to (" + str(collumn + 3) + "," + str(row + 3) + ")."

        return gameOver,wonBy



    def CheckRow(self,row,inCollumn): # Checks if four pieces in the same row make a connect four
        spaces = []
        # print(row,inCollumn)
        for collumn in range(inCollumn,inCollumn + 4):
            spaces.append(self._boardLayout[row][collumn])
        # print(spaces)
        if len(set(spaces)) > 1:
            return False
        else:
            return True

    def CheckCollumn(self,inRow,collumn): # Checks if four pieces in the same collumn make a connect four
        # print(inRow, collumn)
        spaces = []
        for row in range(inRow,inRow + 4):
            spaces.append(self._boardLayout[row][collumn])
        # print(spaces)
        if len(set(spaces)) > 1:
            return False
        else:
            return True

    def CheckPosDiagonal(self,row,collumn): # Checks if four pieces in the same diagonal (/) make a connect four
        # print(row,collumn)
        spaces = []
        for i in range(4):
            spaces.append(self._boardLayout[row+i][collumn-i])
        # print(spaces)
        if len(set(spaces)) > 1:
            return False
        else:
            return True

    def CheckNegDiagonal(self,row,collumn): # Checks if four pieces in the same diagonal (\) make a connect four
        spaces = []
        for i in range(4):
            spaces.append(self._boardLayout[row + i][collumn + i])
        # print(spaces)
        if len(set(spaces)) > 1:
            return False
        else:
            return True