# Generated by Django 4.2.2 on 2023-11-21 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_contactmessage_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]