import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象

    # 初始化背景设置
    pygame.init()
    # 创建一个名为screen的显示窗口，实参元组(1000, 600)指定窗口尺寸
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于管理子弹的编组
    bullets = Group()

    # 创建一个用于管理外星人的编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens)

    # 创建一个外星人
    # alien = Alien(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        # 调用game_functions中函数
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
