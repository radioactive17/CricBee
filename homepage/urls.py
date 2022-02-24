from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('timeline/', views.timeline, name = 'timeline'),\
    path('news/', views.news, name = 'news'),
    path('<int:pk>/detailed-news/', views.detailed_news, name = 'detailed-news'),
    path('signin',views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
