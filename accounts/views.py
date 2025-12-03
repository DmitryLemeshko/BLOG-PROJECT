from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm

# Реєстрація користувача
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} створено!')
            login(request, user)  # Автоматичний вхід після реєстрації
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Логін користувача
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Ви увійшли як {username}')
                return redirect('home')
            else:
                messages.error(request, 'Невірний логін або пароль')
        else:
            messages.error(request, 'Невірний логін або пароль')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Вихід користувача
def logout_view(request):
    logout(request)
    messages.info(request, 'Ви вийшли з аккаунту')
    return redirect('home')
