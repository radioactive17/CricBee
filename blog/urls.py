from django.urls import path
from . import views

urlpatterns=[
    path('blog-home/',views.index,name='blog-home'),
]
