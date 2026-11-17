
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Application, UploadedDocument


def get_citizen_application_or_404(user, application_id):
    """
    Return an application only if it belongs to this user.

    Otherwise, return HTTP 404.
    """

    if not user.is_authenticated:
        raise Http404("Application not found.")

    return get_object_or_404(
        Application.objects.select_related("service"),
        pk=application_id,
        applicant_id=user.pk,
    )


def get_citizen_document_or_404(user, document_id):
    """
    Return an uploaded document only if its application
    belongs to this user.

    Otherwise, return HTTP 404.
    """

    if not user.is_authenticated:
        raise Http404("Document not found.")

    return get_object_or_404(
        UploadedDocument.objects.select_related(
            "application",
            "required_document",
        ),
        pk=document_id,
        application__applicant_id=user.pk,
    )
