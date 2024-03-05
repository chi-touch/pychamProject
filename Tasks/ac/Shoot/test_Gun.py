from unittest import TestCase

from ac.Shoot import Gun


class TestGun(TestCase):
    def setUp(self):
        self.gun = Gun.Gun('87cm', 30)

    def test_load_bullet(self):
        self.assertEqual(30, self.gun.get_number_of_bullets())

    def test_reload(self):
        self.gun.reload_bullets(number_of_bullets=30)
        self.assertEqual(30, self.gun.get_number_of_bullets())

    def test_shoot(self):
        self.gun.shoot_gun()
        self.assertEqual(29, self.gun.get_number_of_bullets())

    def test_safety_indicator(self):
        self.gun.safety_indicator()
        self.assertEqual(self.gun.toggle_indicator, True)


