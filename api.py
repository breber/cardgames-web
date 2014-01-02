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
        game.lastmodified = datetime.datetime.now()
        game.put()
        return game

    @Game.method(path='game/join/{id}',
                 http_method='POST',
                 name='game.join'
                 request_fields=('id',))
    def GameJoin(self, game):
        pass

    @Game.method(path='game/start/{id}',
                 http_method='POST',
                 name='game.start',
                 request_fields=('id',))
    def GameStart(self, game):
        if not game.from_datastore:
            raise endpoints.NotFoundException('game not found.')

        # If the game state isn't created, then we shouldn't be calling this method
        if game.state != GameState.STATE_CREATED:
            raise endpoints.BadRequestException('game already started')

        # If we don't have a valid number of players, don't start the game
        if len(game.users) < 2 or len(game.users) > 5 : # TODO: do we want to allow one player games?
            raise endpoints.BadRequestException('invalid number of players')

        # Mark the game as started
        game.state = GameState.STATE_STARTED
        game.put()

        # TODO: send notification to all users

        return game

    @Game.method(path='game/move/{id}',
                 http_method='POST',
                 name='game.move',
                 request_fields=('id',))
    def GameMakeMove(self, game):
        pass

    @Game.method(path='game/status/{id}',
                 http_method='GET',
                 name='game.status',
                 request_fields=('id',))
    def GameStatus(self, game):
        if not game.from_datastore:
            raise endpoints.NotFoundException('game not found.')

        return game

application = endpoints.api_server([CardGamesApi], restricted=False)
