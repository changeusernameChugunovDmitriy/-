from django import forms


class RegistrationForm(forms.Form):
    fio = forms.CharField(max_length=55)
    email = forms.EmailField()
    password = forms.CharField()

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()