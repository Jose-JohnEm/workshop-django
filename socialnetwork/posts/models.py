from django.db import models

# Create your models here.
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