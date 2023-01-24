from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Группа"
    )
    slug = models.SlugField(unique=True)
    description = models.TextField(
        max_length=400,
        verbose_name="Описание"
    )

    def _str_(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name="Содержание")
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата"
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def _str_(self):
        return self.text
