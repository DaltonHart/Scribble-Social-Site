from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=140)

    def __str__(self):
        return self.author

class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=140)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author