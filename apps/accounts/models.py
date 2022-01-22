from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Фото профиля', upload_to='user-profile/')
    bio = models.TextField('Биография', blank=True, null=True)
    inst = models.URLField('Инстаграм', max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s profile"

