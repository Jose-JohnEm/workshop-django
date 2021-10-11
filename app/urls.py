from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
        path('', views.index, name="index"),
        path('upload_post/', views.upload_post, name="upload_post"),
        path('download/<int:post_id>', views.download_post, name="download_post"),
        path('register', views.register, name='register'),
        path('like', views.like, name='like'),
]