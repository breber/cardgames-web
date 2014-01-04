from constants import ComputerDifficulty
from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel, EndpointsAliasProperty

import card
import logging

class Player(EndpointsModel):
    cards = ndb.StructuredProperty(card.Card, repeated=True)
    name = ndb.StringProperty()
    player_id = ndb.IntegerProperty(default=-1)
    position = ndb.IntegerProperty(default=-1)
    difficulty = ndb.IntegerProperty(default=ComputerDifficulty.DIFFICULTY_NONE)

    def __init__(self, name='Computer', player_id=-1, position=-1, difficulty=ComputerDifficulty.DIFFICULTY_NONE):
        ndb.Model.__init__(self)
        
        logging.info('name = ' + name)
        if(name is None):
            self.name = 'Computer'
        else:
            self.name = name
            
        logging.info('player_id = ' + str(player_id))
        self.player_id = player_id
        logging.info('position = ' + str(position))
        self.position = position
        logging.info('difficulty = ' + str(difficulty))
        self.difficulty = difficulty

    def getNumCards(self):
        return len(self.cards)

    def addCard(self, card):
        self.cards.add(card)

    def removeCard(self, card):
        for c in self.cards:
            if c.get_id_num() == card.get_id_num():
                cards.remove(c)
                return

