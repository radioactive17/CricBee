from django.urls import path
from . import views
from blog.views import UserBlogView, CreateBlogView

urlpatterns=[
    path('blog-home/',views.blog_home,name='blog-home'),
    path('my-blogs/', UserBlogView.as_view(), name = 'my-blogs'),
    path('new-blog', CreateBlogView.as_view(), name = 'new-blog'),
]
