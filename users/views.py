from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserUpdateForm, BeesUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulations {username}, you are now a part of Cricbee Community')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        b_form = BeesUpdateForm(request.POST, request.FILES, instance = request.user.bees)
        if u_form.is_valid() and b_form.is_valid():
            u_form.save()
            b_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        b_form = BeesUpdateForm(instance = request.user.bees)

    context = {
        'u_form': u_form,
        'b_form': b_form,
    }
    return render(request, 'users/profile.html', context)
