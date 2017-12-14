from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)

    def publish(self):
        self.save()

    def __str__(self):
        #strTime = str(self.created_date)
        #return strTime
        return self.created_date.strftime("%Y / %m / %d / %I:%M %p")

# class Comment(models.Model):
#     post = models.ForeignKey('diary.Post', related_name='comments')
#     author = models.ForeignKey('auth.User')
#     message = models.TextField()
#     created_date = models.DateTimeField(auto_now=True)

#     def publish(self):
#         self.save()

#     def __str__(self):
#         return self.message
