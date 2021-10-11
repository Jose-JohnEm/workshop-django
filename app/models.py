from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    class Format(models.IntegerChoices):
        AUDIO = 1
        VIDEO = 2
        IMAGE = 3
        BOOK = 4

    title = models.CharField(max_length=100)
    format = models.IntegerField(choices=Format.choices)
    description = models.CharField(max_length=100)
    content = models.FileField()
    last_modified_at = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(to=User, related_name="likes", default=None)
    views = models.ManyToManyField(to=User, related_name="views", default=None)
    saves = models.ManyToManyField(to=User, related_name="saves", default=None)
    post_owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="post_owner")


class Comment(models.Model):
    comment_owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comment_owner")
    related_post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="related_post")
    content = models.TextField()
    # parent_comment = models.ForeignKey(to=)
    last_updated = models.DateField(auto_now_add=True)

    def from_post(self, post_id: int):
        self.objects.all()