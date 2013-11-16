class Constants:

    ''' GUI '''
    '''A constant to limit the number of characters for a players name'''
    NAME_MAX_CHARS = 10

    '''The maximum number of cards to be displayed on longest sides of tablet'''
    MAX_DISPLAYED = 12

    '''The maximum number of cards to be displayed on shortest sides of tablet'''
    MAX_DIS_SIDES = 6

    '''A constant to represent the name of the font to use'''
    FONT_NAME = 'hammersmithone.ttf'

    '''A constant to scale a card to the full card size'''
    fullCard = 1

    '''A constant to scale a card to half the card size horizontally cut'''
    halfCard = 2

    '''A constant to scale a card to half of the card size vertically cut'''
    halfCardVertCut = 3

    '''A constant to scale a card to a fourth of the size'''
    fourthCard = 4


    ''' Game Constants '''
    '''The default maximum number of players allowed'''
    DEFAULT_MAX_PLAYERS = 4

    '''A constant to represent the Clubs suit'''
    SUIT_CLUBS = 0

    '''A constant to represent the Diamonds suit'''
    SUIT_DIAMONDS = 1

    '''A constant to represent the Spades suit'''
    SUIT_SPADES = 3

    '''A constant to represent the Hearts suit'''
    SUIT_HEARTS = 2

    '''A constant to represent the jokers'''
    SUIT_JOKER = 4

    '''A constant for the ace card value'''
    ACE_VALUE = 0

    '''A constant for the two card value'''
    TWO_VALUE = 1

    '''A constant for the three card value'''
    THREE_VALUE = 2

    '''A constant for the four card value'''
    FOUR_VALUE = 3

    '''A constant for the five card value'''
    FIVE_VALUE = 4

    '''A constant for the six card value'''
    SIX_VALUE = 5

    '''A constant for the seven card value'''
    SEVEN_VALUE = 6

    '''A constant for the eight card value'''
    EIGHT_VALUE = 7

    '''A constant for the nine card value'''
    NINE_VALUE = 8

    '''A constant for the ten card value'''
    TEN_VALUE = 9

    '''A constant for the jack card value'''
    JACK_VALUE = 10

    '''A constant for the queen card value'''
    QUEEN_VALUE = 11

    '''A constant for the king card value'''
    KING_VALUE = 12

    '''A constant for the king card value'''
    BLACK_JOKER_VALUE = 0

    '''A constant for the king card value'''
    RED_JOKER_VALUE = 1

    '''This is used by the connections screen to pass the player 1 name thathave been entered'''
    PLAYER_1 = 'player1'

    '''This is used by the connections screen to pass the player 2 name thathave been entered'''
    PLAYER_2 = 'player2'

    '''This is used by the connections screen to pass the player 3 name thathave been entered'''
    PLAYER_3 = 'player3'

    '''This is used by the connections screen to pass the player 4 name thathave been entered'''
    PLAYER_4 = 'player4'

    ''' JSON keys '''
    '''this is a JSON key for the suit of a card'''
    KEY_SUIT = 'suit'

    '''this is a JSON key for the value of a card'''
    KEY_VALUE = 'value'

    '''this is a JSON key for a card id'''
    KEY_CARD_ID = 'id'

    '''this is the key for message type this is used to obtain the message typeinformation from the message sent over wireless'''
    KEY_MESSAGE_TYPE = 'messagetype'

    '''this is a JSON key for getting the isTurn boolean'''
    KEY_TURN = 'isturn'

    '''this is a JSON key for getting the player name'''
    KEY_PLAYER_NAME = 'playername'

    '''This is a JSON key for telling the player what state the game is in'''
    KEY_CURRENT_STATE = 'currentstate'

    '''This is a JSON key for telling the player what cards are in their hand'''
    KEY_CURRENT_HAND = 'currenthand'

    '''This is a JSON key for telling the player the current discard card'''
    KEY_DISCARD_CARD = 'discardCard'

    '''TODO'''
    '''this is a request code for the get EnterNameActivity'''
    '''GET_PLAYER_NAME = Math.abs('GET_PLAYER_NAME'.hashCode())'''

    ''' wireless connection message codes '''
    '''message type for setting up a game'''
    MSG_SETUP = 0

    '''message type for telling a player it is their turn'''
    MSG_IS_TURN = 1

    '''message type for sending the card that was drawn'''
    MSG_CARD_DRAWN = 2

    '''message type telling the player they won'''
    MSG_WINNER = 3

    '''message type telling the player they lost'''
    MSG_LOSER = 4

    '''message type for refreshing the game state by re-sending cards and whoseturn it is to all players'''
    MSG_REFRESH = 5

    '''message type for pausing the game'''
    MSG_PAUSE = 6

    '''message type for unpausing the game'''
    MSG_UNPAUSE = 7

    '''message type for telling the players to end their game'''
    MSG_END_GAME = 8

    '''message types that a player sends when playing a card'''
    MSG_PLAY_CARD = 9

    '''message type that a player sends when requesting to draw a card'''
    MSG_DRAW_CARD = 10

    '''message type that a player sends when requesting to draw a card'''
    MSG_PLAY_AGAIN = 11

    '''message type for the player name'''
    MSG_PLAYER_NAME = 12

    '''message type for suggested card'''
    MSG_SUGGESTED_CARD = 13

    ''' Preferences Options '''
    '''The name of the shared preferences to be used when getting the object'''
    PREFERENCES = 'PREFERENCES'

    '''A constant representing the difficulty of the AI players in the game forthe preferences'''
    PREF_DIFFICULTY = 'DIFFICULTY OF COMPUTERS'

    '''A constant representing the computer difficulty easy'''
    EASY = 'Easy'

    '''A constant representing the computer difficulty medium'''
    MEDIUM = 'Medium'

    '''A constant representing the computer difficulty hard'''
    HARD = 'Hard'

    '''A constant representing the connection type for the shared preferences'''
    PREF_CONNECTION_TYPE = 'CONNECTION TYPE'

    '''A constant to represent a key in the shared preferences for the soundeffects option'''
    PREF_SOUND_EFFECTS = 'SOUND EFFECTS'

    '''A constant to represent a key in the shared preferences for the speechvolume option'''
    PREF_SPEECH_VOLUME = 'SPEECH VOLUME'

    '''A constant to represent a key in the shared preferences for thelanguage/locale option'''
    PREF_LANGUAGE = 'LANGUAGE'

    '''A constant to represent a key in the shared preferences for the number ofcomputers in the game option'''
    PREF_NUMBER_OF_COMPUTERS = 'NUMBER OF COMPUTERS'

    '''A constant to represent a key in the shared preferences for the game type'''
    PREF_GAME_TYPE = 'GAME TYPE'

    '''A constant to represent a key in the shared preferences for the imageresource to use as the back of the card'''
    PREF_CARD_BACK = 'BACKOFCARD'

    '''A constant to represent cheater mode'''
    PREF_CHEATER_MODE = 'CHEATERMODE'

    '''A constant to represent a key in the shared preferences for the speechvolume option'''
    PREF_PLAY_ASSIST_MODE = 'PLAY ASSIST MODE'

    '''Does this device have TTS?'''
    PREF_HAS_TTS = 'PREF_HAS_TTS'

    ''' AI Constants '''
    '''The time you wait in between computer turns, about 1 and a half secondsnow'''
    COMPUTER_WAIT_TIME = 1500

