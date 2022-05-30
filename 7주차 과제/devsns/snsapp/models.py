from django.db import models
from django.conf import settings

#모델 파일 생성 후 makemigrations
#migration 파일 생성 후 migrate
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#1.models.py에 모델을 만든다.
#2.forms.py에 form을 만든다.
class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
# Create your models here.
