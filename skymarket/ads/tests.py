# from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from ads.models import Ad
from users.models import User, UserRoles


# Create your tests here.


class AdsTestCase(APITestCase):
    """
    Класс для тестов модели Ad.
    """

    def setUp(self) -> None:
        """
        Метод подготавливает данные тестового пользователя перед каждым тестом.
        """
        self.user = User.objects.create(
            id=1,
            email='testuser@example.com',
            first_name='User',
            last_name='Us',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.USER,
        )
        self.user.set_password('testpassword')
        self.user.save()

        # Получаем токен авторизации
        response = self.client.post('/api/token/',
                                    {'email': 'testuser@example.com', 'password': 'testpassword'})
        self.access_token = response.json().get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_model_name = 'ad_for_test'

        self.test_ad_data = {
            "author": self.user,
            'title': 'ad_for_test',
            "price": "8888",
            "description": "Test Ad Description",
        }
        self.ad = Ad.objects.create(**self.test_ad_data)

    def test_ad_create(self):
        """
        Метод тестирует создание объявления.
        """
        ad_test = Ad.objects.create(title=self.test_model_name,
                                    price="8888",
                                    description="Test Ad Description",
                                    author=self.user, )
        response = self.client.post('/api/ads/', {'title': 'test2',
                                                  'price': '8888',
                                                  'description': 'Test Ad Description',
                                                  'author': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ad_test.title, 'ad_for_test')

    def test_ad_update(self):
        """
        Метод тестирует изменение созданного объявления.
        """
        self.test_ad_create()
        ad_id = self.ad.pk
        # ad_id = 4
        response = self.client.patch(
            reverse('ads:ads-detail', args=[ad_id]), {'title': 'test2',
                                                      'price': '5555',
                                                      'description': 'Test Ad Description',
                                                      'author': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ad.objects.filter(price=5555).exists(), True)

    def test_get_ad(self):
        """
        Метод тестирует просмотр созданного объявления.
        """
        self.test_ad_create()
        ad_id = self.ad.pk
        # ad_id = 4
        response = self.client.get(
            reverse('ads:ads-detail', args=[ad_id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ad.objects.filter(pk=ad_id).exists(), True)

    def test_list_ads(self):
        """
        Метод тестирует просмотр листа объявлений.
        """
        self.test_ad_create()
        response = self.client.get('/api/ads/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ad.objects.all().count(), 3)

    def test_ad_delete(self):
        """
        Метод тестирует удаление созданного объявления.
        """
        ad_id = self.ad.pk
        response = self.client.delete(
            reverse('ads:ads-detail', args=[ad_id])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ad.objects.filter(pk=ad_id).exists(), False)


class SuperuserTestCase(APITestCase):
    """
    Класс для теста superuser.
    """

    def setUp(self) -> None:
        """
        Метод подготавливает данные тестового superuser для теста.
        """
        self.superuser = User.objects.create(
            email='testadmin@example.com',
            first_name='Admin',
            last_name='Adm',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role=UserRoles.ADMIN,
        )
        self.superuser.set_password('testpassword')
        self.superuser.save()

        # Получаем токен авторизации
        response = self.client.post('/api/token/',
                                    {"email": "testadmin@example.com", "password": "testpassword"})
        self.access_token = response.json().get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_users_get(self):
        """
        Метод тестирует вывод/отображение созданного superuser.
        """
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
