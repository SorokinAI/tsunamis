from .models import Swimmer, Mark
from django.forms import ModelForm, TextInput


class LoginForm(ModelForm):
    class Meta:
        model = Swimmer
        fields = ['name', 'surname', 'password']

        widgets = {
            'name': TextInput(attrs={
                'type': 'text',
                'placeholder': 'Имя',
                'class': 'register_input'
            }),
            'surname': TextInput(attrs={
                'type': 'text',
                'placeholder': 'Фамилия',
                'class': 'register_input'
            }),
            'password': TextInput(attrs={
                'type': 'password',
                'placeholder': 'Пароль',
                'class': 'register_input'
            }),
        }
