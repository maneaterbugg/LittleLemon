from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from myapp.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Veritabanını temizleme işlemi gerekmez, test veritabanı her testten önce temizlenir
        self.menu1 = Menu.objects.create(title="Pizza", price=10.99, inventory=50)
        self.menu2 = Menu.objects.create(title="Burger", price=5.99, inventory=20)
        self.menu3 = Menu.objects.create(title="IceCream", price=3.99, inventory=30)

    def tearDown(self):
        Menu.objects.all().delete()  # Testlerden sonra veritabanını temizle

    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Test için oluşturduğumuz 3 menü öğesinin olduğunu kontrol ediyoruz
