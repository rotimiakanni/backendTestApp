import json
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employees
from .serializers import EmployeeSerializer

Accounts = get_user_model()

class EmployeeViewTestCase(APITestCase):

    def setUp(self):
        self.user = Accounts.objects.create_user(
            email='testuser@user.com',
            password='some_password'
        )
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

    def test_get_all_employees(self):
        response = self.client.get('/employee/get-all-employees')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee(self):
        data = {
            'employee_id':'E0001',
            'first_name':'Employee',
            'last_name':'One',
            'age':24,
            'join_date':'24-03-2021'
        }
        response = self.client.post('/employee/create-employee/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class EmployeePostPutTestCase(APITestCase):

    def setUp(self):
        # self.user = Accounts.objects.create_user(
        #     email='testuser@user.com',
        #     password='some_password'
        # )
        # self.token, _ = Token.objects.get_or_create(user=self.user)
        # self.api_authentication()

        employee = Employees.objects.create(
            employee_id='E0001',
            first_name='Employee',
            last_name='Two',
            age=23,
            join_date='21-02-2020'
        )

    # def api_authentication(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

    def test_update_employee(self):
        # data = {
        #     'employee_id':'E0001',
        #     'first_name':'Employee',
        #     'last_name':'Three',
        #     'age':24,
        #     'join_date':'24-03-2021'
        # }
        # response = self.client.post('/employee/create-employee/', data)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # employees = Employees.objects.get()
        # self.assertEqual(employees[0].employee_id, 'E0001')

        data = {
            'last_name':'Two'
        }
        response = self.client.put("/employee/update-employee/'E0001'/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)