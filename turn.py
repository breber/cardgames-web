from google.appengine.ext import ndb

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