from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


# Create your models here.
class CatUser(models.Model):
    cat_user = models.CharField(max_length=15, verbose_name='Категория полльзователя')

    class Meta:
        verbose_name = 'Категория пользователей'
        verbose_name_plural = 'Категории пользователей'

    def __str__(self):
        return self.cat_user


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    cat_user = models.ForeignKey(CatUser, on_delete=models.PROTECT)
    photo = ResizedImageField(size=[300, 300], upload_to='avatars', default='def_avatar.jpg', verbose_name='Фото '
                                                                                                           'профиля')

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    place_work = models.CharField(max_length=20, verbose_name='Место работы')
    position = models.CharField(max_length=20, verbose_name='Должность')
    time_start = models.DateField(verbose_name='Работал с')
    time_end = models.DateField(verbose_name='Работал по')

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'
