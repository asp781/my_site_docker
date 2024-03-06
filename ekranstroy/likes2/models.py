from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.db import models
from price.models import Service
from django.utils import timezone

User = get_user_model()


class ServiceLikes(models.Model):
    blog_post = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пост',
        # related_name='service_likes'
    )
    liked_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пользователь'
    )
    like = models.BooleanField('Like', default=False)
    created = models.DateTimeField('дата публикации', default=timezone.now)

    def __str__(self):
        return f'{self.liked_by}: {self.blog_post} {self.like}'

    class Meta:
        verbose_name = 'Blog Like'
        verbose_name_plural = 'Blog Likes'
