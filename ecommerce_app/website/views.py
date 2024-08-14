from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Hoặc chuyển hướng đến một trang khác sau khi đăng ký thành công
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

# Create your views here.
def landing_page(request):
    return render(request, "cart.html")
