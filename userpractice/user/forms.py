from django.contrib.auth import forms
from .models import CustomUser

class CustomUserCreationForm(forms.UserCreationForm):
    class Meta:
        model = CustomUser
        fields = forms.UserCreationForm.Meta.fields + ('age', 'address',)


class CustomUserChangeForm(forms.UserChangeForm):
    class Meta:
        model = CustomUser
        fields =forms.UserChangeForm.Meta.fields