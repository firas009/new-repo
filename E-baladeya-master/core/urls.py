
from django.urls import path
from django.contrib.auth.decorators import login_required

from .permissions import employee_required

from .views import (
    application_complete,
    application_create,
    application_review,
    default_service_detail,
    document_upload,
    page,
    service_detail,
    services_catalogue,
    verification_result,
    register,
    login_view,
    logout_view,
    citizen_application_detail,
)


urlpatterns = [

    # ==========================================================
    # 1. PUBLIC ROUTES
    # ==========================================================

    path(
        "",
        page("home.html"),
        name="home",
    ),

    path(
        "services/",
        services_catalogue,
        name="services",
    ),

    path(
        "services/detail/",
        default_service_detail,
        name="service_detail",
    ),

    path(
        "services/<slug:service_slug>/",
        service_detail,
        name="service_detail_slug",
    ),


    # ==========================================================
    # 2. AUTHENTICATION ROUTES
    # ==========================================================

    path(
        "register/",
        register,
        name="register",
    ),

    path(
        "login/",
        login_view,
        name="login",
    ),

    path(
        "logout/",
        logout_view,
        name="logout",
    ),


    # ==========================================================
    # 3. AUTHENTICATED DASHBOARD
    # ==========================================================

    path(
        "dashboard/",
        login_required(
            page("dashboard.html"),
            login_url="login",
        ),
        name="dashboard",
    ),


    # ==========================================================
    # 4. PROTECTED APPLICATION ROUTES
    # ==========================================================

    path(
        "requests/new/",
        login_required(
            application_create,
            login_url="login",
        ),
        name="application_create_generic",
    ),

    path(
        "applications/new/<slug:service_slug>/",
        login_required(
            application_create,
            login_url="login",
        ),
        name="application_create",
    ),

    path(
        "requests/documents/",
        login_required(
            document_upload,
            login_url="login",
        ),
        name="document_upload",
    ),

    path(
        "applications/<slug:service_slug>/documents/",
        login_required(
            document_upload,
            login_url="login",
        ),
        name="document_upload_service",
    ),

    path(
        "requests/verification/",
        login_required(
            verification_result,
            login_url="login",
        ),
        name="verification_result",
    ),

    path(
        "applications/<slug:service_slug>/verification/",
        login_required(
            verification_result,
            login_url="login",
        ),
        name="verification_result_service",
    ),

    path(
        "requests/review/",
        login_required(
            application_review,
            login_url="login",
        ),
        name="application_review",
    ),

    path(
        "applications/<slug:service_slug>/review/",
        login_required(
            application_review,
            login_url="login",
        ),
        name="application_review_service",
    ),

    path(
        "requests/complete/",
        login_required(
            application_complete,
            login_url="login",
        ),
        name="application_complete",
    ),

    path(
        "applications/<slug:service_slug>/complete/",
        login_required(
            application_complete,
            login_url="login",
        ),
        name="application_complete_service",
    ),

    path(
        "requests/detail/",
        login_required(
            page("application_detail.html"),
            login_url="login",
        ),
        name="application_detail",
    ),


    # ==========================================================
    # 5. EMPLOYEE / ADMINISTRATION ROUTES
    # ==========================================================

    path(
        "administration/",
        employee_required(
            page("employee_dashboard.html")
        ),
        name="employee_dashboard",
    ),

    path(
        "administration/requests/detail/",
        employee_required(
            page("employee_application_detail.html")
        ),
        name="employee_application_detail",
    ),

    path(
        "administration/analytics/",
        employee_required(
            page("analytics.html")
        ),
        name="analytics",
    ),

    path(
    "applications/<int:application_id>/",
    citizen_application_detail,
    name="citizen_application_detail",
),
]
