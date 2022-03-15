from django.urls import path
from . import views
from blog.views import UserBlogView, DetailedBlogView, CreateBlogView, UpdateBlogView, DeleteBlogView

urlpatterns=[
    path('blog-home/',views.blog_home,name='blog-home'),
    path('my-blogs/', UserBlogView.as_view(), name = 'my-blogs'),
    path('new-blog', CreateBlogView.as_view(), name = 'new-blog'),
    path('blog/<int:pk>/', DetailedBlogView.as_view(), name = 'blog'),
    path('blog/<int:pk>/update/', UpdateBlogView.as_view(), name = 'update-blog'),
    path('blog/<int:pk>/delete/', DeleteBlogView.as_view(), name = 'delete-blog'),
]
