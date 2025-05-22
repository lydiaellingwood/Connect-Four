class player(): # The player object
    def __init__(self,name,symbol):
        self._name = name
        self._symbol = symbol

    def __str__(self):
        return self._name # Used for printing winner

    def PlaceDisk(self,collumn):
        pass

    def GetSymbol(self): # Used in the board object
        return self._symbol

    def GetName(self):
        return self._name