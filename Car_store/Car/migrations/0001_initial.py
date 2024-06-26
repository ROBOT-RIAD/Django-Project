# Generated by Django 5.0.2 on 2024-03-19 17:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand_name', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('buye', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Car/media/uploads/')),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand_name.carmodel')),
                ('coustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
