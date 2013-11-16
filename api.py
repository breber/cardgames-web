from protorpc import remote
from models import *
import datetime
import endpoints
import logging

@endpoints.api(name='cardgames',
               version='v1',
               description='CardGames API',
               hostname='worthwhile-games.appspot.com')
class CardGamesApi(remote.Service):

    @Game.query_method(path='game/list/all',
                       name='game.list.all',)
    def GameListAll(self, query):
        return query.filter(Game.is_active == True)

application = endpoints.api_server([CardGamesApi], restricted=False)
