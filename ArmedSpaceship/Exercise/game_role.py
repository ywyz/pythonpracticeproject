"""
将图片绘制到屏幕中央，并更改图片背景颜色
"""
import pygame
import sys
from ship import Ship


def run_windows():
    pygame.init()
    bg_color = (255, 255, 255)
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