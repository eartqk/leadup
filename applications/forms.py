from django.forms import ModelForm
from .models import Application


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        labels = {
            "name": "Имя",
            "phone_number": "Номер телефона",
            "text": "Ваши предпочтения/пожелания",
        }
        error_messages = {
            'name': {
                'blank': "Введите Ваше имя.",
            },
            'phone_number': {
                'invalid': "Введите номер телефона в формате: +7 999 999 99 99.",
                'unique': "Номер телефона уже занят.",
                'blank': "Введите номер Вашего телефона."
            },
            'email': {
                'blank': "Введите Ваш почтовый адрес.",
                'unique': "Почтовый адрес уже занят.",
                'invalid': "Введите корректный почтовый адрес.",
            },
            'text': {
                'blank': "Введите Ваши вопросы или предпочтения.",
            },
        }
