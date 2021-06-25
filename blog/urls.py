from django.urls import path, include
from .views import BlogPostListView, BlogPostDetailView
from . import views

urlpatterns = [
    path('', BlogPostListView.as_view(), name='index'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name = 'blog-detail'),
    path('post/new/', views.createBlog , name = 'blog-create'),
]