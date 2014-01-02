from constants import Constants
from endpoints_proto_datastore.ndb import EndpointsModel, EndpointsAliasProperty
from google.appengine.ext import ndb

class Card(EndpointsModel):
    suit = ndb.IntegerProperty()
    value = ndb.IntegerProperty()
    id_num = ndb.IntegerProperty()

    @classmethod
    def create(cls, suit, value, id_num):
        toRet = Card()
        toRet.suit = suit
        toRet.value = value
        toRet.id_num = id_num

        return toRet

    @classmethod
    def create_from_card(cls, card):
        toRet = Card()
        toRet.suit = card.suit
        toRet.value = card.value
        toRet.id_num = card.id_num

        return toRet

    def compare_to(self, c):
        return self.id_num - c.id_num

    def get_suit(self):
        return self.suit

    def set_suit(self, suit):
        self.suit = suit

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_id_num(self):
        return self.id_num

    def set_id_num(self, id_num):
        self.id_num = id_num
