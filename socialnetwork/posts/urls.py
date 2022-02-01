from django.urls import path
from. import views

urlpatterns = [
    path('', views.FeedView.as_view(), name="/"),
    path('upload_post/', views.create_post, name="upload_post"),
    path('posts/<int:pk>/', views.create_comment, name="create-comment-view")
]