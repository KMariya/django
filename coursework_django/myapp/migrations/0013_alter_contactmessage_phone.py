# Generated by Django 4.2.2 on 2023-10-23 23:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_rename_contactform_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+79999999999", regex='^\\+7\\d{10}$')]),
        ),
    ]