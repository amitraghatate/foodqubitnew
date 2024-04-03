# Generated by Django 4.0.1 on 2024-01-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('api_key', models.CharField(default='43295164-59d2-4152-b6e0-1556c282ba72', max_length=40, unique=True)),
            ],
        ),
    ]
