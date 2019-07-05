from django.test import TestCase

class SmokeTest(TestCase):
    '''тест на токсичность'''
    def test_bad_maths(self):
        '''тест на правильность мат. расчётов'''
        self.assertEqual(2+4, 4)
