from protorpc import remote
from models import *
import datetime
import endpoints
import logging

@endpoints.api(name='cardgames',version='v1',
               description='CardGames API',
               hostname='worthwhile-games.appspot.com',
               audiences=carhubkeys.AUDIENCES,
               allowed_client_ids=carhubkeys.ALLOWED_CLIENT_IDS)
class CarHubApi(remote.Service):

    @Game.query_method(user_required=True,
                       path='game/list',
                       name='game.list',
                       query_fields=('order', 'pageToken', 'modified_since'))
    def GameList(self, query):
        return query

application = endpoints.api_server([CardGamesApi], restricted=False)
