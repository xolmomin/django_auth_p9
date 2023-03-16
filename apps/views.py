from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.forms import CustomUserCreationForm


def main_page(request):
    return render(request, 'apps/index.html')


@login_required(login_url='/login')
def product_page(request):
    return render(request, 'apps/product.html')


def logout_page(request):
    logout(request)
    return redirect(reverse('login_page'))


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.data['username'], password=form.data['password'])
            if user:
                login(request, user)
                return redirect(reverse('main_page'))
    return render(request, 'apps/auth/login.html')


def register_page(request):
    context = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Saytdan royhatdan otdingiz!")
            return redirect(reverse('login_page'))
        context['form'] = form

    return render(request, 'apps/auth/login.html', context)
