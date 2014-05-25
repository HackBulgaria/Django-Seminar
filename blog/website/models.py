from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(blank=False, max_length=100)
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(default='0')


class Comment(models.Model):
    text = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article)