import pygame

class Ship():

    def __init__(self, game_settings, screen):
        ''' Init ship and set its starting position '''
        self.screen = screen
        self.game_settings = game_settings

        # Load the ship img and get its rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value for ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.movement_right = False
        self.movement_left = False

    def update(self):
        ''' Update the ships position based on the movement flag '''
        if self.movement_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.movement_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        ''' Draw the ship at its current location '''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Center ship in the center of the screen'''
        self.center = self.screen_rect.centerx
