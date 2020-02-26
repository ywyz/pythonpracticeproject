import sys
import pygame


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen, ship, exercise_settings):
    # 填充颜色
    screen.fill(exercise_settings.bg_color)
    ship.blitme()
    # 显示屏幕
    pygame.display.flip()