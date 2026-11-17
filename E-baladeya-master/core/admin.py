from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User,
    Profile,
    MunicipalService,
    RequiredDocument,
    Application,
    ApplicationField,
    UploadedDocument,
    DocumentVerification,
    VerificationCheck,
    ApplicationEvent,
    EmployeeComment,
    Notification,
    GeneratedDocument,
)


admin.site.site_header = "E-Baladiya Administration"
admin.site.site_title = "E-Baladiya Admin"
admin.site.index_title = "Municipal Platform Management"


class SuperuserOnlyMixin:

    def _allowed(self, request):
        return (
            request.user.is_active
            and request.user.is_superuser
        )

    def has_module_permission(self, request):
        return self._allowed(request)

    def has_view_permission(self, request, obj=None):
        return self._allowed(request)

    def has_add_permission(self, request):
        return self._allowed(request)

    def has_change_permission(self, request, obj=None):
        return self._allowed(request)

    def has_delete_permission(self, request, obj=None):
        return self._allowed(request)


@admin.register(User)
class EBaladiyaUserAdmin(SuperuserOnlyMixin, UserAdmin):

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
    )

    search_fields = (
        "email",
        "first_name",
        "last_name",
    )

    ordering = ("email",)

    readonly_fields = (
        "last_login",
        "date_joined",
    )

    fieldsets = (
        (None, {
            "fields": ("email", "password")
        }),
        ("Personal information", {
            "fields": ("first_name", "last_name")
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important dates", {
            "fields": ("last_login", "date_joined")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
            ),
        }),
    )

    filter_horizontal = (
        "groups",
        "user_permissions",
    )


@admin.register(Profile)
class ProfileAdmin(SuperuserOnlyMixin, admin.ModelAdmin):

    list_display = (
        "user",
        "role",
        "municipality",
    )

    list_filter = ("role", "municipality")

    search_fields = (
        "user__email",
        "municipality",
    )


@admin.register(MunicipalService)
class MunicipalServiceAdmin(
    SuperuserOnlyMixin,
    admin.ModelAdmin
):

    list_display = (
        "name",
        "category",
        "processing_type",
        "is_active",
    )

    list_filter = (
        "category",
        "processing_type",
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
        "description",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(RequiredDocument)
class RequiredDocumentAdmin(
    SuperuserOnlyMixin,
    admin.ModelAdmin
):

    list_display = (
        "name",
        "service",
        "required",
        "position",
    )

    list_filter = ("required", "service")

    search_fields = (
        "name",
        "service__name",
    )


class ReadOnlyAdmin(SuperuserOnlyMixin, admin.ModelAdmin):

    actions = None

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Application)
class ApplicationAdmin(ReadOnlyAdmin):

    list_display = (
        "reference_number",
        "applicant",
        "service",
        "status",
        "created_at",
    )

    list_filter = ("status", "service")

    search_fields = (
        "reference_number",
        "applicant__email",
    )


@admin.register(ApplicationField)
class ApplicationFieldAdmin(ReadOnlyAdmin):

    list_display = (
        "application",
        "field_name",
    )

    search_fields = (
        "field_name",
        "application__reference_number",
    )


@admin.register(UploadedDocument)
class UploadedDocumentAdmin(ReadOnlyAdmin):

    list_display = (
        "application",
        "required_document",
        "version",
        "status",
        "is_active",
    )

    list_filter = (
        "status",
        "is_active",
    )


@admin.register(DocumentVerification)
class DocumentVerificationAdmin(ReadOnlyAdmin):

    list_display = (
        "uploaded_document",
        "provider",
        "status",
        "score",
        "checked_at",
    )

    list_filter = (
        "status",
        "provider",
    )


@admin.register(VerificationCheck)
class VerificationCheckAdmin(ReadOnlyAdmin):

    list_display = (
        "verification",
        "check_type",
        "passed",
        "score",
    )

    list_filter = (
        "check_type",
        "passed",
    )


@admin.register(ApplicationEvent)
class ApplicationEventAdmin(ReadOnlyAdmin):

    list_display = (
        "application",
        "actor",
        "event_type",
        "created_at",
    )

    list_filter = ("event_type",)


@admin.register(EmployeeComment)
class EmployeeCommentAdmin(ReadOnlyAdmin):

    list_display = (
        "application",
        "employee",
        "visibility",
        "created_at",
    )

    list_filter = ("visibility",)


@admin.register(Notification)
class NotificationAdmin(ReadOnlyAdmin):

    list_display = (
        "recipient",
        "notification_type",
        "is_read",
        "created_at",
    )

    list_filter = (
        "notification_type",
        "is_read",
    )


@admin.register(GeneratedDocument)
class GeneratedDocumentAdmin(ReadOnlyAdmin):

    list_display = (
        "application",
        "document_type",
        "delivery_status",
        "generated_at",
    )

    list_filter = ("delivery_status",)