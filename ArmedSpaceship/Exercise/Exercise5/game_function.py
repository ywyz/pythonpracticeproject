import sys
import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.move_up = True
            elif event.key == pygame.K_DOWN:
                ship.move_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ship.move_up = False
            elif event.key == pygame.K_DOWN:
                ship.move_down = False


def update_screen(screen, ship, exercise_settings):
    # 填充颜色
    screen.fill(exercise_settings.bg_color)
    ship.blitme()
    ship.update()
    # 显示屏幕
    pygame.display.flip()