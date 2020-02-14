import pygame
import sys


def button():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Button")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
            elif event.type == pygame.KEYUP:
                continue
            elif event.type == pygame.QUIT:
                sys.exit()


button()
