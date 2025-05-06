from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Watch(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Бренд")
    model = models.CharField(max_length=100, verbose_name="Модель")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    published = models.DateTimeField(default=datetime.now, db_index=True, verbose_name="Дата публикации")
    image = models.ImageField(upload_to='watch_images/', verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="Дата добавления")
    author = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"
    
    def get_absolute_url(self):
        return reverse('home:post_detail', kwargs={'parameter': self.id})


class Comment(models.Model):
    watch = models.ForeignKey('Watch', on_delete=models.CASCADE, related_name='comments', verbose_name="Часы")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Комментарий")
    date = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")

    def __str__(self):
        return f'Комментарий от {self.author.username} к {self.watch}'