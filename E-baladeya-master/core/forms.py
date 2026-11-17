from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from django.core.exceptions import ValidationError

from .models import User

from django.contrib.auth.forms import AuthenticationForm

class CitizenRegistrationForm(BaseUserCreationForm):

    first_name = forms.CharField(
        label="First name",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "autocomplete": "given-name",
        }),
    )

    last_name = forms.CharField(
        label="Last name",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "autocomplete": "family-name",
        }),
    )

    email = forms.EmailField(
        label="Email address",
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "autocomplete": "email",
            "placeholder": "you@example.com",
        }),
    )

    phone = forms.CharField(
        label="Phone number",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "autocomplete": "tel",
        }),
    )

    cin = forms.CharField(
        label="CIN",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
    )

    class Meta(BaseUserCreationForm.Meta):
        model = User

        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "cin",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in ("password1", "password2"):
            self.fields[field_name].widget.attrs.update({
                "class": "form-control",
                "autocomplete": "new-password",
            })

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError(
                "An account with this email address already exists."
            )

        return email



class EmailLoginForm(AuthenticationForm):

    username = forms.EmailField(
        label="Email address",
        max_length=254,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "you@example.com",
            "autocomplete": "email",
        }),
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Your password",
            "autocomplete": "current-password",
        }),
    )

    def clean_username(self):
        return self.cleaned_data["username"].strip().lower()
