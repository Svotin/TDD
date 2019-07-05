from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item

class SmokeTest(TestCase):
    '''тест домашней страницы'''
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'First Item'
        first_item.save()

        second_item = Item()
        second_item.text = "Second Item"
        second_item.save()

        saved_items = Item.objects.all()

        self.assertEqual(saved_items.count(), 2)

        first_saved = saved_items[0]
        second_saved = saved_items[1]

        self.assertEqual(first_saved.text, 'First Item')
        self.assertEqual(second_saved.text, "Second Item")



    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        response = self.client.get('/')
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')
    def test_can_save_a_POST_request(self):
        '''тест: сохоранение пост запроса'''
        response = self.client.post("/", data={"item_text":"A new list item"})
        self.assertIn("A new list item", response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


