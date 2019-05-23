import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represnt a single alien fleet'''
    def __init__(self, game_settings, screen):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Load alien image and set its rect attribute
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens extact position
        self.x = float(self.rect.x)

    def blitme(self):
        '''Draw the alien at its current location'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''Returns true if alien is at the edge of screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return False

    def update(self):
        '''Move the alien right'''
        self.x += (self.game_settings.alien_speed_factor *
                    self.game_settings.fleet_direction)
        self.rect.x = self.x
