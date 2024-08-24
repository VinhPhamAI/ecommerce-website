from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import *
import random
import logging
import string
from django.db.models import Q
import json
from django.http import JsonResponse
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})



def landing_page(request):

    all_books = list(Book.objects.all())     
    random_books = random.sample(all_books, min(12, len(all_books)))
    user_profile = None
    if request.user.is_authenticated:
        user_profile, created = Profile.objects.get_or_create(user=request.user)
    # Render trang với danh sách sách
    return render(request, 'landing_page.html', {'books': random_books, 'user_profile': user_profile})


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
        payment_method = request.POST.get('payment_method')
        
        # Chỉ cập nhật các trường nếu chúng có giá trị
        if first_name:
            user_profile.first_name = first_name
        if last_name:
            user_profile.last_name = last_name
        if email:
            user_profile.email = email
        if phone_number:
            user_profile.phone_number = phone_number
        if gender:
            user_profile.gender = gender
        if date_of_birth:
            user_profile.date_of_birth = date_of_birth
        if address:
            user_profile.address = address
        if payment_method:
            user_profile.payment_method = payment_method
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


@csrf_exempt
@require_POST
def update_order_items(request):
    try:
        data = json.loads(request.body)
        cart_items = data.get('cart_items', [])
        user_profile = request.user.profile
        
        # Clear existing order items for this user
        ShoppingCart.objects.filter(profile=user_profile).delete()
        
        for item in cart_items:
            isbn = item['isbn']
            quantity = int(item['quantity'])
            book = Book.objects.get(isbn=isbn)
            
            # Create or update OrderItem for this book
            ShoppingCart.objects.create(
                profile=user_profile,
                book=book,
                quantity=quantity
            )
        
        return JsonResponse({'success': True})
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'success': False, 'error': str(e)})


@login_required
def cart_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        if 'remove_book_id' in request.POST:
            book_id = request.POST.get('remove_book_id')
            book = get_object_or_404(Book, isbn=book_id)
            profile.cart_books.remove(book)
            profile.save()

    cart_books = profile.cart_books.all()
    total_amount = sum(book.price for book in cart_books)

    truncated_books = []
    for book in cart_books:
        if len(book.title) > 20:
            truncated_title = book.title[:20] + '...'
        else:
            truncated_title = book.title
        truncated_books.append({
            'book': book,
            'truncated_title': truncated_title
        })
    
    context = {
        'cart_books': truncated_books,
        'total_amount': total_amount,
    }
    return render(request, 'cart.html', context)



@login_required
def checkout(request):
    profile = request.user.profile
    order_items = ShoppingCart.objects.filter(profile=profile)

    # Calculate total amount with shipping
    total_amount = sum(item.book.price * item.quantity for item in order_items)
    shipping_cost = Decimal(5.00)  # Adjust as needed
    total_amount_with_ship = total_amount + shipping_cost
    first_name = profile.first_name
    last_name = profile.last_name
    name = first_name + " " + last_name
    context = {
        'order_items': order_items,
        'total_amount': total_amount,
        'shipping_cost': shipping_cost,
        'total_amount_with_ship': total_amount_with_ship,
        'name': name,
        'phone': profile.phone_number,
        'email': profile.email,  # Email comes from the User model
        'address': profile.address,
        'payment_method': profile.payment_method,
    }
    return render(request, 'checkout.html', context)

def search_books(request):
    query = request.GET.get('q', '')  # Get search query from search bar
    genre_books = {}

    if query:
        # Get books matching the search query
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(isbn__icontains=query) |
            Q(genres__icontains=query)
        ).distinct()  # Ensure distinct results

        # Limit results to 60
        limited_results = results[:100]

        # Group books by genre
        for book in limited_results:
            genres = book.genres.split(',')  # Assuming genres are comma-separated
            for genre in genres:
                genre = genre.strip()  # Remove any extra whitespace
                if genre not in genre_books:
                    genre_books[genre] = []
                genre_books[genre].append(book)

    context = {
        'genre_books': genre_books,
        'query': query,
    }

    return render(request, 'book_list.html', context)

