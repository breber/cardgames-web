from constants import *
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
        from deck import Deck
        # TODO: type configurable
        game_type = GameType.TYPE_CRAZYEIGHTS

        # Set up the basic game model and store it
        game.game_type = GameType.get_name(game_type)
        game.deck = Deck.get_deck(game_type)
        game.is_active = True
        game.lastmodified = datetime.datetime.now()
        game.put()
        return game

    @Game.method(path='game/join',
                 http_method='POST',
                 name='game.join')
    def GameJoin():
        pass

    @Game.method(path='game/start',
                 http_method='POST',
                 name='game.start')
    def GameStart():
        pass

    @Game.method(path='game/move',
                 http_method='POST',
                 name='game.move')
    def GameMakeMove():
        pass

    @Game.method(path='game/status',
                 http_method='POST',
                 name='game.status')
    def GameStatus():
        pass

application = endpoints.api_server([CardGamesApi], restricted=False)
