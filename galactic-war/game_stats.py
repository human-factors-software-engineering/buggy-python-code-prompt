class GameStats():
    '''Track stats for the game'''


    def __init__(self, game_settings):
        '''Init stats'''
        self.game_settings = game_settings
        self.reset_stats()
        # Start game in active state
        self.game_active = False

    def reset_stats(self):
        '''Init stats that can be changed in the game'''
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
