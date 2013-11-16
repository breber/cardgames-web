from datetime import datetime
from google.appengine.ext import endpoints, ndb
from google.appengine.ext.ndb import polymodel

from protorpc import remote, messages
from endpoints_proto_datastore.ndb import EndpointsModel, EndpointsAliasProperty, EndpointsVariantIntegerProperty

class Game(EndpointsModel):
    _message_fields_schema = ('server_id', 'game_type', 'users', 'lastmodified')

    game_type = ndb.StringProperty()
    users = ndb.StringProperty()
    lastmodified = ndb.DateTimeProperty()

    @EndpointsAliasProperty(property_type=messages.StringField)
    def server_id(self):
        return str(self.key.id())

# API specific messages
class UnusedRequest(messages.Message):
    unused = messages.StringField(1, required=False)
