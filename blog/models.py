from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32, default= 'title')
    content = models.TextField(null=True)
    #  官方文档：https://docs.djangoproject.com/en/1.10/ref/models/fields/
