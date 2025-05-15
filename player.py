class player():
    def __init__(self,name,symbol):
        self._name = name
        self._symbol = symbol

    def __str__(self):
        return self._name

    def PlaceDisk(self,collumn):
        pass

    def GetSymbol(self):
        return self._symbol

    def GetName(self):
        return self._name