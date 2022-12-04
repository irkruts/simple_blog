from django.db import models

from django.db import models


class Article(models.Model):
    author = models.ForeignKey('auth.User', max_length=20, on_delete=models.CASCADE, verbose_name="Author")
    title = models.CharField(max_length=100, verbose_name="Title")
    body = models.TextField(verbose_name="Context")

    def __str__(self):
        return self.title
