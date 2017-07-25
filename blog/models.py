from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32, default= 'title')
    content = models.TextField(null=True)
    #  官方文档：https://docs.djangoproject.com/en/1.10/ref/models/fields/
# 修改数据默认显示名称
# __str__(self)(python 3.0)/__unicode__(self)(python 2.7)
# 方法里返回return self.title
    def __str__(self):
       return self.title