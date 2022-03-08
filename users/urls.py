from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

urlpatterns=[
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},  name = 'logout'),
]
