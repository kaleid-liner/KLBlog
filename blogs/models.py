from django.db import models
from django.contrib.auth.models import User


def get_user_path(instance, filename):
    return f'{ instance.author.id }/{ filename }'


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=1024, default='')
    pub_date = models.DateTimeField('Date Published')
    text = models.TextField()
    pic = models.ImageField(upload_to=get_user_path, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


