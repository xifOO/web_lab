# Generated by Django 5.1.7 on 2025-04-22 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='Бренд')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='watch_images/', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата добавления')),
            ],
        ),
    ]
