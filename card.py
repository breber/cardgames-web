from constants import Constants
from endpoints_proto_datastore.ndb import EndpointsModel, EndpointsAliasProperty
from google.appengine.ext import ndb

class Card(EndpointsModel):
    suit = ndb.IntegerProperty()
    value = ndb.IntegerProperty()
    idNum = ndb.IntegerProperty()

    @classmethod
    def create(cls, suit, value, idNum):
        toRet = Card()
        toRet.suit = suit
        toRet.value = value
        toRet.idNum = idNum

        return toRet

    @classmethod
    def create_from_card(cls, card):
        toRet = Card()
        toRet.suit = card.suit
        toRet.value = card.value
        toRet.idNum = card.idNum

        return toRet

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
