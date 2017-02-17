from django.forms import ModelForm
from website.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
