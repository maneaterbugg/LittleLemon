from django.test import TestCase
from myapp.models import Menu

class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.all().delete()  # Veritabanını temizle

    def tearDown(self):
        Menu.objects.all().delete()  # Testlerden sonra veritabanını temizle

    def test_string_representation(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        expected_string = "IceCream : 80"
        self.assertEqual(str(item), expected_string)
