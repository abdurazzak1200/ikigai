from django.db import models
from custom.models import Custom
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Фото профиля', upload_to='user-profile/')
    bg = models.ImageField('Задний фон', upload_to='user-bg/')
    bio = models.TextField('Биография', blank=True, null=True)
    inst = models.URLField('Инстаграм', max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s profile"
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, image='user-profile/default.png', bg='user-bg/user-bg.jpeg')
        Custom.objects.create(user=instance, name='кастом', custom_bg='')

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
