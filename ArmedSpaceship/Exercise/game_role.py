import pygame
import sys
from ship import Ship

def run_windows():
    pygame.init()
    bg_color = (0, 0, 255)
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")
    ship = Ship(screen)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()


run_windows()