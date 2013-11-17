class Constants:
    SUIT_CLUBS = 0
    SUIT_DIAMONDS = 1
    SUIT_SPADES = 3
    SUIT_HEARTS = 2
    SUIT_JOKER = 4
    ACE_VALUE = 0
    TWO_VALUE = 1
    THREE_VALUE = 2
    FOUR_VALUE = 3
    FIVE_VALUE = 4
    SIX_VALUE = 5
    SEVEN_VALUE = 6
    EIGHT_VALUE = 7
    NINE_VALUE = 8
    TEN_VALUE = 9
    JACK_VALUE = 10
    QUEEN_VALUE = 11
    KING_VALUE = 12
    BLACK_JOKER_VALUE = 0
    RED_JOKER_VALUE = 1

class GameType:
    TYPE_CRAZYEIGHTS = 0

    @classmethod
    def get_name(cls, game_type):
        if game_type == GameType.TYPE_CRAZYEIGHTS:
            return "CrazyEights"

        return None
