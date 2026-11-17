from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)
from pathlib import Path
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("An email address is required")

        email = self.normalize_email(email).strip().lower()

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)







class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):

    class Role(models.TextChoices):
        CITIZEN = "citizen", "Citizen"
        EMPLOYEE = "employee", "Employee"
        ADMINISTRATOR = "administrator", "Administrator"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    cin = models.CharField(
        max_length=30,
        blank=True
    )

    address = models.TextField(blank=True)

    municipality = models.CharField(
        max_length=120,
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CITIZEN
    )

    def __str__(self):
        return f"{self.user.email} - {self.get_role_display()}"




    
class MunicipalService(models.Model):

    class ProcessingType(models.TextChoices):
        AUTOMATIC = "automatic", "Instant service"
        MANUAL_REVIEW = "manual_review", "Administrative review"

    name = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True
    )

    category = models.CharField(max_length=100)

    category_slug = models.SlugField(max_length=120)

    description = models.TextField()

    eligibility = models.TextField(blank=True)

    fee = models.CharField(
        max_length=150,
        blank=True
    )

    issuing_authority = models.CharField(
        max_length=200,
        blank=True
    )

    processing_type = models.CharField(
        max_length=30,
        choices=ProcessingType.choices,
        default=ProcessingType.MANUAL_REVIEW
    )

    summary_details = models.JSONField(
        default=list,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    @property
    def required_documents_count(self):
        return self.required_documents.count()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name





class RequiredDocument(models.Model):

    service = models.ForeignKey(
        MunicipalService,
        on_delete=models.CASCADE,
        related_name="required_documents"
    )

    name = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    required = models.BooleanField(default=True)

    accepted_file_types = models.CharField(
        max_length=100,
        default="PDF, JPG, PNG"
    )

    max_size_bytes = models.PositiveIntegerField(
        default=5 * 1024 * 1024
    )

    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "id"]

        constraints = [
            models.UniqueConstraint(
                fields=["service", "name"],
                name="unique_document_name_per_service"
            )
        ]

    def __str__(self):
        return f"{self.service.name} - {self.name}"




class Application(models.Model):

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        DOCUMENTS_PENDING = "documents_pending", "Documents pending"
        VERIFICATION_PENDING = "verification_pending", "Verification pending"
        CORRECTION_REQUIRED = "correction_required", "Correction required"
        MANUAL_REVIEW = "manual_review", "Manual review"
        ADDITIONAL_DOCUMENTS_REQUIRED = (
            "additional_documents_required",
            "Additional documents required"
        )
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="submitted_applications"
    )

    service = models.ForeignKey(
        MunicipalService,
        on_delete=models.PROTECT,
        related_name="applications"
    )

    reference_number = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        blank=True,
        editable=False
    )

    status = models.CharField(
        max_length=40,
        choices=Status.choices,
        default=Status.DRAFT
    )

    assigned_employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_applications"
    )

    submitted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    decision_at = models.DateTimeField(
        null=True,
        blank=True
    )

    rejection_reason = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

        indexes = [
            models.Index(
                fields=["applicant", "status"],
                name="app_applicant_status_idx"
            ),
            models.Index(
                fields=["service", "status"],
                name="app_service_status_idx"
            ),
        ]

    def __str__(self):
        reference = self.reference_number or f"Draft #{self.pk}"
        return f"{reference} - {self.service.name}"




class ApplicationField(models.Model):

    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="fields"
    )

    field_name = models.SlugField(
        max_length=100
    )

    value = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["field_name"]

        constraints = [
            models.UniqueConstraint(
                fields=["application", "field_name"],
                name="unique_application_field"
            )
        ]

    def __str__(self):
        return f"Application {self.application_id} - {self.field_name}"


def private_document_path(instance, filename):
    extension = Path(filename).suffix.lower()
    unique_name = f"{uuid4().hex}{extension}"

    return (
        f"applications/"
        f"{instance.application_id}/"
        f"{unique_name}"
    )


class UploadedDocument(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CHECKING = "checking", "Checking"
        VALID = "valid", "Valid"
        INVALID = "invalid", "Invalid"
        REPLACED = "replaced", "Replaced"

    application = models.ForeignKey(
        Application,
        on_delete=models.PROTECT,
        related_name="uploaded_documents"
    )

    required_document = models.ForeignKey(
        RequiredDocument,
        on_delete=models.PROTECT,
        related_name="uploads"
    )

    file = models.FileField(
        upload_to=private_document_path,
        max_length=500
    )

    original_name = models.CharField(max_length=255)

    mime_type = models.CharField(
        max_length=127,
        blank=True
    )

    size_bytes = models.PositiveBigIntegerField(default=0)

    sha256 = models.CharField(
        max_length=64,
        blank=True
    )

    version = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )

    is_active = models.BooleanField(default=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    uploaded_at = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        ordering = ["-uploaded_at"]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "application",
                    "required_document",
                    "version"
                ],
                name="unique_uploaded_document_version"
            ),

            models.UniqueConstraint(
                fields=[
                    "application",
                    "required_document"
                ],
                condition=Q(is_active=True),
                name="unique_active_uploaded_document"
            ),
        ]

    def clean(self):
        super().clean()

        if self.application_id and self.required_document_id:
            if (
                self.application.service_id
                != self.required_document.service_id
            ):
                raise ValidationError({
                    "required_document":
                    "This document is not required by "
                    "the application's service."
                })

    def __str__(self):
        return (
            f"Application {self.application_id} - "
            f"{self.required_document.name} "
            f"(v{self.version})"
        )




