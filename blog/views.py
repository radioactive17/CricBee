from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def blog_home(request):
    blogs=Blog.objects.all()
    context={
        'blogs':blogs,
    }
    return render(request,'blog/blog-home.html', context)
