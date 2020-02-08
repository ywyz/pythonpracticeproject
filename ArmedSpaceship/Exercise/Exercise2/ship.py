import pygame

class Ship():

    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = 400
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.centertemp = float(self.rect.centerx)
        self.bottomtemp = float(self.rect.bottom)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_down and self.rect.bottom < 800:
            self.bottomtemp += 1
        if self.move_up and self.rect.bottom > 50:
            self.bottomtemp -= 1
        if self.move_left and self.rect.left > 0:
            self.centertemp -= 1
        if self.move_right and self.rect.centerx < 1200:
            self.centertemp += 1
        self.rect.centerx = self.centertemp
        self.rect.bottom = self.bottomtemp
