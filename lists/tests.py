from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

class SmokeTest(TestCase):
    '''тест домашней страницы'''
    def test_root_url_resolves_to_home_page(self):
        '''тест: корневой url преобразуется в представление домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        request = HttpRequest()
        responce = home_page(request)
        html = responce.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))


