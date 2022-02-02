from django.db import models

# Create your models here.
from socialnetwork import settings


class Post(models.Model):
    content = models.TextField(max_length=512)

    def _comments(self):
        comments = Comments.objects.filter(pk=self.pk)
        if len(comments) > 3:
            return comments[:3]
        else:
            return comments


class Comments(models.Model):
    parent_post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    comment_content = models.TextField(max_length=512)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )