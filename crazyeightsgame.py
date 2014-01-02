import game

class CrazyEightsGame(game.Game):
    discard_pile = ndb.StructuredProperty(card.Card, repeated=True)
