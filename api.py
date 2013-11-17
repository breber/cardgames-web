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
                       name='game.list.all')
    def GameListAll(self, query):
        return query.filter(Game.is_active == True)

    @Game.method(path='game/add',
                 http_method='POST',
                 name='game.add')
    def GameAdd(self, game):
        # TODO: type
        # TODO: create deck
        game.is_active = True
        game.lastmodified = datetime.datetime.now()
        game.put()
        return game

application = endpoints.api_server([CardGamesApi], restricted=False)
