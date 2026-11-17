from django.test import Client, TestCase
from django.urls import reverse

from .models import User, Profile



class RegistrationTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.existing_user = User.objects.create_user(
            email="existing@example.com",
            password="Existing!SecurePassword2026",
            first_name="Existing",
            last_name="Citizen",
        )

        Profile.objects.create(
            user=cls.existing_user,
            role=Profile.Role.CITIZEN,
        )

    def registration_data(self, **overrides):

        data = {
            "first_name": "Test",
            "last_name": "Citizen",
            "email": "new.citizen@example.com",
            "phone": "",
            "cin": "",
            "password1": "Test!SecurePassword2026",
            "password2": "Test!SecurePassword2026",
        }

        data.update(overrides)

        return data


    def test_registration_page_loads(self):

        response = self.client.get(reverse("register"))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="password2"')


    def test_registration_creates_user_and_profile(self):

        data = self.registration_data()

        response = self.client.post(
            reverse("register"),
            data,
        )

        self.assertRedirects(response, reverse("login"))

        user = User.objects.get(
            email="new.citizen@example.com"
        )

        self.assertTrue(
            user.check_password(data["password1"])
        )

        self.assertNotEqual(
            user.password,
            data["password1"]
        )

        self.assertEqual(
            user.profile.role,
            Profile.Role.CITIZEN
        )

        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_duplicate_email_is_rejected(self):

        data = self.registration_data(
            email="EXISTING@EXAMPLE.COM"
        )

        response = self.client.post(
            reverse("register"),
            data,
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            "email",
            response.context["form"].errors
        )

        self.assertEqual(User.objects.count(), 1)


    def test_password_mismatch_is_rejected(self):

        data = self.registration_data(
            password2="Different!Password2026"
        )

        response = self.client.post(
            reverse("register"),
            data,
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            "password2",
            response.context["form"].errors
        )

        self.assertEqual(User.objects.count(), 1)


    def test_weak_password_is_rejected(self):

        data = self.registration_data(
            password1="123",
            password2="123",
        )

        response = self.client.post(
            reverse("register"),
            data,
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            "password2",
            response.context["form"].errors
        )

        self.assertEqual(User.objects.count(), 1)


    def test_citizen_cannot_assign_admin_privileges(self):

        data = self.registration_data()

        data.update({
            "role": "administrator",
            "is_staff": "true",
            "is_superuser": "true",
        })

        response = self.client.post(
            reverse("register"),
            data,
        )

        self.assertRedirects(response, reverse("login"))

        user = User.objects.get(
            email="new.citizen@example.com"
        )

        self.assertEqual(
            user.profile.role,
            Profile.Role.CITIZEN
        )

        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_registration_requires_csrf(self):

        csrf_client = Client(enforce_csrf_checks=True)

        csrf_client.get(reverse("register"))

        response = csrf_client.post(
            reverse("register"),
            self.registration_data(),
        )

        self.assertEqual(response.status_code, 403)

        self.assertFalse(
            User.objects.filter(
                email="new.citizen@example.com"
            ).exists()
        )



class LoginLogoutTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.email = "login.citizen@example.com"
        cls.password = "Login!SecurePassword2026"

        cls.citizen = User.objects.create_user(
            email=cls.email,
            password=cls.password,
            first_name="Login",
            last_name="Citizen",
        )

        Profile.objects.create(
            user=cls.citizen,
            role=Profile.Role.CITIZEN,
        )

    def test_login_with_correct_credentials(self):

        response = self.client.post(
            reverse("login"),
            {
                "username": self.email,
                "password": self.password,
            },
        )

        self.assertRedirects(
            response,
            reverse("dashboard")
        )

        self.assertEqual(
            int(self.client.session["_auth_user_id"]),
            self.citizen.pk
        )


    def test_login_email_is_case_insensitive(self):

        response = self.client.post(
            reverse("login"),
            {
                "username": self.email.upper(),
                "password": self.password,
            },
        )

        self.assertRedirects(
            response,
            reverse("dashboard")
        )


    def test_login_rejects_incorrect_password(self):

        response = self.client.post(
            reverse("login"),
            {
                "username": self.email,
                "password": "WrongPassword!",
            },
        )

        self.assertEqual(response.status_code, 200)

        self.assertTrue(
            response.context["form"].non_field_errors()
        )

        self.assertNotIn(
            "_auth_user_id",
            self.client.session
        )


    def test_inactive_user_cannot_login(self):

        self.citizen.is_active = False
        self.citizen.save(update_fields=["is_active"])

        response = self.client.post(
            reverse("login"),
            {
                "username": self.email,
                "password": self.password,
            },
        )

        self.assertEqual(response.status_code, 200)

        self.assertNotIn(
            "_auth_user_id",
            self.client.session
        )


    def test_logout_rejects_get_requests(self):

        self.client.force_login(self.citizen)

        response = self.client.get(
            reverse("logout")
        )

        self.assertEqual(response.status_code, 405)

        self.assertIn(
            "_auth_user_id",
            self.client.session
        )


    def test_logout_clears_authenticated_session(self):

        self.client.force_login(self.citizen)

        self.assertIn(
            "_auth_user_id",
            self.client.session
        )

        response = self.client.post(
            reverse("logout")
        )

        self.assertRedirects(
            response,
            reverse("login")
        )

        self.assertNotIn(
            "_auth_user_id",
            self.client.session
        )

        login_response = self.client.get(
            reverse("login")
        )

        self.assertEqual(
            login_response.status_code,
            200
        )


    def test_logout_requires_csrf(self):

        csrf_client = Client(
            enforce_csrf_checks=True
        )

        csrf_client.force_login(self.citizen)

        response = csrf_client.post(
            reverse("logout")
        )

        self.assertEqual(
            response.status_code,
            403
        )

        self.assertIn(
            "_auth_user_id",
            csrf_client.session
        )
