from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Comment(models.Model):
    username = models.CharField('Имя', max_length=140)
    text = models.TextField('Текст')
    