from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):
    def test_instance(self):
        menu = Menu.objects.create(Title='Ice cream', Price=80, Inventory = 100)
        result = f'{menu.Title} : {menu.Price}'
        self.assertEqual(result, 'Ice cream : 80')