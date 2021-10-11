from django.shortcuts import render, redirect, get_object_or_404
from app.forms import NewUserForm, UploadPostForm
from django.contrib.auth import login, authenticate
from app.models import Post
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        print("Hello", request.user)
    else:
        print("not authenticated.")

    page_number = request.GET.get('page')

    posts = Paginator(Post.objects.all().order_by("id"), 12)
    return render(request, 'artists/index.html', {"posts": posts.get_page(page_number)})


@login_required
def like(request):
    if request.method == "POST":
        if request.POST.get("operation", "") == "like_submit" and request.is_ajax():
            post = get_object_or_404(Post, pk=request.POST.get("post_id", "").replace("post_", ""))
            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
                return JsonResponse({"liked": False, "post_id": post.id})
            post.likes.add(request.user)
            return JsonResponse({"liked": True, "post_id": post.id})


@login_required
def download_post(request):
    pass


@login_required
def upload_post(request):
    if request.method == 'POST':
        form = UploadPostForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(title=form.cleaned_data['title'],
                                format=form.cleaned_data['format'],
                                description=form.cleaned_data['description'],
                                content=form.cleaned_data['content'],
                                post_owner=request.user)
            return HttpResponseRedirect('/')
    return render(request, 'artists/upload_post.html', {"form": UploadPostForm()})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user = authenticate(request, user.username, user.password)
            if user:
                messages.success(request, 'Registration successful.')
                return redirect('app:upload_post')
        messages.error(request, 'Unsucessful registration!')
    return render(request, 'artists/register.html', {"form": NewUserForm(), })


def profile(request):
    if request.method == 'GET':
        return render(request, 'artists/profile.html', {})
