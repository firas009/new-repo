
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.db.models.deletion import ProtectedError
from django.test import TestCase

from core.models import (
    Profile,
    MunicipalService,
    RequiredDocument,
    Application,
    UploadedDocument,
    DocumentVerification,
    VerificationCheck,
    ApplicationEvent,
    EmployeeComment,
    Notification,
    GeneratedDocument,
)


class DatabaseIntegrityTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()

        cls.citizen = User.objects.create_user(
            email="citizen-test@example.com",
            password="TestOnlyPassword123!"
        )

        cls.service = MunicipalService.objects.create(
            name="Test Birth Certificate",
            slug="test-birth-certificate",
            category="Civil status",
            category_slug="civil-status",
            description="A test municipal service"
        )

        cls.other_service = MunicipalService.objects.create(
            name="Test Building Permit",
            slug="test-building-permit",
            category="Urbanism",
            category_slug="urbanism",
            description="Another test service"
        )

        cls.requirement = RequiredDocument.objects.create(
            service=cls.service,
            name="Identity document"
        )

        cls.other_requirement = RequiredDocument.objects.create(
            service=cls.other_service,
            name="Building plan"
        )

        cls.application = Application.objects.create(
            applicant=cls.citizen,
            service=cls.service,
            reference_number="REQ-TEST-00001"
        )

    def make_upload(self, version=1, active=True,
                    status=UploadedDocument.Status.PENDING):
        # String path only: no physical file is written.
        return UploadedDocument.objects.create(
            application=self.application,
            required_document=self.requirement,
            file=f"test-only/version-{version}.pdf",
            original_name=f"version-{version}.pdf",
            version=version,
            is_active=active,
            status=status
        )

    def test_01_profile_relationship(self):
        profile = Profile.objects.create(
            user=self.citizen,
            role=Profile.Role.CITIZEN
        )

        self.assertEqual(self.citizen.profile, profile)

    def test_02_duplicate_email_rejected(self):
        User = get_user_model()

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                User.objects.create_user(
                    email="citizen-test@example.com",
                    password="AnotherTestPassword123!"
                )

    def test_03_duplicate_service_slug_rejected(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                MunicipalService.objects.create(
                    name="Duplicate test service",
                    slug="test-birth-certificate",
                    category="Testing",
                    category_slug="testing",
                    description="Duplicate slug test"
                )

    def test_04_duplicate_reference_rejected(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Application.objects.create(
                    applicant=self.citizen,
                    service=self.service,
                    reference_number="REQ-TEST-00001"
                )

    def test_05_application_protects_service(self):
        with self.assertRaises(ProtectedError):
            self.service.delete()

        self.assertTrue(
            Application.objects.filter(
                pk=self.application.pk
            ).exists()
        )

    def test_06_wrong_service_document_rejected(self):
        document = UploadedDocument(
            application=self.application,
            required_document=self.other_requirement,
            file="test-only/wrong.pdf",
            original_name="wrong.pdf"
        )

        with self.assertRaises(ValidationError):
            document.full_clean()

    def test_07_duplicate_document_version_rejected(self):
        self.make_upload(version=1)

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                self.make_upload(version=1, active=False)

    def test_08_two_active_versions_rejected(self):
        self.make_upload(version=1, active=True)

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                self.make_upload(version=2, active=True)

    def test_09_document_replacement(self):
        old_document = self.make_upload(version=1)

        old_document.status = UploadedDocument.Status.REPLACED
        old_document.is_active = False
        old_document.full_clean()
        old_document.save(
            update_fields=["status", "is_active"]
        )

        self.make_upload(version=2, active=True)

        documents = UploadedDocument.objects.filter(
            application=self.application,
            required_document=self.requirement
        )

        self.assertEqual(documents.count(), 2)
        self.assertEqual(
            documents.filter(is_active=True).count(),
            1
        )

    def test_10_invalid_verification_score(self):
        document = self.make_upload()

        verification = DocumentVerification(
            uploaded_document=document,
            provider="mock",
            status=DocumentVerification.Status.INVALID,
            score=Decimal("120.00")
        )

        with self.assertRaises(ValidationError):
            verification.full_clean()

    def test_11_verification_relationships(self):
        document = self.make_upload()

        verification = DocumentVerification.objects.create(
            uploaded_document=document,
            provider="mock",
            status=DocumentVerification.Status.INVALID,
            score=Decimal("35.00")
        )

        VerificationCheck.objects.create(
            verification=verification,
            check_type="required_fields",
            passed=False,
            message="Required field missing"
        )

        self.assertEqual(document.verifications.count(), 1)
        self.assertEqual(verification.checks.count(), 1)

    def test_12_operational_relationships(self):
        User = get_user_model()

        employee = User.objects.create_user(
            email="employee-test@example.com",
            password="TestOnlyPassword123!"
        )

        ApplicationEvent.objects.create(
            application=self.application,
            actor=self.citizen,
            event_type=ApplicationEvent.EventType.CREATED
        )

        EmployeeComment.objects.create(
            application=self.application,
            employee=employee,
            text="Test internal comment"
        )

        Notification.objects.create(
            application=self.application,
            recipient=self.citizen,
            title="Test notification",
            body="Your application was created"
        )

        GeneratedDocument.objects.create(
            application=self.application,
            file="test-only/generated.pdf",
            document_type="Test certificate"
        )

        self.assertEqual(self.application.events.count(), 1)
        self.assertEqual(self.application.comments.count(), 1)
        self.assertEqual(self.application.notifications.count(), 1)
        self.assertEqual(
            self.application.generated_documents.count(),
            1
        )


