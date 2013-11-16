from Constants import Constants
class Card:
    
    suit = -1
    value = -1
    idNum = -1
    
    def __init__(self, suit, value, idNum):
        self.suit = suit
        self.value = value
        self.idNum = idNum
        
    def __init__(self, c):
        self.suit = c.suit
        self.value = c.value
        self.idNum = c.idNum
        
    def toJSON(self):
        return [ { Constants.SUIT:suit, Constants.VALUE:value, Constants.ID:idNum } ]
        
    def compareTo(self, c):
        return self.idNum - c.idNum
        
    def getSuit(self):
        return self.suit
        
    def setSuit(self, suit):
        self.suit = suit
        
    def getValue(self):
        return self.value
        
    def setValue(self, value):
        self.value = value
        
    def getIdNum(self):
        return self.idNum
        
    def setIdNum(self, idNum):
        self.idNum = idNum
        
    