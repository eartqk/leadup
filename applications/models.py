from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
# Create your models here.


class Application(models.Model):
    name = models.CharField(max_length=64, null=True)
    # phone_regex = RegexValidator(regex=r'^\+?7?\d{10}$')
    # validators=[phone_regex] (in phone_number)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=64, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.name + '  ' + self.email
