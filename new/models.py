from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    userName = models.CharField(max_length=150,null=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=250)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.userName} - {self.date}'