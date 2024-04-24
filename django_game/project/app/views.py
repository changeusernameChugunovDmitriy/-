from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm
from .models import User, Skin


def home(request):
    user = request.user
    if user.is_authenticated:
        user_skins = request.user.skins.all()
        return render(request, 'home.html',
                      context={"user": user, "user_skins": user_skins})
    return render(request, 'home.html',
                  context={"user": user})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            fio = request.POST.get('fio')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(email=email).exists():
                error = "Пользователь с таким email уже существует"
                return render(request, 'registration.html',
                              {'form': form, 'error': error})
            user = User.objects.create_user(fio=fio, email=email,
                                            password=password, username=email
                                            )
            return redirect("login")
        else:
            return render(request, 'registration.html',
                          {'form': form, 'error': form.errors})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html',
                  {'form': form, 'error': form.errors})


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            skin = Skin.objects.get(id=1)
            user.skins.add(skin)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = "Неверный email или пароль"
                return render(request, 'login.html',
                              {'form': form, 'error': error})
    return render(request, 'login.html', {'form': form})


def shop(request):
    skin = Skin.objects.all()
    return render(request, 'shop.html', {"skins": skin})


def shop_add(request, id):
    user = request.user
    skin = Skin.objects.get(id=id)
    if user.money >= skin.price:
        user.skins.add(skin)
        user.money -= skin.price  # Вычитаем стоимость скина из баланса пользователя
        user.save()
        return redirect('home')
    else:
        skin = Skin.objects.all()
        return render(request, 'shop.html', {"skins": skin})


def logout_view(request):
    logout(request)
    return redirect('home')


def add_money(request, ball):
    user = request.user
    user.money += ball
    user.save()
    user_skins = request.user.skins.all()
    return render(request, 'home.html',
                  context={"user": user, "user_skins": user_skins})
