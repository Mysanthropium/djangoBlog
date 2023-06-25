from .models import Comment, UserProfile
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class ProfilePageForm(forms.ModelForm):
    # User profile page form
    class Meta:
        model = UserProfile
        fields = ('profile_image', 'bio')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    # Comment form in blog posts
    class Meta:
        model = Comment
        fields = ('body',)


class EditProfileForm(UserChangeForm):
    # Edit settings form for email, first name, last name and password
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class PasswordChangedForm(PasswordChangeForm):
    # Change password form
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'type': 'password'
    }))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'type': 'password'
        }))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'type': 'password'
        }))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
