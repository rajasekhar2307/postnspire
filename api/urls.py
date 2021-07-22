from django.urls import path, include
from .views import blogPostView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', blogPostView.as_view(), name='apiview'),
]
