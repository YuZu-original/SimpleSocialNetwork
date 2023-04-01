from django.db import models

from core.models import User
from utils.model_mixins import UpdateAndCreateDateMixin


class Post(UpdateAndCreateDateMixin):
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    title = models.CharField(verbose_name="Заголовок", max_length=128)
    text = models.CharField(verbose_name="Текст", max_length=512)
    image = models.ImageField(verbose_name="Изображение", upload_to="images_of_posts")
    author = models.ForeignKey(to=User, verbose_name="Автор", related_name="posts", on_delete=models.CASCADE)


class Comment(UpdateAndCreateDateMixin):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    text = models.CharField(verbose_name="Текст", max_length=512)
    author = models.ForeignKey(to=User, verbose_name="Автор", related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, verbose_name="Пост", related_name="comments", on_delete=models.CASCADE)
