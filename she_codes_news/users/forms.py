from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class CustomUserCreationForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 200px;'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 200px;'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'style': 'width: 400px;'}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username','password1', 'password2',]


class EditUserProfileForm(forms.ModelForm):
    avatar = forms.URLField(help_text='Copy Image Address URL', required=True)
    location = forms.CharField(max_length=30, required=False)
    bio = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        required=False,
        help_text='Tell us about yourself?'
    )

    class Meta:
        model = CustomUser
        fields = ['avatar', 'location', 'bio']


