from datetime import datetime
from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from endpoints_proto_datastore.ndb import EndpointsModel, EndpointsAliasProperty
from protorpc import remote, messages

import card
import endpoints
import player

class GameState:
    STATE_CREATED = 0
    STATE_STARTED = 1
    STATE_COMPLETED = 2

class Game(EndpointsModel, polymodel.PolyModel):

    # TODO: restrict the players sent to only the ones necessary
    _message_fields_schema = ('id', 'server_id', 'game_type', 'state', 'deck', 'player1', 'player2', 'player3', 'player4', 'current_user', 'lastmodified')
    
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
        return str(self.key.string_id())

        


    def start(self):
        # Nothing to do at this level
        pass
	
	def get_player(self, index):
		if index == 0:
			return player1
		elif index == 1:
			return player2
		elif index == 2:
			return player3
		elif index == 3:
			return player4
		else:
			return None
            
    # ENDPOINTS STUFF
    from endpoints_polymodel import _PolyModelQueryInfo, _DowncastMessage
    def __init__(self, *args, **kwargs):
        from endpoints_polymodel import _PolyModelQueryInfo
        # Don't need to call both constructors since PolyModel doesn't define one
        # and descends from model.Model, a superclass of EndpointsModel
        super(Game, self).__init__(*args, **kwargs)
        self._endpoints_query_info = _PolyModelQueryInfo(self)
        
    @classmethod
    def ToMessageCollection(cls, items, collection_fields=None,
                            next_cursor=None):
        proto_model = cls.ProtoCollection(collection_fields=collection_fields)

        items_as_message = [item.ToMessage(fields=collection_fields)
                            for item in items]
        final_proto_class = cls.ProtoModel(fields=collection_fields)
        items_as_message = [_DowncastMessage(item, final_proto_class)
                            for item in items_as_message]

        result = proto_model(items=items_as_message)

        if next_cursor is not None:
            result.nextPageToken = next_cursor.to_websafe_string()

        return result
