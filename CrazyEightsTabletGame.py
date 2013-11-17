from Card import Card

'''
  A class for keeping track of the logic and game state for the game type crazy eights
'''
class CrazyEightsTabletGame:

    '''
      A tag for the class name
    '''
    '''private static final String TAG = CrazyEightsTabletGame.class.getName()'''
    '''
      A variable for and instance of the crazy eights game type
    '''
    '''private static CrazyEightsTabletGame instance = null'''

    '''
      A private variable for a list of players in the current game
    '''
    players = []

    '''
      A private variable representing the game deck for the crazy eights game
    '''
    '''gameDeck = Deck()'''

    '''
      A private variable to represent the difficulty of computers in the current game
    '''
    computerDifficulty = Constants.EASY

    '''
      An iterator for removing cards from the shuffled deck
    '''
    '''private Iterator<Card> iter'''

    '''
      A list of all the cards in the shuffle deck
    '''
    huffledDeck = []

    '''
      A list of all the cards in the discard pile
    '''
    discardPile = []

    '''
      Represents whether the game is currently active
    '''
    gameActive = False

    '''
      Create a new instance of the tablet game so that multiple classes are able to reference
      the same card game and only one instance will be made available. self method uses the default
      constructor.
      
      @return an instance of CrazyEightsTabletGame
    '''
    def getInstance(self) :
        if (self.instance == null) :
            self instance = CrazyEightsTabletGame()
        
        return instance
    

    '''
      Clear the game instance
    '''
    def clearInstance() :
        self instance = None
    

    '''
      A constructor for the crazy eights game type. self constructor will initialize the all the variables
      for a game of crazy eights including the rules, players, deck, shuffled deck pile and the discard pile.
    '''
    def __init__ (self) : 
        self.players = []
        self.gameDeck = Deck()
        self.shuffledDeck = self.gameDeck.getCardIDs()
        self.discardPile = []
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#getPlayers()
    '''
    
    def getPlayers(self) :
        return self.players
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#getShuffledDeck()
    '''
    
    def getShuffledDeck(self) :
        return self.shuffledDeck
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#setComputerDifficulty(java.lang.String)
    '''
    
    def setComputerDifficulty(self, diff):
        self.computerDifficulty = diff
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#getComputerDifficulty()
    '''
    
    def getComputerDifficulty(self) :
        return self.computerDifficulty
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#setup()
    '''
    
    def setup(self) :
       '''Shuffle the card ID's'''
        self.shuffleDeck()

       ''' Deal the initial cards to all the players in the game'''
        self.deal()

       ''' Discard pile first one '''
        self.discardPile.insert(iter.next())

       ''' Remove the last card returned by iter.next() '''
        iter.remove()
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#shuffleDeck()
    '''
    
    def shuffleDeck(self) :
       '''create a random number generator '''
        Random generator = new Random()

       '''shuffle the deck '''
        Collections.shuffle(shuffledDeck, generator)

       '''set the iterator to go through the shuffled deck '''
        self.iter = self.shuffledDeck.iterator()
    

    '''
      self method will shuffle the discard pile and replace the current draw
      pile with the old discard pile. After self method call the shuffled deck
      will only have the top card remaining.
    '''
    def shuffleDiscardPile(self) : 
        card = self.discardPile.remove(Len(self.DiscardPile)- 1)

       ''' Make copy of discard pile to be new shuffled deck '''
       ''' add to the shuffled deck in case there are still '''
       ''' some cards left that are unaccounted for '''
        self.shuffledDeck.addAll(self.discardPile)

       '''
        if Util.isDebugBuild():
            Log.d(TAG, "shuffleDiscardPile: shuffledDeck: " + shuffledDeck.size() + " - discardPile: " + discardPile.size())
       '''
        

       ''' Remove all the cards from the discard pile '''
        discardPile.removeAll(discardPile)

       ''' Place the last card discarded back on the discard pile '''
        self.discardPile.insert(card)

       ''' Shuffle the deck '''
        self.shuffleDeck()
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#deal()
    '''
    
    def deal(self) : 
        gameActive = True
        if (Util.isDebugBuild()) 
            Log.d(TAG, "deal: numberOfPlayers: " + players.size())

            for (Player p : players) 
                Log.d(TAG, "pre deal: player[" + p.getId() + "] has " + p.getNumCards() + " cards")
                Log.d(TAG, "          player[" + p.getId() + "]: " + p)
            
        

       ''' Count the number of human players '''
        for (Player p : players) 
            if (!p.getIsComputer()) 
            
        

       ''' Deal the given number of cards to each player
        for (i = 0 i < NUMBER_OF_CARDS_PER_HAND i++) 
            for (Player p : players) 
               ''' give them a card '''
                p.addCard(iter.next())

                if (Util.isDebugBuild()) 
                    Log.d(TAG, "p.addCard: player[" + p.getId() + "] has " + p.getNumCards() + " cards")
                

               '''remove the last card returned by iter.next() '''
                iter.remove()
            
        

        if (Util.isDebugBuild()) 
            for (Player p : players) 
                Log.d(TAG, "postdeal: player[" + p.getId() + "] has " + p.getNumCards() + " cards")
                Log.d(TAG, "          player[" + p.getId() + "]: " + p)
            
        
    

    '''
      Get the discard pile
      
      @return the discard pile
    '''
    List<Card> getDiscardPile() 
        return discardPile
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#discard(com.worthwhilegames.cardgames.shared.Player, com.worthwhilegames.cardgames.shared.Card)
    '''
    
    discard(Player player, Card card) 
        discardPile.add(card)
        player.removeCard(card)
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#isGameOver(com.worthwhilegames.cardgames.shared.Player)
    '''
    
    isGameOver(Player player) 
       '''check to see if the player has any cards left '''
        if (player.getNumCards() == 0) 
            return True
        

        return False
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#draw(com.worthwhilegames.cardgames.shared.Player)
    '''
    
    Card draw(Player player) 
        if (!iter.hasNext()) 
            self.shuffleDiscardPile()
        

        if (!iter.hasNext()) 
            return null
        

       ''' Get a card out of the shuffled pile and add to the players hand '''
        Card card = iter.next()
        player.addCard(card)

       ''' Remove the last card returned by iter.next()'''
        iter.remove()

       ''' Shuffle the deck if the player drew the last card '''
        if (shuffledDeck.isEmpty()) 
            shuffleDiscardPile()
        

        return card
    

    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#dropPlayer(java.lang.String)
    '''
    
    dropPlayer(String playerMacAddress) 
        if (Util.isDebugBuild()) 
            Log.d(TAG, "dropPlayer: " + playerMacAddress)
        

        Player p = null

        for (Player player : players) 
            if (player.getId().equals(playerMacAddress)) 
                p = player
                break
            
        

        if (gameActive) 
            if (p != null) 
                p.setIsComputer(True)
                p.setComputerDifficulty(computerDifficulty)
             else 
                if (Util.isDebugBuild()) 
                    Log.d(TAG, "dropPlayer: couldn't find player with id: " + playerMacAddress)
                
            
         else 
           ''' If the game hasn't been started yet, just remove them from the list
            players.remove(p)
        
    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#getDiscardPileTop()
    '''
    Card getDiscardPileTop() 
        if (!discardPile.isEmpty()) 
            return discardPile.get(discardPile.size() - 1)
         else 
            return null
        
    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#getNumPlayers()
    '''
    getNumPlayers() 
        return players.size()
    
    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#getMaxNumPlayers()
    '''
    getMaxNumPlayers() 
        if (players.isEmpty() || !gameActive) 
            return C8Constants.MAX_NUM_PLAYERS
         else 
            count = 0
            for (Player p : players) 
                if (p.isDisconnected()) 
                    count++
                
            

            return players.size() - count
        
    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#addPlayer(com.worthwhilegames.cardgames.shared.Player)
    '''
    def addPlayer(self, p) :
        self.players.insert(p)
    
    ''' (non-Javadoc)
      @see com.worthwhilegames.cardgames.shared.Game#isActive()
    '''
    def isActive(self) : 
        return gameActive
    
    def getCardAtPosition(self, position) :
        if position == 2:
            return self.getDiscardPileTop()
         elif (position == 4) 
           '''TODO customizable back'''
            return Card()
        
        return None
