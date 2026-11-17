
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Profile


def employee_required(view_func):
    """
    Allow employees and administrators.
    Reject citizens and users without an authorized role.
    """

    @login_required(login_url="login")
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        user = request.user

        if user.is_superuser:
            return view_func(request, *args, **kwargs)

        profile = getattr(user, "profile", None)

        allowed_roles = (
            Profile.Role.EMPLOYEE,
            Profile.Role.ADMINISTRATOR,
        )

        if profile is None or profile.role not in allowed_roles:
            raise PermissionDenied(
                "You do not have permission to access this page."
            )

        return view_func(request, *args, **kwargs)

    return wrapper


def administrator_required(view_func):
    """
    Allow platform administrators only.
    """

    @login_required(login_url="login")
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        user = request.user

        if user.is_superuser:
            return view_func(request, *args, **kwargs)

        profile = getattr(user, "profile", None)

        if (
            profile is None
            or profile.role != Profile.Role.ADMINISTRATOR
        ):
            raise PermissionDenied(
                "Administrator access is required."
            )

        return view_func(request, *args, **kwargs)

    return wrapper
