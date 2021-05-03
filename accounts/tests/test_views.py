from .test_setup import TestSetUp
from rest_framework import status

class TestViews(TestSetUp):

    def test_user_can_signup(self):
        response = self.client.post(self.signup_url, self.signup_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_signin(self):
        response = self.client.post(self.signup_url, self.signup_data)
        import pdb
        response2 = self.client.post(self.signin_url, self.signup_data)
        # pdb.set_trace()
        self.assertEqual(response2.status_code, status.HTTP_200_OK)