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

    def blitme(self):
        self.screen.blit(self.image, self.rect)
