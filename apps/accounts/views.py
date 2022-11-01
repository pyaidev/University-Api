from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.profiles.models import Profile

def login_view(request):
    if request.user.is_authenticated:
        return redirect('account:logout')
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'registration/logout.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('account:logout')
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            # creating prifile
            Profile.objects.create(
                account=user,
                role=form.data.get('role')
            )
            return redirect('/profile/')
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)
