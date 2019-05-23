import pygame.font

class Scoreboard():
    '''A class to report score info'''
    def __init__(self, game_settings, screen, stats):
        '''Init scorekeeping attributes'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        # Font seetings for score info
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(none, 48)

        # Prepare the init score img
        self.prep_score()

    def prep_score(self):
        '''Turn the score into a rendered image'''
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                                self.game_settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect = 20

    def show_score(self):
        ''' Draw score to the screen '''
        self.screen.blit(self.score_image, self.score_rect)
