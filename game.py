from datetime import datetime
from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel, EndpointsAliasProperty
from protorpc import remote, messages

import card
import endpoints
import player

class GameState:
    STATE_CREATED = 0
    STATE_STARTED = 1
    STATE_COMPLETED = 2

class Game(EndpointsModel):
    # TODO: restrict the players sent to only the ones necessary
    _message_fields_schema = ('server_id', 'game_type', 'state', 'deck', 'player1', 'player2', 'player3', 'player4', 'current_user', 'lastmodified')

    game_type = ndb.StringProperty()
    state = ndb.IntegerProperty(default=GameState.STATE_CREATED)
    deck = ndb.StructuredProperty(card.Card, repeated=True)

    # StructuredProperty doesn't allow repeated=True with properties
    # that have repeated properties of their own
    player1 = ndb.StructuredProperty(player.Player)
    player2 = ndb.StructuredProperty(player.Player)
    player3 = ndb.StructuredProperty(player.Player)
    player4 = ndb.StructuredProperty(player.Player)
    current_user = ndb.IntegerProperty()
    lastmodified = ndb.DateTimeProperty()

    @EndpointsAliasProperty(property_type=messages.StringField)
    def server_id(self):
        return str(self.key.id())


    def start(self):
        # Nothing to do at this level
        pass
