"""
@Project ：pythonGame 
@File    ：ship
@Describe：
@Author  ：KlNon
@Date    ：2022/5/27 21:34 
"""

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game) -> None:
        super().__init__()
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #         加载飞船图像并获取起外接矩形.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #         对于每艘新飞船,都将其放在屏幕底部的中央.
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中储存小数值
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

        #     子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

    def update(self):
        """根据移动标志调整飞船的位置."""
        # 更新飞船而不是rect对象的值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.x += 1
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            # self.rect.x -= 1
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        """让飞船居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.x)

    def blitme(self):
        """在指定位置绘制飞船."""
        self.screen.blit(self.image, self.rect)