import pygame
from .settings import Settings
import sys


def main():
    # 初始化游戏
    pygame.init()
    exercise_settings = Settings()
    screen = pygame.display.set_mode((exercise_settings.screen_width, exercise_settings.screen_height))
    # 设置背景色
    pygame.display.set_caption(exercise_settings.screen_name)

    while True:

        # 监视鼠标活动
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 填充颜色
        screen.fill(exercise_settings.bg_color)

        # 显示屏幕
        pygame.display.flip()


main()
