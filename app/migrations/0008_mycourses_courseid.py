# Generated by Django 4.2.6 on 2023-10-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_mycourses_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycourses',
            name='courseid',
            field=models.IntegerField(null=True),
        ),
    ]
