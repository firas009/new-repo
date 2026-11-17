from django.http import Http404
from django.shortcuts import redirect, render

from .services import SERVICES, SERVICES_BY_SLUG

from django.contrib import messages
from django.db import IntegrityError, transaction

from .forms import CitizenRegistrationForm
from .models import Profile, User

from django.contrib.auth import login as auth_login
from .forms import EmailLoginForm


from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

from .access import get_citizen_application_or_404

def page(template_name):
    def view(request):
        return render(request, template_name)

    return view


def services_catalogue(request):
    categories = []
    for service in SERVICES:
        category = next((item for item in categories if item['slug'] == service['category_slug']), None)
        if category is None:
            category = {'slug': service['category_slug'], 'name': service['category'], 'services': []}
            categories.append(category)
        category['services'].append(service)
    return render(request, 'services.html', {'services': SERVICES, 'categories': categories})


def service_detail(request, service_slug):
    service = SERVICES_BY_SLUG.get(service_slug)
    if service is None:
        raise Http404('Municipal service not found')
    return render(request, 'service_detail.html', {'service': service})


def default_service_detail(request):
    return service_detail(request, 'birth-certificate-extract')


def application_create(request, service_slug=None):
    if service_slug is not None:
        if service_slug not in SERVICES_BY_SLUG:
            raise Http404('Municipal service not found')
        return redirect('document_upload_service', service_slug=service_slug)
    return render(request, 'application_create.html', {'service': None, 'services': SERVICES})


def document_upload(request, service_slug=None):
    context = {'service': None}
    if service_slug is not None:
        service = SERVICES_BY_SLUG.get(service_slug)
        if service is None:
            raise Http404('Municipal service not found')
        context['service'] = service
    return render(request, 'document_upload.html', context)


def verification_result(request, service_slug=None):
    context = {'service': None}
    if service_slug is not None:
        service = SERVICES_BY_SLUG.get(service_slug)
        if service is None:
            raise Http404('Municipal service not found')
        context['service'] = service
    return render(request, 'verification_result.html', context)


def application_review(request, service_slug=None):
    context = {'service': None}
    if service_slug is not None:
        service = SERVICES_BY_SLUG.get(service_slug)
        if service is None:
            raise Http404('Municipal service not found')
        context['service'] = service
    return render(request, 'application_review.html', context)


def application_complete(request, service_slug=None):
    context = {'service': None}
    if service_slug is not None:
        service = SERVICES_BY_SLUG.get(service_slug)
        if service is None:
            raise Http404('Municipal service not found')
        context['service'] = service
    return render(request, 'application_complete.html', context)




def register(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = CitizenRegistrationForm(request.POST)

        if form.is_valid():

            try:
                with transaction.atomic():

                    user = form.save(commit=False)

                    user.is_staff = False
                    user.is_superuser = False

                    user.save()

                    Profile.objects.create(
                        user=user,
                        phone=form.cleaned_data.get("phone", ""),
                        cin=form.cleaned_data.get("cin", ""),
                        role=Profile.Role.CITIZEN,
                    )

            except IntegrityError:
                if User.objects.filter(
                    email__iexact=form.cleaned_data["email"]
                ).exists():
                    form.add_error(
                        "email",
                        "An account with this email already exists."
                    )
                else:
                    raise

            else:
                messages.success(
                    request,
                    "Your account has been created successfully. "
                    "You can now log in."
                )

                return redirect("login")

    else:
        form = CitizenRegistrationForm()

    return render(
        request,
        "register.html",
        {"form": form},
    )




def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = EmailLoginForm(
            request=request,
            data=request.POST,
        )

        if form.is_valid():

            user = form.get_user()

            auth_login(request, user)

            return redirect("dashboard")

    else:
        form = EmailLoginForm(request=request)

    return render(
        request,
        "login.html",
        {"form": form},
    )



@require_POST
def logout_view(request):

    auth_logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("login")



@login_required(login_url="login")
def citizen_application_detail(request, application_id):

    application = get_citizen_application_or_404(
        user=request.user,
        application_id=application_id,
    )

    return render(
        request,
        "application_detail.html",
        {
            "application": application,
        },
    )
