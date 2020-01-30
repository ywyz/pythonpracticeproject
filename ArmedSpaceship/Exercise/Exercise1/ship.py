"""
将图片绘制到屏幕中央，并更改图片背景颜色
"""
import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.bottom = 400

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.center = float(self.rect.center)
        self.bottom = float(self.rect.bottom)

    def update(self):
        if self.move_left:
            self.center -= 1
        if self.move_right:
            self.center += 1
        if self.move_up:
            self.bottom -= 1
        if self.move_down:
            self.bottom += 1

        self.rect.center = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
