# Generated by Django 3.0.8 on 2020-07-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_application_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=64, null=True, unique=True),
        ),
    ]
