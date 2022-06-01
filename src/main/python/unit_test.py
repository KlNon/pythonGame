import unittest

import pygame

from alien_invasion import AlienInvasion
import time


class MyTestCase(unittest.TestCase):

    def test_UP(self):
        """测试上移"""
        self.game = AlienInvasion()
        self.game.run_game()
        start_time = time.time()
        while True:
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
            self.game._check_keydown_events(event)
            # 判断是否按下"上"键
            self.assertEqual(self.game.ship.moving_up, True)
            # 判断是否超出范围
            self.assertGreaterEqual(self.game.ship.rect.top, 0)
            end_time = time.time()
            flag = 0
            if end_time - start_time <= 5:
                flag += 1
                print(flag)
            if end_time - start_time > 5:
                return


if __name__ == '__main__':
    unittest.main()
