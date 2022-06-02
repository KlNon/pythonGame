import threading
import unittest
from unittest.mock import Mock

import pygame

from alien_invasion import AlienInvasion
import time


class MyTestCase(unittest.TestCase):

    def test_UP(self):
        # 判断是否按下"上"键
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
        self.mock_obj._check_keydown_events(event)
        self.assertEqual(self.mock_obj.ship.moving_up, True)
        # 休眠5秒
        time.sleep(5)
        # 5秒后判断是否超出范围
        self.assertGreaterEqual(self.mock_obj.ship.rect.top, 0)

        # 判断是否松开"上"键
        event = pygame.event.Event(pygame.KEYUP, key=pygame.K_UP)
        self.mock_obj._check_keyup_events(event)
        self.assertEqual(self.mock_obj.ship.moving_up, False)
        print("上移测试通过")

    def test_DOWN(self):
        # 判断是否按下"下"键
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
        self.mock_obj._check_keydown_events(event)
        self.assertEqual(self.mock_obj.ship.moving_down, True)
        # 休眠5秒
        time.sleep(5)
        # 5秒后判断是否超出范围,界面底部的值要大于飞船底部的值,否则就是超出界面
        self.assertGreaterEqual(self.mock_obj.screen.get_rect().bottom, self.mock_obj.ship.rect.bottom)

        # 判断是否松开"下"键
        event = pygame.event.Event(pygame.KEYUP, key=pygame.K_DOWN)
        self.mock_obj._check_keyup_events(event)
        self.assertEqual(self.mock_obj.ship.moving_down, False)
        print("下移测试通过")

    def test_RIGHT(self):
        # 判断是否按下"右"键
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
        self.mock_obj._check_keydown_events(event)
        self.assertEqual(self.mock_obj.ship.moving_right, True)
        # 休眠5秒
        time.sleep(5)
        # 5秒后判断是否超出范围,飞船右边要小于200像素,否则就是超出界面
        self.assertGreaterEqual(200, self.mock_obj.ship.rect.right)

        # 判断是否松开"下"键
        event = pygame.event.Event(pygame.KEYUP, key=pygame.K_RIGHT)
        self.mock_obj._check_keyup_events(event)
        self.assertEqual(self.mock_obj.ship.moving_right, False)
        print("右移测试通过")

    def test_LEFT(self):
        # 判断是否按下"左"键
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
        self.mock_obj._check_keydown_events(event)
        self.assertEqual(self.mock_obj.ship.moving_left, True)
        # 休眠5秒
        time.sleep(5)
        # 5秒后判断是否超出范围,飞船左边要大于0像素,否则就是超出界面
        self.assertGreaterEqual(self.mock_obj.ship.rect.left, 0)

        # 判断是否松开"左"键
        event = pygame.event.Event(pygame.KEYUP, key=pygame.K_LEFT)
        self.mock_obj._check_keyup_events(event)
        self.assertEqual(self.mock_obj.ship.moving_left, False)
        print("左移测试通过")

    def test_Space(self):
        # 连续按3次宫格
        for bullet_num in range(1, 4):
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
            self.mock_obj._check_keydown_events(event)
            event = pygame.event.Event(pygame.KEYUP, key=pygame.K_SPACE)
            self.mock_obj._check_keyup_events(event)
            # 休眠0.5秒,继续
            time.sleep(0.1)
            # 子弹数量是否等于num(当前应该正确的子弹数量)
            self.assertEqual(len(self.mock_obj.bullets), bullet_num)
        print("子弹测试通过")

    def test_ship_hit(self):
        # 模拟飞船被击中
        self.mock_obj._ship_hit()
        # 被击中一次,生命值减1
        self.assertEqual(self.mock_obj.stats.ships_left, 2)
        print("生命值减少测试通过")

    def test_super_mdoe(self):
        # 超级模式测试开启
        self.mock_obj._update_stars(True)
        # 检测超级模式标识是否正确
        self.assertEqual(self.mock_obj.stats.super_mode, True)
        # 吃掉星星飞船生命增加,由于是在飞船被击中后,因此生命值为3
        self.assertEqual(self.mock_obj.stats.ships_left, 3)
        # 子弹长度变为125
        self.assertEqual(self.mock_obj.settings.bullet_height, 125)
        # 子弹可穿透敌人
        self.assertEqual(self.mock_obj.settings.star_throw_enemy, True)
        print("超级模式测试通过")

    def test(self):
        self.mock_obj = AlienInvasion()
        mock_game = Mock(return_value=self.mock_obj)
        self.mock_obj = mock_game()

        try:
            t = threading.Thread(target=self.mock_obj.run_game)
            t.start()
            # 开始游戏
            self.mock_obj._check_play_button(None, True)
            # 上移测试
            self.test_UP()
            # 下移测试
            self.test_DOWN()
            # 右移测试
            self.test_RIGHT()
            # 左移测试
            self.test_LEFT()
            # 子弹测试
            self.test_Space()
            # 生命值减少测试
            self.test_ship_hit()
            # 超级模式测试
            self.test_super_mdoe()
        except Exception as e:
            print(e)
        finally:
            # 当运行完所有测试就退出
            self.mock_obj.quit_game_flag = True


if __name__ == '__main__':
    unittest.main()
