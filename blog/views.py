from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

@login_required
def blog_home(request):
    blogs=Blog.objects.all()
    context={
        'blogs':blogs,
    }
    return render(request,'blog/blog-home.html', context)

class UserBlogView(LoginRequiredMixin, ListView):
    def get_queryset(self, *args, **kwargs):
        return Blog.objects.filter(author = self.request.user)
    context_object_name = 'blogs'
    template_name = 'blog/myblogs.html'
    paginate_by = 5

class DetailedBlogView(LoginRequiredMixin, DetailView):
    model = Blog


class CreateBlogView(LoginRequiredMixin, CreateView):
     model = Blog
     fields = ['title', 'content', 'images']
     def form_valid(self, form):
         form.instance.author = self.request.user
         form.instance.date_posted = datetime.today()
         return super().form_valid(form)

class UpdateBlogView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'content', 'images']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False

class DeleteBlogView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Blog
    context_object_name = 'blog'
    success_url = '/my-blogs/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False
