from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'excerpt', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }