from django.db import models

# Create your models here.

class Post(models.Model):
    id = 0 # Django id

    text = models.TextField()
    num = models.IntegerField()

    def __str__(self):
        post_name = "Post " + str(self.id)
        return post_name
