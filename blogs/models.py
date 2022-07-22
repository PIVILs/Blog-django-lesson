from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """Сообщение, которое создал пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращаемое строковое предсьавление модели."""
        return self.text

class Entry(models.Model):
    """Инвормацияб внутри блога"""
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text[:50] + "..."