from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Customuser
from .serializers import RegisterSerializers
import funcs


class UserTests(APITestCase):

    def setUp(self):
        """
        تنظیمات اولیه برای هر تست
        """
        self.client = APIClient()
        self.register_url = reverse('register')  # اطمینان حاصل کنید که این نام URL صحیح است
        self.login_url = reverse('login')
        self.active_code_url = reverse('active_code')
        self.change_password_url = reverse('change_password')

        # ایجاد یک کاربر تست
        self.user = Customuser.objects.create_user(
            mobile_number="09123456789",
            password="testpass123",
            is_active=True
        )
    def test_register_user(self):
        """
        تست ثبت کاربر جدید
        """
        data = {
            'mobile_number': '09987654321',
            'password': 'newpassword'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        """
        تست ورود کاربر با شماره موبایل و رمز عبور صحیح
        """
        data = {
            'mobile_number': '09123456789',
            'password': 'testpass123'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activate_user(self):
        """
        تست فعال‌سازی کاربر با کد فعال‌سازی صحیح
        """
        self.user.active_code = funcs.create_random_code(5)
        self.user.save()

        data = {
            'active_code': self.user.active_code
        }
        response = self.client.post(self.active_code_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_password(self):
        """
        تست تغییر رمز عبور کاربر
        """
        data = {
            'password': 'newpassword123'
        }
        self.client.session['user_info'] = {
            'mobile_number': self.user.mobile_number,
            'active_code': self.user.active_code
        }
        response = self.client.post(self.change_password_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)