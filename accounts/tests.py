import json
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status


class SignupTestCase(APITestCase):

    def test_signup(self):
        data = {
            'email':'test@user.com',
            'password':'some_password'
        }
        response = self.client.post('/accounts/signup/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
