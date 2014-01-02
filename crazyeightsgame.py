from google.appengine.ext import ndb
from crazyeightsconstants import C8Constants

import game

class CrazyEightsGame(game.Game):
    discard_pile = ndb.StructuredProperty(card.Card, repeated=True)

    def start(self):
        # Overrides the start in Game
        super(CrazyEightsGame, self).start()

        # If we don't have a valid number of players, don't start the game
        if len(self.users) < 2 or len(self.users) > 5 : # TODO: do we want to allow one player games?
            raise endpoints.BadRequestException('invalid number of players')

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
