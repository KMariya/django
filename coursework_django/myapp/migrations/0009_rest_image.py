# Generated by Django 4.2.2 on 2023-06-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_rest_image_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='rest',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
