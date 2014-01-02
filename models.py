from datetime import datetime
from google.appengine.ext import ndb
from protorpc import remote, messages
from endpoints_proto_datastore.ndb import EndpointsModel, EndpointsAliasProperty

import card
import endpoints

class GameState:
    STATE_CREATED = 0
    STATE_STARTED = 1
    STATE_COMPLETED = 2

class Game(EndpointsModel):
    _message_fields_schema = ('server_id', 'game_type', 'is_active', 'deck', 'users', 'current_user', 'lastmodified')

    game_type = ndb.StringProperty()
    state = ndb.IntegerProperty(default=GameState.STATE_CREATED)
    deck = ndb.StructuredProperty(card.Card, repeated=True)
    users = ndb.StringProperty(repeated=True)
    current_user = ndb.IntegerProperty()
    lastmodified = ndb.DateTimeProperty()

    @EndpointsAliasProperty(property_type=messages.StringField)
    def server_id(self):
        return str(self.key.id())

# API specific messages
class UnusedRequest(messages.Message):
    unused = messages.StringField(1, required=False)

# Empty basic turn information that all turn types will have.
class Turn(EndpointsModel):
    _message_fields_schema = ('turn_id', 'server_id', 'current_user', 'lastmodified')
	server_id = ndb.StringProperty()
	current_user = ndb.IntegerProperty()
    lastmodified = ndb.DateTimeProperty()

    @EndpointsAliasProperty(property_type=messages.StringField)
    def turn_id(self):
        return str(self.key.id())
	
# Simple Turn type to play a card.
class SimpleTurn(Turn):
    _message_fields_schema = ('turn_id', 'server_id', 'current_user', 'card', 'lastmodified')
    card = ndb.StructuredProperty(card.Card)
	is_draw_card = ndb.BooleanProperty()
	
# Bet Turn type to play a card.
class BetTurn(Turn):
    _message_fields_schema = ('turn_id', 'server_id', 'current_user', 'card', 'lastmodified')
    amount = ndb.IntegerProperty()
	trump = ndb.IntegerProperty()
	is_going_alone = ndb.BooleanProperty()