class DocumentVerification(models.Model):

    class Status(models.TextChoices):
        VALID = "valid", "Valid"
        INVALID = "invalid", "Invalid"
        INCOMPLETE = "incomplete", "Incomplete"
        MANUAL_REVIEW = "manual_review", "Manual review"

    uploaded_document = models.ForeignKey(
        UploadedDocument,
        on_delete=models.PROTECT,
        related_name="verifications"
    )

    provider = models.CharField(
        max_length=100,
        default="mock"
    )

    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices
    )

    raw_result_reference = models.CharField(
        max_length=255,
        blank=True
    )

    checked_at = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        ordering = ["-checked_at"]

    def __str__(self):
        return (
            f"Verification {self.pk} - "
            f"{self.status}"
        )




class VerificationCheck(models.Model):

    verification = models.ForeignKey(
        DocumentVerification,
        on_delete=models.CASCADE,
        related_name="checks"
    )

    check_type = models.CharField(
        max_length=100
    )

    passed = models.BooleanField(
        null=True,
        blank=True
    )

    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    message = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return (
            f"{self.check_type} - "
            f"Verification {self.verification_id}"
        )



class ApplicationEvent(models.Model):

    class EventType(models.TextChoices):
        CREATED = "created", "Application created"
        SUBMITTED = "submitted", "Application submitted"
        DOCUMENT_UPLOADED = "document_uploaded", "Document uploaded"
        DOCUMENT_REPLACED = "document_replaced", "Document replaced"
        VERIFICATION_COMPLETED = (
            "verification_completed",
            "Verification completed"
        )
        STATUS_CHANGED = "status_changed", "Status changed"
        CORRECTION_REQUESTED = (
            "correction_requested",
            "Correction requested"
        )
        ADDITIONAL_DOCUMENTS = (
            "additional_documents",
            "Additional documents requested"
        )
        ASSIGNED = "assigned", "Employee assigned"
        COMMENT_ADDED = "comment_added", "Comment added"
        APPROVED = "approved", "Application approved"
        REJECTED = "rejected", "Application rejected"
        COMPLETED = "completed", "Application completed"
        CANCELLED = "cancelled", "Application cancelled"

    application = models.ForeignKey(
        Application,
        on_delete=models.PROTECT,
        related_name="events"
    )

    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="application_events"
    )

    event_type = models.CharField(
        max_length=40,
        choices=EventType.choices
    )

    old_status = models.CharField(
        max_length=40,
        choices=Application.Status.choices,
        blank=True
    )

    new_status = models.CharField(
        max_length=40,
        choices=Application.Status.choices,
        blank=True
    )

    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at", "id"]

        indexes = [
            models.Index(
                fields=["application", "created_at"],
                name="app_event_time_idx"
            )
        ]

    def __str__(self):
        return (
            f"Application {self.application_id} - "
            f"{self.event_type}"
        )



class EmployeeComment(models.Model):

    class Visibility(models.TextChoices):
        PUBLIC = "public", "Visible to citizen"
        INTERNAL = "internal", "Internal only"

    application = models.ForeignKey(
        Application,
        on_delete=models.PROTECT,
        related_name="comments"
    )

    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="employee_comments"
    )

    text = models.TextField()

    visibility = models.CharField(
        max_length=20,
        choices=Visibility.choices,
        default=Visibility.INTERNAL
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return (
            f"Comment by {self.employee.email} "
            f"on application {self.application_id}"
        )



class Notification(models.Model):

    class NotificationType(models.TextChoices):
        GENERAL = "general", "General"
        REQUEST_SUBMITTED = "request_submitted", "Request submitted"
        STATUS_UPDATE = "status_update", "Status update"
        CORRECTION_REQUIRED = (
            "correction_required",
            "Correction required"
        )
        ADDITIONAL_DOCUMENTS = (
            "additional_documents",
            "Additional documents required"
        )
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"
        COMPLETED = "completed", "Completed"

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="notifications"
    )

    application = models.ForeignKey(
        Application,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notifications"
    )

    notification_type = models.CharField(
        max_length=40,
        choices=NotificationType.choices,
        default=NotificationType.GENERAL
    )

    title = models.CharField(max_length=200)

    body = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    read_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["-created_at"]

        indexes = [
            models.Index(
                fields=["recipient", "is_read"],
                name="noti_recipient_read_idx"
            )
        ]

    def __str__(self):
        return f"{self.recipient.email} - {self.title}"



def private_generated_document_path(instance, filename):
    extension = Path(filename).suffix.lower()

    unique_name = f"{uuid4().hex}{extension}"

    return (
        f"generated/applications/"
        f"{instance.application_id}/"
        f"{unique_name}"
    )




class GeneratedDocument(models.Model):

    class DeliveryStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        AVAILABLE = "available", "Available"
        DELIVERED = "delivered", "Delivered"
        FAILED = "failed", "Failed"

    application = models.ForeignKey(
        Application,
        on_delete=models.PROTECT,
        related_name="generated_documents"
    )

    file = models.FileField(
        upload_to=private_generated_document_path,
        max_length=500
    )

    document_type = models.CharField(max_length=100)

    delivery_status = models.CharField(
        max_length=20,
        choices=DeliveryStatus.choices,
        default=DeliveryStatus.PENDING
    )

    generated_at = models.DateTimeField(auto_now_add=True)

    delivered_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["-generated_at"]

    def __str__(self):
        return (
            f"{self.document_type} - "
            f"Application {self.application_id}"
        )