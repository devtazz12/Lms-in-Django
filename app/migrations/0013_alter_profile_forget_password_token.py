# Generated by Django 4.2.6 on 2023-10-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='forget_password_token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]