from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('', views.landing_page, name="landing_page"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.update_profile, name='profile'),
    path('cart/', views.cart_view, name='shopping_cart'),
    path('credit/', views.checkout, name='credit'),
    path('manage_product/', views.manage_product, name='manage_product'),
    path('add_product/', views.add_product, name='add_product'),
    path('book/<str:isbn>/', views.book_detail, name='book_detail'),
    path('add-to-cart/<str:isbn>/', views.add_to_cart, name='add_to_cart'),
    path('books/<str:genre>/', views.book_list, name='book_list'),
    path('search/', views.search_books, name='search_books'),
]
