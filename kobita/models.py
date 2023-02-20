from django.db import models
import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    operator = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    view = models.IntegerField(default=0)
    detail = models.TextField(max_length=100000)
    created_at = models.DateTimeField(datetime.datetime.now())

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    post_comment = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(datetime.datetime.now())

    def __str__(self):
        return self.name
    
class subscription(models.Model):
    email = models.EmailField(max_length=100)
    ip = models.CharField(max_length=100)
    def __str__(self):
        return self.email
    