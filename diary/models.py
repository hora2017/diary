from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __ref__(self):
        return self.created_date
