# Generated by Django 4.1.7 on 2023-03-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_about_profile_birthday_profile_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tiktok',
            field=models.URLField(max_length=50, null=True),
        ),
    ]
