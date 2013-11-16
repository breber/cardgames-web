from Card import Card
from C8Constants import C8Constants
from Constants import Constants

class CrazyEightGameRules:

    def checkCardCard( cardPlayed, onDiscard) :
        ''' check to see if a card is null or the discard pile is null '''
        if cardPlayed is None or onDiscard is None :
            return False
        

        ''' joker and 8 are always accepted '''
        if cardPlayed.getSuit() == Constants.SUIT_JOKER or cardPlayed.getValue() == C8Constants.EIGHT_CARD_NUMBER :
            return True
        

        ''' 8 is played and suit is correct '''
        if onDiscard.getValue() == C8Constants.EIGHT_CARD_NUMBER and onDiscard.getSuit() == cardPlayed.getSuit():
            return True
        

        ''' anything can be played on a joker '''
        if onDiscard.getSuit() == Constants.SUIT_JOKER :
            return True
        

        ''' must match suit or value '''
        if cardPlayed.getSuit() == onDiscard.getSuit() or cardPlayed.getValue() == onDiscard.getValue() :
            return True
        

        return False
    


