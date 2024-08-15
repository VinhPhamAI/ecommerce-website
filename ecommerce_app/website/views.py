from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('login')  # Hoặc chuyển hướng đến một trang khác sau khi đăng ký thành công
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

@login_required
def dashboard(request): 
    return render(request, 'dashboard.html')

# Create your views here.
def landing_page(request):
    return render(request, "landing_page.html")


def login(request): 
    """Hàm view của user login"""
    if request.method == 'POST': 
        form = LoginForm(data=request.POST)

        if form.is_valid(): 
            cd = form.cleaned_data
            user = authenticate(
                request, 
                username=cd['username'], 
                password=cd['password']
            )
            if user is not None: 
                if user.is_active: 
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else: 
                    return HttpResponse('Disabled account')
            else : 
                return HttpResponse('Invalid login')

    else : 
        form = LoginForm()
    return render(request, 'login.html', {'form': form})