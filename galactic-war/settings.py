
class Settings():
    ''' Stores all settings for Galactic War '''

    def __init__(self):
        ''' Init the game's static settings '''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 20
        self.fleet_direction = 1 # 1 is right, -1 is left

        # How fast the game speeds up
        self.speedup_scale = 1.6

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        ''' Init seetings that change throughout the game '''
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Fleet direction of 1 means right, -1 is left
        self.fleet_direction = 1

    def increase_speed(self):
        '''Increase speed settings'''
        self.ship_speed_factor  *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        # Allows you to fire extra bullet every round
        self.bullets_allowed += 1
