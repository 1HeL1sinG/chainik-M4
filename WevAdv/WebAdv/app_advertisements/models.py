from typing import Any
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()

class Advertisement(models.Model):


    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="есть ли торг")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    image = models.ImageField(("изображение"), upload_to='advertisements/')


    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        else:
            return self.created_at.strftime('%d:%m:%Y в %H:%M:%S')
    
    @admin.display(description='Мини-фото')
    def mini_image(self):
        
        if self.image != '':
            return format_html('<img src="{}"', self.image.url)
        else:
            return format_html('<span style="color: red; font-weight: bold;">Фото отсутсвует</span>')

    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: yellow; font-weight: bold;">Сегодня в {}</span>', created_time)
        else:
            return self.updated_at.strftime('%d:%m:%Y в %H:%M:%S')


    class Meta:
        db_table = "Advertisements"

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
    
