# Generated by Django 3.0.8 on 2020-07-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='text',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
