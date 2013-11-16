from Constants import Constants
from Card import Card

class Player :

    ''' A list of card objects to represent the cards a player has '''
    cards = []

    ''' A string to store the name of the user '''
    name = ''

    ''' A string to store the idNum of the user which will be represented by a MAC Address '''
    idNum = -1

    ''' The position of the current user on the gameboard '''
    position = -1

    ''' A boolean to set whether or not self player is a computer '''
    isComputer = False

    ''' A variable to set the difficulty of the player if they are a computer '''
    computerDifficulty = Constants.EASY

    ''' Represents whether self player has a name yet '''
    hasName = False

    ''' Represents whether self player has been disconnected '''
    isDisconnected = False

    ''' A default player constructor. A fields will be set with getters and setters '''
    def __init__(self) :
        self.cards = []
        self.name = null
        self.idNum = null
    

    ''' A method to get a list of cards that a player currently has
      
      @return a list of card objects that a player has in their hand '''
    def getCards(self) :
        return cards
    

    ''' A method to get the number of cards that a player has
      
      @return an integer representing the number of cards in a players hand '''
    def getNumCards(self) :
        return Len(cards)
    

    ''' A method to add a card to a players hand
      
      @param card the card to be added to the list of cards a player has '''
    def addCard(self, card) :
        self.cards.add(card)
    

    ''' A method to get a players computer status
      
      @return True if the current player is a computer, False otherwise '''
    def getIsComputer(self) :
        return self.isComputer
    

    ''' A method to set if a player is a computer or not
      
      @param isComp True if the player is a computer, False otherwise '''
    def setIsComputer(self, isComp) :
        isComputer = isComp

        if self.isComputer:
            self.isDisconnected = False
    

    ''' A method to get the difficulty of a computer player
      
      @return an representing easy, medium or hard '''
    def getComputerDifficulty(self) :
        return self.computerDifficulty
    

    ''' A method to set the difficulty of a computer player
      
      @param dif an representing easy, medium or hard '''
    def setComputerDifficulty(self, dif) :
        self.computerDifficulty = dif
    

    ''' This method will remove a card from a players hand by object matching
      using a loop that checks every card in the players hand
      
      @param card
                 the card to be removed from the players hand '''
    def removeCard(self, card) :
        for c in self.cards :
            if c.getIdNum() == card.getIdNum() :
                cards.remove(c)
                return
            
        
    

    ''' A method to return the name of a player
      
      @return a string representing the name of the player '''
    def getName(self) :
        return self.name
    

    ''' A method to set the name of a player object
      
      @param name the new name of the player '''
    def setName(self, name) :
        self.name = name
        self.hasName = True
    

    ''' This method will return the MAC Address of a player
      
      @return a string representing the MAC Address of a player '''
    def getId(self) :
        return self.idNum
    

    ''' This method will set the idNum of a player
      
      @param idNum a string representing the new ID of a player '''
    def setId(self, idNum) :
        self.idNum = idNum
        self.isDisconnected = False
        self.isComputer = False
    

    ''' This method will get the current position of the player based on the game board
      
      @return an integer to represent the player's location on the game board '''
    def getPosition(self) :
        return self.position
    

    ''' This method will set the position of the player on the game board
      
      @param position an integer representing the new player position '''
    def setPosition(self, position) :
        self.position = position
    

    ''' @return the hasName '''
    def hasName(self) :
        return self.hasName
    

    ''' @param hasName the hasName to set '''
    def clearName(self) :
        self.hasName = False
    

    ''' @return the isDisconnected '''
    def isDisconnected(self) :
        return self.isDisconnected
    

    ''' @param isDisconnected the isDisconnected to set '''
    def setDisconnected(self, isDisconnected) :
        self.isDisconnected = isDisconnected
    

    ''' This toString() method will overridNume the default toString() method. This
      will return a JSON object that is in the form of a string which will be
      easy for decoding
      
      @return a string representation of a player object '''
     
    '''TODO'''
    def toString(self) :
        '''Encode the cards into a JSONArray'''  
        arr = []
        for c in self.cards:
            arr.insert(c.toJSONObject())
        

        return arr.toString()
    

