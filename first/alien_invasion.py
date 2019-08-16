#-*- coding:utf-8 -*-

import sys
import pygame
import game_functions as gf

from settings import Settings
from pygame.sprite import Group
from ship import Ship


def run_game():
#初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    # 创建一膄飞船
    ship = Ship(ai_settings,screen)

    bullets = Group()

    # 开始游戏的主循环
    while True:
        
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()

        gf.update_bullets(bullets)

        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
