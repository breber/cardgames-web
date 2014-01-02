from constants import ComputerDifficulty

import card

class Player(ndb.Model):
    cards = ndb.StructuredProperty(card.Card, repeated=True)
    name = ndb.StringProperty()
    player_id = ndb.IntegerProperty(default=-1)
    position = ndb.IntegerProperty(default=-1)
    difficulty = ndb.IntegerProperty(default=ComputerDifficulty.NONE)


    def getNumCards(self) :
        return len(self.cards)

    def addCard(self, card) :
        self.cards.add(card)

    def removeCard(self, card) :
        for c in self.cards:
            if c.getIdNum() == card.getIdNum():
                cards.remove(c)
                return

