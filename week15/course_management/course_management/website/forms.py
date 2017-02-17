from django import forms
from website.models import User


class PromoteUser(forms.Form):
    email = forms.CharField(max_length=128, label='Email:')
    course = forms.CharField(max_length=128, label='Course:')
    promote_to = forms.CharField(max_length=128, label='Promote to:')


class LoginForm(forms.Form):
    email = forms.CharField(max_length=128, label='Email:')
    password = forms.CharField(max_length=128, label='Password:',
                               widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=128, label='First Name:')
    last_name = forms.CharField(max_length=128, label='Last Name:')
    email = forms.CharField(max_length=128, label='Email:')
    password = forms.CharField(max_length=128, label='Password:',
                               widget=forms.PasswordInput)

    def save(self, commit=True):
        user = User.objects.create(first_name=self.cleaned_data['first_name'],
                                   last_name=self.cleaned_data['last_name'],
                                   email=self.cleaned_data['email'],
                                   password=self.cleaned_data['password'])
        user.save()
        return user