@login_required
def manage_product(request):
    products = Product.objects.filter(user=request.user)
    books = Book.objects.filter(product_books__in=products)

    return render(request, 'manage_product.html', {'books': books})

@login_required
def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year_of_publication = request.POST.get('year_of_publication')
        image_url_l = request.POST.get('image_url_l')
        price = request.POST.get('price')
        genres = request.POST.get('genres')
        description = request.POST.get('description')
        pages = request.POST.get('pages')
        number_of_books = request.POST.get('number_of_books')

        # Tạo productId tự động
        title_prefix = title[:5].upper()  # Lấy 5 chữ cái đầu tiên của tên sản phẩm
        random_suffix = ''.join(random.choices(string.digits, k=5))  # 5 số ngẫu nhiên
        isbn = f"{title_prefix}{random_suffix}"
        print(isbn)
        # Tạo một đối tượng Book mới và lưu vào cơ sở dữ liệu
        book = Book(
            isbn=isbn,
            title=title,
            author=author,
            year_of_publication=year_of_publication,
            publisher=request.user,
            image_url_l=image_url_l,
            price=price,
            genres=genres,
            rating=request.POST.get('rating'),
            description=description,
            pages=pages,
            number_of_books=number_of_books
        )
        book.save()
        # Cập nhật Profile của người dùng hiện tại
        if request.user.is_authenticated:
            product = Product(
                user=request.user,
                title=title,
                description=description,
                price=price,
            )
            product.save()
            product.book_product.add(book)  # Add the new book to the product
            product.save()

        # Chuyển hướng đến trang thành công hoặc một view khác
        return redirect('landing_page')

    return render(request, 'add_product.html')

from website.AI.model_ai import infer

@login_required
def book_detail(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)

    try:
    # Truy vấn sách từ cơ sở dữ liệu dựa trên ISBN
        similar_isbns = infer(isbn)
    # Fetch similar books from the database
        similar_books = Book.objects.filter(isbn__in=similar_isbns)
    except ValueError as e:
        all_books = list(Book.objects.all())  
        similar_books = random.sample(all_books, min(12, len(all_books)))
    # Truyền sách vào template
    return render(request, 'book_detail.html', {
        'book': book,
        'similar_books': similar_books
    })

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
    
    return redirect('shopping_cart')

def book_list(request, genre):
    # Filter books by the selected genre
    books = Book.objects.filter(genres__icontains=genre)
    
    # Convert QuerySet to list
    books_list = list(books)
    
    # Sample from the list
    random_books = random.sample(books_list, min(12, len(books_list))) if books_list else []
    
    # Prepare the context for the template
    context = {
        'genre_books': {genre: random_books},  # Pass the books grouped by the genre
        'genre': genre,
    }
    return render(request, 'book_list.html', context)

@login_required
def purchase_order(request):
    orders = Order.objects.filter(user=request.user)
    books = Book.objects.filter(order_books__in=orders)
    return render(request, "purchase_oder.html", {'books': books})

@login_required
def confirm_order(request):
    profile = request.user.profile
    order_items = ShoppingCart.objects.filter(profile=profile)

    total_amount = sum(item.book.price * item.quantity for item in order_items)
    shipping_cost = Decimal(5.00)  # Adjust as needed
    total_amount_with_ship = total_amount + shipping_cost
    # Create a new Order object
    order = Order(
        user=request.user,
        name=f"{profile.first_name} {profile.last_name}",
        phone_number=profile.phone_number,
        email=profile.email,
        address=profile.address,
        payment_method=profile.payment_method,
        price=total_amount,
        shipping_cost=shipping_cost,
        total_cost=total_amount_with_ship
    )
    order.save()

    # Add books to the Order's ManyToMany field
    order.book_order.set(item.book for item in order_items)

    for item in order_items:
        book = item.book
        # If the quantity in the order matches the number of books in stock, delete the book entry
        print("item :", item.quantity)
        print(book.number_of_books)
        book.number_of_books = book.number_of_books - item.quantity
        
        book.save()

    ShoppingCart.objects.filter(profile=profile).delete()
    profile.cart_books.clear()
    return render(request, "checkout_success.html")