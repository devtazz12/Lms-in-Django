# Generated by Django 4.2.6 on 2023-10-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='images',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
