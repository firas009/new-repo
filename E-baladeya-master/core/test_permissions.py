
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import RequestFactory, TestCase
from django.urls import reverse

from .models import Profile, User
from .permissions import administrator_required


class PermissionTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        password = "Test!SecurePassword2026"

        cls.citizen = User.objects.create_user(
            email="citizen.rbac@example.com",
            password=password,
        )

        Profile.objects.create(
            user=cls.citizen,
            role=Profile.Role.CITIZEN,
        )

        cls.employee = User.objects.create_user(
            email="employee.rbac@example.com",
            password=password,
        )

        Profile.objects.create(
            user=cls.employee,
            role=Profile.Role.EMPLOYEE,
        )

        cls.administrator = User.objects.create_user(
            email="administrator.rbac@example.com",
            password=password,
        )

        Profile.objects.create(
            user=cls.administrator,
            role=Profile.Role.ADMINISTRATOR,
        )

        cls.superuser = User.objects.create_superuser(
            email="superuser.rbac@example.com",
            password=password,
        )

        cls.staff_citizen = User.objects.create_user(
            email="staff.rbac@example.com",
            password=password,
            is_staff=True,
        )

        Profile.objects.create(
            user=cls.staff_citizen,
            role=Profile.Role.CITIZEN,
        )

        cls.no_profile = User.objects.create_user(
            email="no.profile@example.com",
            password=password,
        )

    # TEST 1: Anonymous dashboard access

    def test_anonymous_dashboard_redirects_to_login(self):

        response = self.client.get(reverse("dashboard"))

        self.assertRedirects(
            response,
            "/login/?next=/dashboard/",
        )

    # TEST 2: Anonymous employee portal access

    def test_anonymous_administration_redirects_to_login(self):

        response = self.client.get(
            reverse("employee_dashboard")
        )

        self.assertRedirects(
            response,
            "/login/?next=/administration/",
        )

    # TEST 3: Citizen dashboard access

    def test_citizen_can_access_dashboard(self):

        self.client.force_login(self.citizen)

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)

    # TEST 4: Citizen employee portal restriction

    def test_citizen_cannot_access_administration(self):

        self.client.force_login(self.citizen)

        response = self.client.get(
            reverse("employee_dashboard")
        )

        self.assertEqual(response.status_code, 403)

    # TEST 5: Citizen employee request restriction

    def test_citizen_cannot_access_employee_request_detail(self):

        self.client.force_login(self.citizen)

        response = self.client.get(
            reverse("employee_application_detail")
        )

        self.assertEqual(response.status_code, 403)

    # TEST 6: Employee portal access

    def test_employee_can_access_administration(self):

        self.client.force_login(self.employee)

        response = self.client.get(
            reverse("employee_dashboard")
        )

        self.assertEqual(response.status_code, 200)

    # TEST 7: Employee analytics access

    def test_employee_can_access_analytics(self):

        self.client.force_login(self.employee)

        response = self.client.get(reverse("analytics"))

        self.assertEqual(response.status_code, 200)

    # TEST 8: Administrator portal access

    def test_profile_administrator_can_access_administration(self):

        self.client.force_login(self.administrator)

        response = self.client.get(
            reverse("employee_dashboard")
        )

        self.assertEqual(response.status_code, 200)

    # TEST 9: Superuser portal access

    def test_superuser_can_access_administration(self):

        self.client.force_login(self.superuser)

        response = self.client.get(
            reverse("employee_dashboard")
        )

        self.assertEqual(response.status_code, 200)

    # TEST 10: Django staff flag does not grant employee access

    def test_is_staff_alone_does_not_grant_employee_access(self):

        self.client.force_login(self.staff_citizen)

        response = self.client.get(
            reverse("employee_dashboard")
        )

        self.assertEqual(response.status_code, 403)

    # TEST 11: Missing profile does not grant access

    def test_user_without_profile_cannot_access_administration(self):

        self.client.force_login(self.no_profile)

        response = self.client.get(
            reverse("employee_dashboard")
        )

        self.assertEqual(response.status_code, 403)

    # TEST 12: Employee cannot access administrator-only view

    def test_employee_cannot_use_administrator_only_view(self):

        request = RequestFactory().get("/test-admin/")
        request.user = self.employee

        protected_view = administrator_required(
            lambda request: HttpResponse("Allowed")
        )

        with self.assertRaises(PermissionDenied):
            protected_view(request)

    # TEST 13: Administrator can access administrator-only view

    def test_administrator_can_use_administrator_only_view(self):

        request = RequestFactory().get("/test-admin/")
        request.user = self.administrator

        protected_view = administrator_required(
            lambda request: HttpResponse("Allowed")
        )

        response = protected_view(request)

        self.assertEqual(response.status_code, 200)
