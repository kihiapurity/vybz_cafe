# VybzCafeProject\cafewebsite\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuListCreate.as_view(), name='menu-list-create'),
    path('updates/', views.UpdateListCreate.as_view(), name='update-list-create'),
    path('about-us/', views.about_us, name='about-us'),
    path('footer/', views.footer, name='footer'),
    path('home-settings/', views.home_settings, name='home-settings'),
    path('menu-details/<int:menu_id>/', views.menu_details, name='menu-details'),  # Add this line
]
