class board:
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

    def PlaceDisk(self, player, column): #Places a disk on the board object, does not control graphics
        placedRow = 0
        for row in range (5,-1,-1):
            if self._boardLayout[row][column] == "_":
                self._boardLayout[row][column] = player.GetSymbol()
                spaceFound = True
                placedRow = row
                break

            else:
                spaceFound = False  # will return false if there was no empty space in a column

        if spaceFound:
            return placedRow

        else:
            return False

    def CheckForWinner(self,lastRow,lastColumn): # Checks if any player has won
        gameOver = False
        wonBy = ""

        # Checks all rows of four pieces that go through the last piece placed
        for column in range(lastColumn,lastColumn - 4,-1):
            if gameOver:
                break
            elif 0 <= column <= 3:
                if self.CheckRow(lastRow,column):
                    gameOver = True
                    wonBy = "row from (" + str(column) + "," + str(lastRow) + ") to (" + str(column + 3) + "," + str(lastRow) + ")."
                    break

        # Checks columns of four pieces that go through the last piece placed
        for row in range(lastRow,lastRow - 4,-1):
            if gameOver:
                break
            elif 0 <= row <= 2:
                if self.CheckColumn(row,lastColumn):
                    gameOver = True
                    wonBy = "column from (" + str(lastColumn) + "," + str(lastRow) + ") to (" + str(lastColumn) + "," + str(lastRow + 3) + ")."

        # Checks all diagonals going this way: / that connect to the last piece placed
        for i in range(4):
            row = lastRow - i
            column = lastColumn + i

            if gameOver:
                break
            elif 0 <= row <= 2 and 3 <= column <= 6:
                if self.CheckPosDiagonal(row,column):
                    gameOver = True
                    wonBy = "diagonal from (" + str(column) + "," + str(row) + ") to (" + str(column - 3) + "," + str(row + 3) + ")."

        # Checks all diagonals going this way \ that connect to the last piece placed
        for i in range (4):
            row = lastRow - i
            column = lastColumn - i

            if gameOver:
                break
            elif 0 <= row <= 2 and 0 <= column <= 3:
                if self.CheckNegDiagonal(row,column):
                    gameOver = True
                    wonBy = "diagonal from (" + str(column) + "," + str(row) + ") to (" + str(column + 3) + "," + str(row + 3) + ")."

        return gameOver,wonBy

    def CheckRow(self,row,inColumn): # Checks if four pieces in the same row make a connect four
        spaces = []
        for column in range(inColumn,inColumn + 4):
            spaces.append(self._boardLayout[row][column])

        # if self._verbose:
        #     print(row,inColumn)
        #     print(spaces)

        if len(set(spaces)) > 1:
            return False
        else:
            return True

    def CheckColumn(self,inRow,column): # Checks if four pieces in the same column make a connect four

        spaces = []
        for row in range(inRow,inRow + 4):
            spaces.append(self._boardLayout[row][column])

        # if self._verbose:
        #     print(inRow,column)
        #     print(spaces)

        if len(set(spaces)) > 1:
            return False
        else:
            return True

    def CheckPosDiagonal(self,row,column): # Checks if four pieces in the same diagonal (/) make a connect four

        spaces = []
        for i in range(4):
            spaces.append(self._boardLayout[row+i][column-i])

        # if self._verbose:
        #     print(row,column)
        #     print(spaces)

        if len(set(spaces)) > 1:
            return False
        else:
            return True

    def CheckNegDiagonal(self,row,column): # Checks if four pieces in the same diagonal (\) make a connect four
        spaces = []
        for i in range(4):
            spaces.append(self._boardLayout[row + i][column + i])

        if self._verbose:
            print(row,column)
            print(spaces)

        if len(set(spaces)) > 1:
            return False
        else:
            return True