from typing import Any
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
class Advertisement(models.Model):


    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="есть ли торг")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        else:
            return self.created_at.strftime('%d:%m:%Y в %H:%M:%S')
        
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
    
