from django.urls import path
from . import views

urlpatterns=[
    path('blog-home/',views.blog_home,name='blog-home'),
]
