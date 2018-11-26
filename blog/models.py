from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    weight = models.TextField(max_length=10)
    gender = models.TextField(max_length=10)
    talants = models.TextField(max_length=50)
    type = models.TextField(max_length=20)
    photo = models.CharField(max_length=255, default='#')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.

