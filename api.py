from constants import *
from game import *
from protorpc import remote
from crazyeightsgame import *
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
        return query.filter(Game.state == GameState.STATE_CREATED)

    @CrazyEightsGame.method(path='game/add/c8',
                            http_method='POST',
                            name='game.add.c8')
    def GameAddC8(self, game):
        # Use the GameAddHelper
        game = self.GameAddHelper(game, GameType.TYPE_CRAZYEIGHTS)
        return game
        
    # Helper method to add a game with its basic features.
    def GameAddHelper(self, game, game_type):
        from deck import Deck
        # Set up the basic game model
        game.game_type = GameType.get_name(game_type)
        game.deck = Deck.get_deck(game_type)
        game.lastmodified = datetime.datetime.now()
        game.put()
        return game

    @Game.method(path='game/join/{id}',
                 http_method='POST',
                 name='game.join',
                 request_fields=('id',))
    def GameJoin(self, game):
        pass

    @CrazyEightsGame.method(request_fields=('id',),
                            path='game/start/c8/{id}',
                            http_method='GET',
                            name='game.start.c8')
    def GameStartC8(self, game):
        if not game.from_datastore:
            raise endpoints.NotFoundException('game not found.')

        logging.info('found it')
        game = self.GameStartHelper(game)
        logging.info('started it')
        
        game.put()
        
    def GameStartHelper(self, game):
        # If the game state isn't created, then we shouldn't be calling this method
        if game.state != GameState.STATE_CREATED:
            raise endpoints.BadRequestException('game already started')

        # Let the game do its initialization
        game.start()

        # Mark the game as started
        game.state = GameState.STATE_STARTED

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
