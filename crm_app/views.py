from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect
from .models import *

from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User

def home_page(request):
    products = Product.objects.all()
    сategories = Categories.objects.all()[:3]
    product_count = Product.objects.all().count()
    remainder = 0
    product_count_honest = 0
    # product_count_honest - четный
    # remainder - остаток
    # product_count_honest = 0
    # remainder = 0
    # remainder = product_count % 3

    # if product_count % 3 == 0:
    #     product_count_honest = product_count / 3
    # else:
    #     product_count_honest = product_count / 3 +  1
    #     # remainder = product_count % 3
    if product_count % 3 == 0:
        product_count_honest = int(product_count / 3)
        remainder = 3
        print(product_count_honest)
        print(remainder)
        pass
    else:
        product_count_honest = int(product_count / 3) + 1
        remainder = 3
        print(product_count_honest)
        print(remainder)
        # remainder = 
        pass

    context = {
        'products' : products,
        'product_count' : range(product_count),
        'product_count_honest' : range(product_count_honest),
        'remainder' : range(remainder),
        'сategories' : сategories,
    }

   

    return render(request, 'crm_app/home.html', context=context)

def make_order(request, slug, id_order):
    сategories = Categories.objects.filter(slug=slug) #[:3]
    foreigh = Product.objects.get(id=id_order)
    set_user = User.objects.get(id=request.user.id)
    print("set_user - ", set_user.id)
    context = {
            'info_prod' : foreigh,
            'сategories' : сategories,
    }
    
    if request.method == 'POST':
        user_name =  request.POST.get('username') # request.user.username 
        user_email = request.POST.get('email') # request.user.email
        Order.objects.create(key_product=foreigh, key_product_user=set_user, name=user_name, email=user_email)
        # return render(request, 'crm_app/complete_order.html')
        return redirect(reverse('profile', args=[str(set_user.id)]))
    else:
        return render(request, 'crm_app/make_order.html', context=context)

def delete_order(request, id_order):
    orders_user = Order.objects.get(id=id_order)
    set_user = User.objects.get(id=request.user.id)
    orders_user.delete()
    return redirect(reverse('profile', args=[str(set_user.id)]))
    

def profile_page(request, id_profile):
    сategories = Categories.objects.all()[:3]
    orders_user = Order.objects.filter(key_product_user=request.user)
    stuff_context = {}
    if request.user.is_staff:
        stuff_context = Order.objects.all()
    context = {
        'orders_user' : orders_user,
        'stuff_context' : stuff_context,
        'сategories' : сategories,
    }
    
        
    return render(request, 'profile.html', context=context)



# --------
# Регистрация нового пользователя
def registration_user(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if User.objects.filter(username=username).exists():
                pass
                # print("Пользователь уже есть..")
            else:
                if password == password2: # если пароли верные
                    User.objects.create_user(username, email, password)
                    # print("Пользователь создан", username)
                    login_user(request)
                    return redirect(reverse("home_page"))
                else:
                    pass # если пароли неверные, написать типо ваш пароль неверный повторите попытку
    return render(request, 'authorization/registration.html')

# --------
# Вход в личный кабинет
def login_user(request):
    context = {}
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active: # user.is_active: если пользователь активен, наверное
                login(request, user)
                # print("Пользователь найден", user.username)
                return redirect(reverse("home_page"))
            else:
                pass
                # print("Пользователь не найден")
    return render(request, 'authorization/login.html', context=context)

# --------
# Выход из личного кабинета
def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

# Функция обработки заказов
def make_process(request, id_profile, id_order):
    categories = Categories.objects.all()
    print(categories)
    process = Order.objects.get(id=id_order)
    context = {
        'process' : process,
    }
    return render(request, 'crm_app/make_process.html', context=context)