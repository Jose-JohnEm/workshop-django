from django import template
from posts.models import Post, Comments
from django.contrib.auth.models import User

register = template.Library()


@register.filter(name='zip')
def zip_lists(a: iter, b: iter):
    return zip(a, b)


@register.filter(name='get_nb_comments')
def get_nb_comments(post: Post):
    return len(Comments.objects.filter(parent_post_id=post.id))


@register.filter(name='get_last_comments')
def get_last_comments(post: Post):
    comments = Comments.objects.filter(parent_post_id=post.id)
    if len(comments) > 3:
        comments = comments[:3]
    return comments