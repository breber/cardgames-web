from datetime import datetime
from google.appengine.ext import ndb
from protorpc import remote, messages
from endpoints_proto_datastore.ndb import EndpointsModel, EndpointsAliasProperty

import card
import endpoints

class Game(EndpointsModel):
    _message_fields_schema = ('server_id', 'game_type', 'is_active', 'deck', 'users', 'current_user', 'lastmodified')

    game_type = ndb.StringProperty()
    is_active = ndb.BooleanProperty()
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
