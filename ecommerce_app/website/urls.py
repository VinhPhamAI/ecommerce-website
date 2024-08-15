from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('', views.landing_page, name="landing_page"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.log_out, name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('sign_up/', auth_views.LoginView.as_view(template_name='sign_up.html'), name='sign_up'),
]
