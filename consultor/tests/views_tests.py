from django.contrib.auth.models import User
from django.test import TestCase


class ViewsTest(TestCase):

    def test_create_register(self):

        response = self.client.post(
            "/api/auth/register/",
            data = {
                "username": "test",
                "email": "test@gmail.com",
                "password": "test1234"
            },
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            User.objects.filter(username="test").exists()
        )
    def test_register_duplicate_username(self):

        User.objects.create_user(
            username="test",
            email="test1@gmail.com",
            password="test1234",
        )

        response = self.client.post(
            "/api/auth/register/",
            data={
                "username": "test",
                "email": "test2@gmail.com",
                "password": "test1234",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)


class LoginTests(TestCase):

    def setUp(self):

        self.password = "test1234"
        
        self.user = User.objects.create_user(
            username = "test",
            email = "test@gmail.com",
            password = self.password 
        )

    def test_login(self):

        response = self.client.post( 
            "/api/auth/login/",
            data = {
                "username" : self.user.username,
                "password" : self.password
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code,200)
        self.assertIn("access_token", response.cookies)
        self.assertIn("refresh_token", response.cookies)

    def test_login_incorrect_password(self):

        response = self.client.post( 
            "/api/auth/login/",
            data = {
                "username" : self.user.username,
                "password" : "1234test"
            },
            content_type="application/json",
        )
        
        self.assertEqual(response.status_code,401)
        self.assertNotIn("access_token", response.cookies)
        self.assertNotIn("refresh_token", response.cookies)


# class AIAskTest(TestCase):

#     def setUp(self):

#         self.user = User.objects.create_user(
#             username="test",
#             email="test@gmail.com",
#             password="test1234",
#         )

#     def test_ask_requires_authentication(self):

#         response = self.client.post(
#             f"/api/ask/",
#             data={
#                 "message": "What is Docker?",
#                 "mode": "consultor",
#             },
#             content_type="application/json",
#         )

#         self.assertEqual(response.status_code, 401)

#     def test_ask_authenticated(self):

#         refresh = RefreshToken.for_user(self.user)
#         access_token = refresh.access_token

#         self.client.cookies["access_token"] = str(access_token)

#         response = self.client.post(
#             "/api/ask/",
#             data={
#                 "message": "What is Docker?",
#                 "mode": "consultor",
#             },
#             content_type="application/json",
#         )

#         self.assertEqual(response.status_code, 201)

#     def test_ai_response_create_model_doubt(self):

#         refresh = RefreshToken.for_user(self.user)
#         access_token = refresh.access_token

#         self.client.cookies["access_token"] = str(access_token)

#         response = self.client.post(
#             "/api/ask/",
#             data={
#                 "message": "What is Docker?",
#                 "mode": "consultor",
#             },
#             content_type="application/json",
#         )

#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Doubt.objects.count(), 1)

#         doubt = Doubt.objects.first()

#         self.assertEqual(doubt.user, self.user)
#         self.assertEqual(doubt.question, "What is Docker?")
#         self.assertEqual(doubt.mode, "consultor")