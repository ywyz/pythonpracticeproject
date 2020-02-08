import sys

import pygame

import ship


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.move_right = True
            elif event.key == pygame.K_LEFT:
                ship.move_left = True
            elif event.key == pygame.K_UP:
                ship.move_up = True
            elif event.key == pygame.K_DOWN:
                ship.move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_LEFT:
                ship.move_left = False
            elif event.key == pygame.K_UP:
                ship.move_up = False
            elif event.key == pygame.K_DOWN:
                ship.move_down = False


def update_screen(ai_settings, screen, ship):
    ship.blitme()

    pygame.display.flip()
