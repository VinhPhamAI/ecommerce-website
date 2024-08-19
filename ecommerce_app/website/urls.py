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
    path('cart/', views.shopping_cart, name='shopping_cart'),
    path('credit/', views.checkout, name='credit'),
    path('manage_product/', views.manage_product, name='manage_product'),
    path('add_product/', views.add_product, name='add_product'),
    path('booksdetail', views.book_detail, name='book_detail'),
]
