from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class SmokeTest(TestCase):
    '''тест домашней страницы'''
    def test_root_url_resolves_to_home_page(self):
        '''тест: корневой url преобразуется в представление домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)