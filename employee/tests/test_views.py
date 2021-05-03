from .test_setup import TestSetUp
from rest_framework import status
from django.contrib.auth import get_user_model
from employee.models import Employees
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

Accounts = get_user_model()

class TestViews(APITestCase):

    def setUp(self):
        self.user = Accounts.objects.create_user(
                email='testuser@user.com',
                password='some_password'
            )
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.api_authentication()

        Employees.objects.create(
            employee_id='E0002',
            first_name='firstname2',
            last_name='lastname2',
            age=23,
            join_date='23-03-2021'
        )
        Employees.objects.create(
            employee_id='E0003',
            first_name='firstname3',
            last_name='lastname3',
            age=24,
            join_date='23-03-2021'
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

    def test_get_all_employees(self):
        response = self.client.get('/employee/get-all-employees')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), len(Employees.objects.all()))
    
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

    def test_get_employee(self):
        import pdb
        response = self.client.get('/employee/get-employee/E0002')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'firstname2')

    def test_update_employee(self):
        data = {
            'employee_id':'E0001',
            'first_name':'Employee',
            'last_name':'One',
            'age':25,
            'join_date':'24-03-2021'
        }
        response = self.client.put('/employee/update-employee/E0002/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employees.objects.get(employee_id='E0001').age, 25)

    def test_delete_employee(self):
        response = self.client.delete('/employee/delete-employee/E0002')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Employees.objects.all()), 1)