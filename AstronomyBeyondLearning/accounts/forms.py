from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    website = forms.URLField(required=False)
    profile_picture = forms.ImageField(required=False)

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # check username exists
        if username and User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken.")

        # check email format
        if email:
            try:
                validate_email(email)
            except ValidationError:
                raise ValidationError("Invalid email format.")

        # check password match
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")

        # check password strength
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#^+-]).{8,}$'
        if password and not re.match(password_regex, password):
            raise ValidationError(
                "Password must contain uppercase, lowercase, a number, a special character and be at least 8 characters long."
            )

        return cleaned_data
    
class SignInForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

