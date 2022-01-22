from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=200)
    img = models.ImageField('Фото поста', upload_to='post-image/')
    description = models.TextField('Описание')
    likes = models.ManyToManyField(User, related_name="likes")
    archived = models.BooleanField('Архив', default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.user} : {self.title}"

    class Meta:
        ordering = ['-created']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commented_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    comment = models.CharField('Комментарии', max_length=250)
