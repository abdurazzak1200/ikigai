from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Custom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Название кастома', max_length=100)
    castom_bg = models.ImageField(upload_to='custom/',blank=True, null=True)

    def __str__(self):
        return f'{self.user} custom'
