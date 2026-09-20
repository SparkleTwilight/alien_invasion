import sys

import pygame

from settings import Settings
from ship import Ship

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
        
        

    def run_game(self):
        """Start the main loop for the game."""
        #Watch for keyboard and mouse events.
        while True:
            self._check_events()
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

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
         #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()