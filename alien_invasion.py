#-*- coding:utf-8 -*-

import sys
import pygame
import game_functions as gf

from settings import Settings
from pygame.sprite import Group
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


def run_game():
#初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings,screen,"Play")

    #创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    alien = Alien(ai_settings,screen)

    # 创建一膄飞船
    ship = Ship(ai_settings,screen)

    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)


    # 开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

# 开始游戏
run_game()
