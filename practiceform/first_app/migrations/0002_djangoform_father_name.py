# Generated by Django 5.0.2 on 2024-03-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangoform',
            name='father_name',
            field=models.TextField(default=None),
        ),
    ]
