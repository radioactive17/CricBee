from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('timeline/', views.timeline, name = 'timeline'),\
    path('news/', views.news, name = 'news'),
    path('<int:pk>/detailed-news/', views.detailed_news, name = 'detailed-news'),
    path('fixtures/<str:fixture_type>/', views.fixtures, name = 'fixtures'),
    path('', include('users.urls')),
]
