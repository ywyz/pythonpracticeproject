import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf


def run_ship():
    pygame.init()
    sets = Settings()
    screen = pygame.display.set_mode((sets.screen_width, sets.screen_height))
    pygame.display.set_caption("Ships")
    ship = Ship(screen)
    while True:

        gf.check_events(ship)
        ship.update()

        gf.update_screen(sets, screen, ship)
        screen.fill(sets.bg_color)


run_ship()
