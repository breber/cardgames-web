from google.appengine.ext import ndb
from crazyeightsconstants import C8Constants

import card
import game
import logging
import random

class CrazyEightsGame(game.Game):
    discard_pile = ndb.StructuredProperty(card.Card, repeated=True)

    def start(self):
        # Overrides the start in Game
        super(CrazyEightsGame, self).start()

        # If we don't have a valid number of players, don't start the game
        logging.info('Number of Users = ' + str(len(self.users)))
        if len(self.users) < 2 or len(self.users) > 5 : # TODO: do we want to allow one player games?
            raise endpoints.BadRequestException('invalid number of players')

        # TODO handle computer players
        if( 0 < len(self.users) ):
            self.player1 = player.Player(self.users[i].nickname(), self.users[i].user_id(), 0, ComputerDifficulty.DIFFICULTY_NONE)
        else:
            self.player1 = player.Player('Computer 0', -1, 0, ComputerDifficulty.DIFFICULTY_EASY)
        if( 1 < len(self.users) ):
            self.player1 = player.Player(self.users[i].nickname(), self.users[i].user_id(), 1, ComputerDifficulty.DIFFICULTY_NONE)
        else:
            self.player1 = player.Player('Computer 1', -1, 1, ComputerDifficulty.DIFFICULTY_EASY)
        if( 2 < len(self.users) ):
            self.player1 = player.Player(self.users[i].nickname(), self.users[i].user_id(), 2, ComputerDifficulty.DIFFICULTY_NONE)
        else:
            self.player1 = player.Player('Computer 2', -1, 2, ComputerDifficulty.DIFFICULTY_EASY)
        if( 3 < len(self.users) ):
            self.player1 = player.Player(self.users[i].nickname(), self.users[i].user_id(), 3, ComputerDifficulty.DIFFICULTY_NONE)
        else:
            self.player1 = player.Player('Computer 3', -1, 3, ComputerDifficulty.DIFFICULTY_EASY)
        
        # TODO Shuffle
        logging.info('Start shuffling')
        self.shuffle_deck()
        
        # TODO Deal
        logging.info('Deal cards')
        self.deal_cards()
        
        # TODO add first card to discard_pile
        logging.info('Deal cards')
        self.discard_pile.push(self.deck.pop())
        
        # TODO tell first player that it is their turn.
        
        logging.info('Finished Start Method')

    def deal_cards(self):
        for i in range(C8Constants.NUMBER_OF_CARDS_PER_HAND):
            for i in range(C8Constants.MAX_NUM_PLAYERS):
                self.get_player(i).add_card(self.deck.pop())
    
    def shuffle_deck(self):
        random.shuffle(self.deck)

    def check_card(played, discard):
        # check to see if a card is null or the discard pile is null
        if played is None or discard is None:
            return False

        # joker and 8 are always accepted
        if played.get_suit() == Constants.SUIT_JOKER or \
           played.get_value() == C8Constants.EIGHT_CARD_NUMBER:
            return True

        # 8 is played and suit is correct
        if discard.get_value() == C8Constants.EIGHT_CARD_NUMBER and \
           discard.get_suit() == played.get_suit():
            return True

        # anything can be played on a joker
        if discard.get_suit() == Constants.SUIT_JOKER:
            return True

        # must match suit or value
        if played.get_suit() == discard.get_suit() or \
           played.get_value() == discard.get_value():
            return True

        return False
