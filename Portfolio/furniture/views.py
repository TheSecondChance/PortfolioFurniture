from django.shortcuts import render, redirect
from .models import Category, Product, Comment
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def store(request):
    pro = Product.objects.all()
    allLike = Comment.objects.all()
    return render(request, 'store/content.html', {'pro':pro, 'allLike':allLike})

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def listItem(request):
    if request.user.is_authenticated:
        
        category = request.GET.get('category')
        if category == None:
            product = Product.objects.all()
        else:
            product = Product.objects.filter(category__name=category)

        categories = Category.objects.all()
        context = {
            'products':product,
            'categories': categories
        }
        return render(request, 'store/category.html', context)

    else:
        pro = Product.objects.all().order_by()[:2]
        return render(request, 'store/content.html', {'pro': pro})

def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'store/loginAndRegister.html', context)

def loginUser(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have been LogedIn"))
            return redirect('content')
        else:
            messages.success(request, ("Something Error"))
            return redirect('login')
    else:
        context = {'form':form}
        return render(request, 'store/login.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('content')
