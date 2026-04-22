from django.test import TestCase, Client
from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.storage import staticfiles_storage

class WhereCryptoUnitTests(TestCase):
    def setUp(self):
        self.client = Client()
        self._old_storage = staticfiles_storage._wrapped
        staticfiles_storage._wrapped = FileSystemStorage()

    def test_home_page_status_code(self):
        """Перевірка доступності головної сторінки"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_map_page_status_code(self):
        """Перевірка доступності сторінки карти"""
        response = self.client.get('/map')
        self.assertEqual(response.status_code, 200)

    def test_cryptocurrencies_page_status_code(self):
        """Перевірка сторінки криптовалют"""
        response = self.client.get('/cryptocurrencies')
        self.assertEqual(response.status_code, 200)

    def test_search_page_loads(self):
        """Перевірка сторінки пошуку"""
        response = self.client.get('/search')
        self.assertEqual(response.status_code, 200)

    def test_search_functionality(self):
        """Тест логіки пошуку з параметром"""
        response = self.client.get('/search', {'q': 'Ukraine'})
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        staticfiles_storage._wrapped = self._old_storage