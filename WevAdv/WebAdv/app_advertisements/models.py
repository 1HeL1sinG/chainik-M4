from typing import Any
from django.db import models

class Advertisement(models.Model):


    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="есть ли торг")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = "Advertisements"

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
    
