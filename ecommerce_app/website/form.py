from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    """ Đây là form đăng nhập của tài khoản người dùng """
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
    
    def clean(self):
        """ Xác thực người dùng """
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")
        return cleaned_data
