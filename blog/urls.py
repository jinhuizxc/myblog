from django.conf.urls import url
from .import views
# 这个地方的index去掉后表示是空串，在网页中任意添加字符都能正常运行
# 如http://127.0.0.1:8000/blog/dsdafdsfs/，这显然不合理，
# 修改的话可以在r‘’里面添加^$输入别的字符串不能浏览页面只有空串才能正常浏览！
urlpatterns = [
    # url(r'^index/', views.index),
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
]
