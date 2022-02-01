from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import PostCreationForm, CommentCreationForm
from .models import Post, Comments


# Create your views here.

class FeedView(ListView):
    model = Post
    template_name = "post/feed.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all()


def create_post(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, "Invalid form, please try again")
    elif request.method == "GET":
        return render(request, "post/upload_post.html", {"post_form": PostCreationForm})


def create_comment(request, pk):
    if request.method == "POST":
        form = CommentCreationForm(request.POST)
        if form.is_valid():
            Comments(comment_content=form.cleaned_data["comment_content"],
                     parent_post=Post.objects.get(pk=pk)).save()
            return redirect('/')
        else:
            messages.error(request, "An error has occurred. Please submit your comment again.")
    elif request.method == "GET":
        return render(request, "post/post_detail.html", {"post": Post.objects.get(pk=pk),
                                                         "comments": Comments.objects.filter(parent_post_id=pk),
                                                         "comment_form": CommentCreationForm})
