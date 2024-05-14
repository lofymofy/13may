from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import User, Order
from django.core.validators import RegexValidator


class RegistrationForm(UserCreationForm):
    validator_phone = RegexValidator(regex=r'^\+7\d{10}$', message='Формат: +7-xxx-xxx-xx-xx')
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}),
                                max_length=100, label="ФИО")
    phone_number = forms.CharField(validators=[validator_phone], widget=forms.TextInput(attrs={'class': 'form-input'}),
                                   max_length=13, label="Телефон")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}),
                             label="Email")
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}),
                               max_length=150, label="Username")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}),
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}),
                                label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'full_name', 'phone_number', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Выберете другое имя")
        return username


class AuthForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter a username'}),
                               max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите password'}),
                                label="Password")

    class Meta:
        model = User
        fields = ['username', 'password']


class OrderForm(forms.ModelForm):

    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Введите количество'}))
    problem = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Опишите проблему'}))

    class Meta:
        model = Order
        fields = ['amount', 'problem']