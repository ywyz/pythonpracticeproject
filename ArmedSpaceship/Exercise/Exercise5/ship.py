import pygame


class Ship():

    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将新飞船放在屏幕右侧中央
        self.rect.centerx = self.screen_rect.right
        self.rect.bottom = self.screen_rect.centery
        self.move_up = False
        self.move_down = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_up:
            self.rect.bottom -= 1

        if self.move_down:
            self.rect.bottom += 1
