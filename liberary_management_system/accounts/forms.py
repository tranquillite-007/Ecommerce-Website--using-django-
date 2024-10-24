from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 150)
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[
        ('user', 'User'),
        ('admin', 'Admin')
    ])