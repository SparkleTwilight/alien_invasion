import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assests and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        #Ensure that the frame rate runs consistently on most systems
        self.clock = pygame.time.Clock()
        self.settings = Settings()  #This accesses the settings in the Settings class
                                    #by creating an instance of a settings object.

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
        

    def run_game(self):
        """Start the main loop for the game."""
        #Watch for keyboard and mouse events.
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            #Set the frame rate to 60 frames/sec
            self.clock.tick(60)  
           
    #The following known as a helper method,
    #which is written with a single underscore before its name.
    #Helper methods cannot be accessed outside of the class.
    def _check_events(self): 
        """Respond to keypreses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)    

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Move ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Create the fleet of aliens"""
        #Create an alien and keep adding aliens until there's no room left.
        #Spacing between aliens is one alien width.
        alien = Alien(self)
        self.aliens.add(alien)
       # alien_width = alien.rect.width

       # current_x = alien.width
        #while current_x < (self.settings.screen_width - 2 * alien_width):
         #   new_alien = Alien(self)
         #   new_alien.x = current_x
         #   new_alien.rect.x = current_x
         #   self.aliens.add(new_alien)
         #   current_x += 2 * alien_width


    def _fire_bullet(self):
        """Create a new bullet and add it to teh bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update bullet positions.
        self.bullets.update()
                   
        #Get rid of old bullets that have disappered
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
         #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()