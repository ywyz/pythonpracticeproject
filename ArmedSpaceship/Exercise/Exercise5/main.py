import pygame
from settings import Settings
import game_function as gf
from ship import Ship


def main():
    # 初始化游戏
    pygame.init()
    exercise_settings = Settings()
    screen = pygame.display.set_mode((exercise_settings.screen_width, exercise_settings.screen_height))
    # 设置背景色
    pygame.display.set_caption(exercise_settings.screen_name)

    # 创建一艘飞船
    ship = Ship(screen)

    while True:

        gf.check_events()

        gf.update_screen(screen, ship, exercise_settings)


main()
