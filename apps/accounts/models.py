from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Фото профиля', upload_to='user-profile/')
    bio = models.TextField('Биография', blank=True, null=True)
    inst = models.URLField('Инстаграм', max_length=300, blank=True, null=True)

    def __str__(self):
        return self.user

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
