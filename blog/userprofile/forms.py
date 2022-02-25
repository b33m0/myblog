from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')
    # From django official website. https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 == password2:
            return password2
        else:
            raise forms.ValidationError('Please enter the same password again.')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_img', 'profile_info')