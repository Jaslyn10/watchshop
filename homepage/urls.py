"""
URL configuration for watchshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('upload', views.upload_watch, name='upload_watch'),
    path('watches', views.watch_list, name='watch_list'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_wishlist/<int:watch_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('add_to_cart/<int:watch_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_wishlist/<int:watch_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),  # Added path
    path('remove_from_cart/<int:watch_id>/', views.remove_from_cart, name='remove_from_cart'),  # Added path
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
]
