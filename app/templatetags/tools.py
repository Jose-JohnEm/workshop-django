from django import template
from app.models import Post, Comment
from django.contrib.auth.models import User

register = template.Library()


@register.filter(name='zip')
def zip_lists(a: iter, b: iter):
    return zip(a, b)


@register.filter(name='get_nb_likes')
def get_post_nb_likes(post: Post):
    return post.likes.count()


@register.filter(name='get_nb_comments')
def get_nb_comments(post: Post):
    return len(Comment.objects.filter(related_post__id=post.id))


@register.filter(name='active_like')
def active_like(post: Post, user: User):
    if post.likes.filter(id=user.id).exists():
        return "dislike"
    return "like"
