from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1', views.post, name = 'post'),
]