import pygame
import sys
from time import sleep
from bullet import Bullet
from enemy import Alien

def check_events(game_settings, screen, stats, play_button, ship, aliens,
                    bullets):
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats, play_button,
                                ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(game_settings, screen, stats, play_button, ship, aliens,
                        bullets, mouse_x, mouse_y):
    '''Start a new game when player clicks the button'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Hides mouse cursor
        pygame.mouse.set_visible(False)
        # resets game Game stats  and settings
        game_settings.init_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet of aliens and center the ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()

def check_keydown_events(event, game_settings, screen, ship, bullets):
    # Responds to keypresses
    if event.key == pygame.K_RIGHT:
        ship.movement_right = True
    elif event.key == pygame.K_LEFT:
        ship.movement_left = True
    elif event.key == pygame.K_SPACE:
        # Creat new bullet and add it to bullets group
        fire_bullet(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    # Responds to key releases
    if event.key == pygame.K_RIGHT:
        ship.movement_right = False
    elif event.key == pygame.K_LEFT:
        ship.movement_left = False

def update_screen(game_settings, screen, stats, ship, aliens, bullets,
                    play_button):
    # Updates the images on the screen and flip to new screen
    screen.fill(game_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Draw button if game is inactive
    if not stats.game_active:
        play_button.draw_button()
    # Make the most recently drawn screen visable
    pygame.display.flip()

def update_bullets(game_settings, screen, ship, aliens, bullets):
    '''Updates position of bullets and gets ride of old bullets'''
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Check for any bullets that have hit aliens
    # If so, remove both
    check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets):
    # Check for any bullets that have hit aliens
    # If so, remove both
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 1:
        # Destroy existing bullets and create new fleet, and speed up game
        bullets.empty()
        game_settings.increase_speed()
        create_fleet(game_settings, screen, ship, aliens)

def fire_bullet(game_settings, screen, ship, bullets):
    '''Fires bullet if limit isnt reached'''
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(game_settings, alien_width):
    '''Determine # of aliens that fit in a row'''
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(game_settings, ship_height, alien_height):
    '''Determine the number of rows of aliens that fit on the screen'''
    available_space_y = (game_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    '''Create an alien and place it in the row'''
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(game_settings, screen, ship, aliens):
    '''Creates fleet of aliens'''
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height,
                                    alien.rect.height)

    # Create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(game_settings, aliens):
    '''Respond appropriately if any aliens have reached an edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break

def change_fleet_direction(game_settings, aliens):
    '''Drop entire fleet and change direction'''
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1

def ship_hit(game_settings, stats, screen, ship, aliens, bullets):
    '''Respond to ship being hit by alien'''
    if stats.ships_left > 1:
        # Decrement ships_left
        stats.ships_left -= 1
        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()
        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets):
    '''Check if aliens have reached bottom of screen'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom <= screen_rect.bottom:
            # Treat same as getting hit
            ship_hit(game_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(game_settings, stats, screen, ship, aliens, bullets):
    '''Check if fleet is at and edge, and update positions of all aliens'''
    check_fleet_edges(game_settings, aliens)
    aliens.update()
    # Look for alien-ship collisions
    check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, screen, ship, aliens, bullets)
