from django.contrib.auth.forms import UserCreationForm
from django import forms


# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields
#
from django.contrib.auth.models import User

from accounts.models import BlogUser


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UpdateBlogUser(forms.ModelForm):
    profilePicture = forms.ImageField(required=False, label='Profile picture:', widget=forms.FileInput)

    class Meta:
        model = BlogUser
        fields = ['profilePicture']
