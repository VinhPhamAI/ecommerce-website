from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Book
import requests
from django.core.files import File
import random
import logging

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
    # Lấy tất cả các sách
    all_books = list(Book.objects.all())
    # Chọn 10 sách ngẫu nhiên
    random_books = random.sample(all_books, min(10, len(all_books)))

    # Render trang với danh sách sách
    return render(request, 'landing_page.html', {'books': random_books})

def log_out(request):
    logout(request)
    return redirect('landing_page')

@login_required
def update_profile(request):
    # Nếu Profile không tồn tại, tạo mới
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Lấy dữ liệu từ form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        
        # Cập nhật thông tin profile
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.email = email
        user_profile.phone_number = phone_number
        user_profile.gender = gender
        user_profile.date_of_birth = date_of_birth
        user_profile.address = address
        user_profile.save()
        
        return redirect('landing_page')  # Hoặc chuyển hướng đến một trang khác nếu cần

    # Render template với thông tin hiện tại của profile
    return render(request, 'profile.html', {'user_profile': user_profile})



def user_login(request): 
    """View function for user login"""
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
                    login(request, user)  # Use `auth_login` instead of `login`
                    return redirect('landing_page')  # Redirect to dashboard after successful login
                else: 
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else: 
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def cart_view(request):
    profile = request.user.profile
    cart_books = profile.cart_books.all()
    total_amount = sum(book.price for book in cart_books)
    context = {
        'cart_books': cart_books,
        'total_amount': total_amount,
    }
    return render(request, 'cart.html', context)

@login_required
def checkout(request):
    return render(request, 'checkout.html')

@login_required
def manage_product(request):
    return render(request, 'manage_product.html')

@login_required
def add_product(request):
    return render(request, 'add_product.html')

@login_required
def book_detail(request, isbn):
    # Truy vấn sách từ cơ sở dữ liệu dựa trên ISBN
    book = get_object_or_404(Book, isbn=isbn)
    # Truyền sách vào template
    return render(request, 'book_detail.html', {'book': book})

@login_required
def add_to_cart(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    print("add_to_cart view was called")
    try:
        profile = request.user.profile
        logging.info(f"Profile found: {profile}")  # Log thông tin của profile
        print(f"Profile found: {profile}")  # In thông tin của profile ra console
        
        # Thêm sách vào giỏ hàng của user
        profile.cart_books.add(book)
        profile.save()
        
    except Profile.DoesNotExist:
        logging.error("Profile does not exist for the user.")
        print("Profile does not exist for the user.")  # In ra console nếu không tìm thấy profile
    
    return redirect('book_detail', isbn=isbn)