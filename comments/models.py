from django.db import models
from django.contrib.auth.models import User
from blogs.models import BlogPost


# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Date Published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
