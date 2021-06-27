from django.urls import include, path
from . import views
from users import views as user_views


urlpatterns = [
	path('login/', views.login, name='login'),
	path('signup/', views.signup, name='signup'),
	path('logout/', views.logout, name='logout'),
	path('<username>/',user_views.profile, name='profile'),
	path('<username>/edit/', views.editProfile, name='edit-profile')
]