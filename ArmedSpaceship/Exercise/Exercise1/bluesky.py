"""
创建一个背景为蓝色的pygame窗口
"""

import sys

import pygame


def run_windows():
    pygame.init()
    bg_color = (0, 0, 255)
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()


run_windows()
